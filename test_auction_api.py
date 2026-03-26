import pytest
from fastapi.testclient import TestClient
from app import app, auction
from auction import Auction

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_auction():
    client.put("/refresh-auction/3")


def test_bid_accepted():
    response = client.post("/bid", json={"price": 100})
    assert response.status_code == 200
    assert response.json()["accepted"] is True


def test_bid_rejected_zero():
    response = client.post("/bid", json={"price": 0})
    assert response.status_code == 400


def test_bid_rejected_negative():
    response = client.post("/bid", json={"price": -5})
    assert response.status_code == 400


def test_bid_rejected_lower_than_current():
    client.post("/bid", json={"price": 100})
    response = client.post("/bid", json={"price": 50})
    assert response.status_code == 400


def test_get_offers():
    client.post("/bid", json={"price": 80})
    client.post("/bid", json={"price": 90})
    response = client.get("/offers")
    assert response.status_code == 200
    assert 80 in response.json()["offers"]
    assert 90 in response.json()["offers"]


def test_get_winner():
    client.post("/bid", json={"price": 80})
    client.post("/bid", json={"price": 110})
    response = client.get("/winner")
    assert response.status_code == 200
    assert response.json()["winner"] == 110


def test_get_winner_no_bids():
    response = client.get("/winner")
    assert response.status_code == 404


def test_remove_lowest():
    client.post("/bid", json={"price": 80})
    client.post("/bid", json={"price": 90})
    response = client.delete("/lowest")
    assert response.status_code == 200
    assert response.json()["removed"] == 80
    assert 80 not in client.get("/offers").json()["offers"]


def test_remove_lowest_no_bids():
    response = client.delete("/lowest")
    assert response.status_code == 404


def test_max_offers_exceeded_evicts_lowest():
    client.post("/bid", json={"price": 80})
    client.post("/bid", json={"price": 90})
    client.post("/bid", json={"price": 100})
    client.post("/bid", json={"price": 110})
    offers = client.get("/offers").json()["offers"]
    assert 80 not in offers
    assert len(offers) == 3


def test_get_max_offers():
    response = client.get("/max-offers")
    assert response.status_code == 200
    assert response.json()["max_offers"] == 3


def test_refresh_auction():
    client.post("/bid", json={"price": 100})
    response = client.put("/refresh-auction/5")
    assert response.status_code == 200
    assert response.json()["max_offers"] == 5
    assert client.get("/offers").json()["offers"] == []
