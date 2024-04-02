from fastapi import FastAPI
from routes.users import router as user_router
from routes.items import router as item_router

app = FastAPI()
app.include_router(user_router) # 장고에서는 setting.py, urls.py가 하는 역할
app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn
    # main.py 파일에서 app 객체를 찾는다
    uvicorn.run("main:app", reload=True)

    # 127.0.0.1:800/docs -> CRUD 테스트
    