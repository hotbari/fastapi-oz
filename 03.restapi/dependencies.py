## 의존성 관리
## DB를 수시로 연결/끊음 반복할 수 없기때문에 connection을 만들어놓고 활용


# SessionLocal은 동기용 의존성(세션 관리)
from database import SessionLocal 
def get_db():
    # db는 SessionLocal을 불러옴
    db = SessionLocal()

    # DB 연결하는 제너레이터 : 연결된 상태를 유지시켜주는 역할
    # yield를 만나면 코드가 멈춤
    # 동기형태의 연결 세션 관리
    try:
        yield db 

    finally:
        db.close()


# 비동기용 의존성(세션 관리)
from database import AsyncSessionLocal
async def get_async_db():
    # sesisonlocal 자체가 await를 받고 있어서 await 하지 않음 
    async with AsyncSessionLocal() as session:
        yield session

    