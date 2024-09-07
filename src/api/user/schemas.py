from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):  # User model that could be seen by customer
    username: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
