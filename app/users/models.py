from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)