## main.py

from fastapi import FastAPI
from items import router as item_router
from users import router as users_router
from books import router as books_router

# FastAPI는 Starlette를 부모 클래스로 상속한다
app = FastAPI()

app.include_router(item_router)
app.include_router(users_router)


# router
# Django에서는 <int:item_id> 형태로 받아왔는데 여기서는 변수로만 받아오면 된다
# 매개변수로 입력할 때 타입힌트 작성
# q는 쿼리 - /items/123?name=hotbari 할 때 items/ 뒤에 붙는 부분


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    # ASGI 서버는 uvicorn을 사용하여 실행
    import uvicorn
    # 포트는 설정할 필요없지만 8000임을 알아두기
    # 디버그 모드
    # 저장하면 서버가 reload 되도록 설정
    uvicorn.run("main:app", port=8000, log_level='debug', reload=True)
    