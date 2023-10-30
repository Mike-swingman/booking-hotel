from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels", response_model=list[SHotel])
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: bool = None,
    stars: int = Query(None, ge=1, le=5)
):
    hotels = [
        {
            "address": "GEORGIA, BATUMI, STREET KHIMSHIASHVILI SHERIF 5",
            "name": "COURTYARD BATUMI MARRIOTT",
            "stars": 5,
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass
