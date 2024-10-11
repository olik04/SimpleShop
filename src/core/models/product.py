from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from core.models.base import Base


class Product(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(length=100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String(length=255), nullable=False)
    category: Mapped[str] = mapped_column(String(length=100), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    rating_count: Mapped[int] = mapped_column(Integer, nullable=False)
