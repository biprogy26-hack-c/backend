from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import crud, models, schemas
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORSを全て許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get("/gifts/get/{user_id}", response_model=schemas.Gift)
def read_gift(user_id: int, db: Session = Depends(get_db)):
    db_gift = crud.get_gift(db, user_id=user_id)
    if db_gift is None:
        raise HTTPException(status_code=404, detail="Gift not found")
    return db_gift

@app.put("/gifts/update/{user_id}", response_model=schemas.Gift)
def update_gift(user_id: int, gift: schemas.GiftUpdate, db: Session = Depends(get_db)):
    db_gift = crud.update_gift(db=db, user_id=user_id, gift=gift)
    if db_gift is None:
        raise HTTPException(status_code=404, detail="Gift not found")
    return db_gift

@app.delete("/gifts/delete/{user_id}", response_model=schemas.Gift)
def delete_gift(user_id: int, db: Session = Depends(get_db)):
    db_gift = crud.delete_gift(db=db, user_id=user_id)
    if db_gift is None:
        raise HTTPException(status_code=404, detail="Gift not found")
    return db_gift

@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/members/get/{user_id}", response_model=schemas.Member)
def read_member(user_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, user_id=user_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.put("/members/update/{user_id}", response_model=schemas.Member)
def update_member(user_id: int, member: schemas.MemberUpdate, db: Session = Depends(get_db)):
    db_member = crud.update_member(db=db, user_id=user_id, member=member)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.delete("/members/delete/{user_id}", response_model=schemas.Member)
def delete_member(user_id: int, db: Session = Depends(get_db)):
    db_member = crud.delete_member(db=db, user_id=user_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member
