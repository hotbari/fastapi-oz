## models.py
## 데이터베이스 테이블 컬럼 정의
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# User 테이블
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String) # 해쉬는 문자열
    # reverse_accessor -> 장고에서는 _set 으로 설정했지만.. FastAPI에서는 이르케
    items = relationship("Item", back_populates="owner") 

# Item 테이블 -> video도 되고,, 뭐도 되고,,, 기본 틀을 제공해준 것
# pk - 테이블 조인하기
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    # 다른 모델에서 User를 가리킬 때 owner라고 함
    owner_id = Column(Integer, ForeignKey('users.id'))

    # 관계 정의
    owner = relationship("User", back_populates="items")
