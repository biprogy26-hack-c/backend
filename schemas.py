from pydantic import BaseModel
from typing import Optional

# Gift schemas
class GiftBase(BaseModel):
    giftName: str
    giftPhoto: str

class GiftCreate(GiftBase):
    pass

class GiftUpdate(GiftBase):
    pass

class Gift(GiftBase):
    userId: int

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
    pass

class MemberUpdate(MemberBase):
    pass

class Member(MemberBase):
    userId: int

    class Config:
        orm_mode = True
