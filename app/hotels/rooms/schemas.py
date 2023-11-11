from pydantic import BaseModel


class SRooms(BaseModel):
    hotel_id: int
    name: str
    description: str
    price: int
    services: dict
    quantity: int
    image_id: int
