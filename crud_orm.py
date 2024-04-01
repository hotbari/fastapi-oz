# ORM 방식으로 CRUD
from sqlalchemy.orm import Session
from models import User, Item

# pip install bctypt
import bcrypt 

# User - CRUD
# db 먼저 연결 - db:Session, user:UserCreate
def create_user(db:Session, user:UserCreate):
    # 해쉬화
    hashed_password = bcrypt.hashpw(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user) # 여기까지 로컬에서 작업한 것
    db.commit() # 로컬 작업물을 커밋하여 반영

    return db_user # object->json 알아서 역직렬화 해줌

def get_user(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).fisrt() # 쿼리 결과의 첫번째 값을 리턴

# skip, limit 옵션으로 orm에서 페이지네이션 기능 
def get_users(db:Session, skip: int=0, limit: int=10): 
    db.query(User).offset(skip).limit(limit).all()
    # sql 방식으로는 ; SELECT * FROM users LIMIT 10 OFFSET 10

def update_user(db:Session, user_id: int, user_update: UserUpdate):
    # 업데이트 할 유저데이터 불러오기
    db_user = db.query(User).filter(User.id == user_id).first() # db에서 가져온 객체 유저
    if not db_user:
        return None
    
    user_data = user_update.dict()

    for key, value in user_data.items():
        setattr(db_user, key, value) # setattribute - python 기본 내장 함수
    
    db.commit()
    # 이걸 안하면 return db_user가 이전 데이터를 가져옴
    # 전체 새고는 낭비니까 db_user로 제한
    db.refresh(db_user) 
    return db_user


def delete_user(db:Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    db.delete(db_user)
    db.commit()

    return db_user # 아직 refresh 안해서 메모리상에는 남아있고 if문 등 코드로 delete success 등 만들어주면 댐

# Item - CRUD
