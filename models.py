from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Gift(Base):
    __tablename__ = "gifts"
    userId = Column(Integer, primary_key=True, index=True)
    giftName = Column(String, index=True)
    giftPhoto = Column(String)

class Member(Base):
    __tablename__ = "members"
    userId = Column(Integer, primary_key=True, index=True)
    userName = Column(String, index=True)
    portrait = Column(String)
    homeTown = Column(String)
    interest = Column(String)
    meeting = Column(String)
