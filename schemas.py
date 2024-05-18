from pydantic import BaseModel

class GiftBase(BaseModel):
    giftName: str
    giftPhoto: str

class GiftCreate(GiftBase):
    pass

class Gift(GiftBase):
    userId: int

    class Config:
        orm_mode: True

class MemberBase(BaseModel):
    userName: str
    portrait: str
    homeTown: str
    interest: str
    meeting: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    userId: int

    class Config:
        orm_mode: True
