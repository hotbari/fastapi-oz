# ORM 방식으로 CRUD
from sqlalchemy.orm import Session
from models import User, Item

# pip install bctypt
import bcrypt 

from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate



# User - CRUD
# db 먼저 연결 - db:Session, user:UserCreate(스키마)
# user:UserCreate가 딕셔너리 형태라 스키마 구조에서 충돌이 일어날 수 있기 때문에  orm_mode = True 옵션 설정
def create_user(db:Session, user:UserCreate):
    # 해쉬화
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user) # 여기까지 로컬에서 작업한 것
    db.commit() # 로컬 작업물을 커밋하여 반영

    return db_user # object->json 알아서 역직렬화 해줌

# id기반
def get_user_id(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first() # 쿼리 결과의 첫번째 값을 리턴

# email 기반
def get_user_email(db:Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first() 


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
def item_create(db:Session, item:ItemCreate, owner_id:int):
    ## ** -> key, value 구분
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item


def get_item(db:Session, item_id:int):
    return db.query(Item).filter(Item.id == item_id).first() # get으로 하면 try: except: 예외처리 필수

def get_items(db:Session, skip: int=0, limit: int=10):
    return db.query(Item).order_by(Item.id.desc()).offset(skip).limit(limit).all()

def update_item(db: Session, item_update: ItemUpdate, item_id:int):
    db_item = get_item(db, item_id)

    if not db_item:
        return None
    
    for key,value in item_update.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db:Session, item_id: int):
    db_item = get_item(db, item_id)

    if not db_item:
        return None
    
    db.delete(db_item)
    db.commit()

    return True