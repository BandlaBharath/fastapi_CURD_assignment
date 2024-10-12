from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    item_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiry_date = Column(Date, nullable=False)
    insert_date = Column(DateTime(timezone=True), server_default=func.now())

class ClockIn(Base):
    __tablename__ = 'clockin'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    insert_datetime = Column(DateTime(timezone=True), server_default=func.now())
