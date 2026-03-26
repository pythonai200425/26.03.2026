

# TEST DRIVEN DEVELOPMENT
import pytest
from auction import Auction

def test_offer_first_bidding():
    auction = Auction(3)

    actual = auction.offer_bidding(80)
    expected = True

    assert expected == actual

    assert auction.get_offers() == [80]

def test_offer_second_bidding_accepted():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(90) == True
    assert auction.get_offers() == [80, 90]

def test_offer_second_bidding_declined_lower():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(79) == False
    assert auction.get_offers() == [80]

def test_offer_second_bidding_declined_exact():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(80) == False
    assert auction.get_offers() == [80]


def test_offer_second_bidding_exceed_high():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(90) == True
    assert auction.offer_bidding(100) == True
    assert auction.offer_bidding(115) == True
    assert auction.get_offers() == [90, 100, 115]

def test_offer_second_bidding_exceed_decline():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(90) == True
    assert auction.offer_bidding(100) == True
    assert auction.offer_bidding(90) == False
    assert auction.get_offers() == [80, 90, 100]

def test_offer_negative():
    auction = Auction(3)

    assert auction.offer_bidding(-10) == False
    assert auction.get_offers() == []

def test_offer_zero():
    auction = Auction(3)

    assert auction.offer_bidding(0) == False
    assert auction.get_offers() == []

def test_offer_get_winner():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(90) == True
    assert auction.offer_bidding(100) == True
    assert auction.get_winner() == 100

def test_offer_remove_lowest():
    auction = Auction(3)

    assert auction.offer_bidding(80) == True
    assert auction.offer_bidding(90) == True
    assert auction.offer_bidding(100) == True
    assert auction.remove_lowest() == 80
    assert auction.get_offers() == [90, 100]

def test_offer_get_max_offers():
    auction = Auction(3)

    assert auction.get_max_offers() == 3


'''
1
Winner when no offers exist
Assert behavior of get_winner in auction.py on empty auction.
Decide expected contract:
either raise IndexError (current behavior), or
return None / custom exception.

2
Remove lowest when no offers exist
Assert behavior of remove_lowest in auction.py on empty auction.
Current behavior is IndexError; lock this in with a test or change API and test the new behavior.

3
Type robustness for price input -- offer_bidding
Test non-numeric inputs like string/None:

4
check in get_offers that we get a copy

'''