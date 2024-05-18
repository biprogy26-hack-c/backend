from sqlalchemy.orm import Session
import models, schemas

def get_gift(db: Session, user_id: int):
    return db.query(models.Gift).filter(models.Gift.userId == user_id).first()

def create_gift(db: Session, gift: schemas.GiftCreate):
    db_gift = models.Gift(giftName=gift.giftName, giftPhoto=gift.giftPhoto)
    db.add(db_gift)
    db.commit()
    db.refresh(db_gift)
    return db_gift

def get_member(db: Session, user_id: int):
    return db.query(models.Member).filter(models.Member.userId == user_id).first()

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(
        userName=member.userName,
        portrait=member.portrait,
        homeTown=member.homeTown,
        interest=member.interest,
        meeting=member.meeting
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_gift(db: Session, user_id: int, gift: schemas.GiftUpdate):
    db_gift = db.query(models.Gift).filter(models.Gift.userId == user_id).first()
    if db_gift:
        db_gift.giftName = gift.giftName
        db_gift.giftPhoto = gift.giftPhoto
        db.commit()
        db.refresh(db_gift)
    return db_gift

def delete_gift(db: Session, user_id: int):
    db_gift = db.query(models.Gift).filter(models.Gift.userId == user_id).first()
    if db_gift:
        db.delete(db_gift)
        db.commit()
    return db_gift

def update_member(db: Session, user_id: int, member: schemas.MemberUpdate):
    db_member = db.query(models.Member).filter(models.Member.userId == user_id).first()
    if db_member:
        db_member.userName = member.userName
        db_member.portrait = member.portrait
        db_member.homeTown = member.homeTown
        db_member.interest = member.interest
        db_member.meeting = member.meeting
        db.commit()
        db.refresh(db_member)
    return db_member

def delete_member(db: Session, user_id: int):
    db_member = db.query(models.Member).filter(models.Member.userId == user_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
    return db_member

