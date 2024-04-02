from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_db
from schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session
import crud_orm
from typing import Union

router = APIRouter(tags=['User'])

# api/v1/user
# CRUD + 데코레이터
@router.post('/') # 경로가 root
def create_user(user: UserCreate, db:Session = Depends(get_db)): # Depends를 통해 get_db를 불러와야 알아서 의존성 관리를 해줌
    # from crud_orm import create_user 할 경우 함수명과 동일하여 오류 발생할 수 있어 이렇게 사용
    db_user = crud_orm.create_user(db, user) 
    return db_user

# data를 받아서 숫자와 문자 모두로 검색 가능하도록 문자로 받음
@router.get('/{user_data}/') 
def get_user(user_data: Union[int, str], db:Session = Depends(get_db)):
    try:
        user_data = int(user_data)
        db_user = crud_orm.get_user_id(db, user_data)
    except:
        user_data = str(user_data)
        db_user = crud_orm.get_user_email(db, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.get('/')
def get_users(skip: int, limit: int, db: Session = Depends(get_db)):
    crud_orm.get_users(db, skip, limit)


@router.put('/{user_id}')
def update_user(user_id:int, user_update:UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud_orm.update_user(db, user_id, user_update)

    if updated_user in None:
        raise HTTPException(404, 'User not found')
    return updated_user

@router.delete('/{user_id}')
def delete_user(db, user_id: int):
    deleted_user = crud_orm.delete_user(db, user_id)

    if deleted_user is None:
        raise HTTPException(404, 'User Not Found')
    
    return deleted_user

