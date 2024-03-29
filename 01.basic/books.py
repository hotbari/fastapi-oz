## books.py

from fastapi import FastAPI, APIRouter

# 로컬 메모리 DB - 서버 종료시 데이터 사라짐

BOOKS = [
    {
        "id":1,
        "title":"채식주의자",
        "author":"한강",
        "url":"http://www.yes24.com/241516734"
    }
]

app = FastAPI()
router = APIRouter()

# 루트페이지
@router.get('/', status_code=200)
def main():
    return {'Message':'Welcome Book'}


# 전체 책 데이터 조회
@router.get('/api/v1/books', status_code=200)
def get_all_books() -> list: #리턴되는 데이터 타입이 list임을 알려줌
    return BOOKS


# 특정 책 데이터 조회
@router.get('/api/v1/books/{book_id}')
def get_book(book_id: int):
    
    # next는 해당 데이터를 1개 찾으면 바로 멈춤
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    if book:
        return book
    return {'error':f'Book not found, Id: {book_id}'}


# 책 생성
@router.post('/api/v1/books/')
def create_book(book: dict):
    BOOKS.append(book)

    return book


# 책 수정
@router.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book_update: dict):
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    for key, value in book_update.items():
        if key in book:
            book[key] = value
    
    return book


# 책 삭제
@router.delete('/api/v1/books/{book_id}')
def delete_book(book_id: int):
    global BOOKS

    BOOKS = [item for item in BOOKS if item['id'] != book_id]

    return {'message':'Book delete'}

# main.py에 등록하는 것 대신
app.include_router(router)

if __name__ == "__main__":
    import uvicorn # 이 안에서만 사용하면 되서 내부 import 형태 많이 사용
    uvicorn.run("books:app", port=8001, reload=True)
