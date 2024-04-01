## pydantic으로 데이터 유효성 검증
from pydantic import BaseModel

# from models import Item
# 스키마 안에서는 import 하지 않고 만들어줌

from typing import List




class Item(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str

    # ORM 방식으로 사용하기 위해 설정
    class Config:
        orm_mode = True


# email을 따로 분리
class UserBase(BaseModel):
    email:str


class User(UserBase):
    id: int
    # 비밀번호는 받지 않아도 됨
    items: List[Item] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    # 둘 중 하나만 업데이트 할 경우에 | None = None
    email: str | None = None
    password: str | None = None


# ^ 시리얼라이즈에서 해주던 걸 스키마에서 정의 ^