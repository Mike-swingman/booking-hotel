import datetime as dt

from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Computed, ForeignKey, Date


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[dt.date] = mapped_column(Date)
    date_to: Mapped[dt.date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    total_days: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from)"))
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from) * price"))

