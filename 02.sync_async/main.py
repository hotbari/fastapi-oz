## main.py
# books.py를 실행시키기 위해 main.py 완성시키기

from fastapi import FastAPI
from books import router as books_router
from sync_async_test import router as sync_async_router

app = FastAPI()
app.include_router(books_router)
app.include_router(sync_async_router)


if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("main:app", reload=True)