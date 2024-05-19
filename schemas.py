from pydantic import BaseModel
from typing import Optional

# Gift schemas
class GiftBase(BaseModel):
    giftName: str
    giftPhoto: str

class GiftCreate(GiftBase):
    userId: str

class GiftUpdate(GiftBase):
    pass

class Gift(GiftBase):
    userId: str

    class Config:
        orm_mode = True

# Member schemas
class MemberBase(BaseModel):
    userName: str
    portrait: str
    homeTown: str
    interest: str
    meeting: str

class MemberCreate(MemberBase):
    userId: str

class MemberUpdate(MemberBase):
    pass

class Member(MemberBase):
    userId: str

    class Config:
        orm_mode = True
