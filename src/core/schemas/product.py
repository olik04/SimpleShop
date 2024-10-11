from typing import Optional
from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    id: int
    title: str
    price: float
    description: str
    image: str
    category: str
    rating: Optional[float] = None
    rating_count: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    title: str
    price: float
    description: str
    image: str
    category: str
    rating: Optional[float] = None
    rating_count: Optional[int] = None


class ProductUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category: Optional[str] = None
    rating: Optional[float] = None
    rating_count: Optional[int] = None
