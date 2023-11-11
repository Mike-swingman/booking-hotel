from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, ForeignKey


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    services: Mapped[dict] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int]
    image_id: Mapped[int]
