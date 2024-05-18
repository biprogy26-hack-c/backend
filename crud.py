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
