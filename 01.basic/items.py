## items.py

from fastapi import APIRouter

router = APIRouter()

# FastAPI에서는 데코레이터 많이 사용
@router.get('/api/v1/items/{item_id}',
            status_code=200, 
            tags=['items', 'payment'],
            summary='특정 아이템 가져오기',
            description='Item 모델에서 item_id 값을 갖고 특정 아이템 조회')

def get_item(item_id: int):
    return {'items': item_id}

# 