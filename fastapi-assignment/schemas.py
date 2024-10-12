from pydantic import BaseModel
from datetime import date, datetime

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

class ItemResponse(ItemCreate):
    id: int
    insert_date: datetime

    class Config:
        orm_mode = True

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInResponse(ClockInCreate):
    id: int
    insert_datetime: datetime

    class Config:
        orm_mode = True
