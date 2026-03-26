from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from auction import Auction

app = FastAPI()
auction = Auction(max_offers=3)


@app.get("/")
def index():
    return FileResponse("auction_dashboard.html")


class BidRequest(BaseModel):
    price: int


@app.post("/bid")
def bid(request: BidRequest):
    success = auction.offer_bidding(request.price)
    if not success:
        raise HTTPException(status_code=400, detail="Bid rejected")
    return {"accepted": True, "price": request.price}


@app.get("/winner")
def winner():
    if not auction.get_offers():
        raise HTTPException(status_code=404, detail="No bids yet")
    return {"winner": auction.get_winner()}


@app.delete("/lowest")
def lowest():
    if not auction.get_offers():
        raise HTTPException(status_code=404, detail="No bids to remove")
    removed = auction.remove_lowest()
    return {"removed": removed}


@app.get("/offers")
def offers():
    return {"offers": auction.get_offers()}


@app.get("/max-offers")
def max_offers():
    return {"max_offers": auction.get_max_offers()}


@app.put("/refresh-auction/{max}")
def refresh_auction(max: int):
    global auction
    auction = Auction(max_offers=max)
    return {"refreshed": True, "max_offers": max}
