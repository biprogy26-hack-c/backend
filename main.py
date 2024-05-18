from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/gifts/", response_model=schemas.Gift)
def create_gift(gift: schemas.GiftCreate, db: Session = Depends(get_db)):
    return crud.create_gift(db=db, gift=gift)

@app.get("/gifts/{user_id}", response_model=schemas.Gift)
def read_gift(user_id: int, db: Session = Depends(get_db)):
    db_gift = crud.get_gift(db, user_id=user_id)
    if db_gift is None:
        raise HTTPException(status_code=404, detail="Gift not found")
    return db_gift

@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/members/{user_id}", response_model=schemas.Member)
def read_member(user_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, user_id=user_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member
