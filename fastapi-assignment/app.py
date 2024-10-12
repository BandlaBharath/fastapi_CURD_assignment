from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Item, ClockIn
from schemas import ItemCreate, ItemResponse, ClockInCreate, ClockInResponse
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{id}", response_model=ItemResponse)
def get_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{id}", response_model=ItemResponse)
def update_item(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.post("/clock-in", response_model=ClockInResponse)
def clock_in(clock_in: ClockInCreate, db: Session = Depends(get_db)):
    db_clock_in = ClockIn(**clock_in.dict())
    db.add(db_clock_in)
    db.commit()
    db.refresh(db_clock_in)
    return db_clock_in

@app.get("/clock-in/{id}", response_model=ClockInResponse)
def get_clock_in(id: int, db: Session = Depends(get_db)):
    db_clock_in = db.query(ClockIn).filter(ClockIn.id == id).first()
    if not db_clock_in:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return db_clock_in

@app.put("/clock-in/{id}", response_model=ClockInResponse)
def update_clock_in(id: int, clock_in: ClockInCreate, db: Session = Depends(get_db)):
    db_clock_in = db.query(ClockIn).filter(ClockIn.id == id).first()
    if not db_clock_in:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    for key, value in clock_in.dict().items():
        setattr(db_clock_in, key, value)
    db.commit()
    db.refresh(db_clock_in)
    return db_clock_in

@app.delete("/clock-in/{id}")
def delete_clock_in(id: int, db: Session = Depends(get_db)):
    db_clock_in = db.query(ClockIn).filter(ClockIn.id == id).first()
    if not db_clock_in:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    db.delete(db_clock_in)
    db.commit()
    return {"message": "Clock-in record deleted successfully"}
