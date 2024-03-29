from fastapi import APIRouter
from typing import List, Optional
from models import Book, CreateBook, SearchBooks

router = APIRouter()

# 실제 데이터 validation 방식
books: List[Book] = [] # [Book, Book, Book, ...]

@router.post('/')
# return을 Book 형태로 제한 
# id를 숨기기 위해 CreatBook으로 반환하면 id값이 없기 때문에 검증 오류가 발생하므로 반환은 Book으로!
def create_book(book: CreateBook) -> Book: 
    book = Book(id=len(books)+1, **book.model_dump())
    books.append(book)

    return book # id 포함

# 검색 기능
# search_book과 search_books의 차이
# 내려주는 데이터 체킹이 FastAPI의 장점

@router.get('/search/')
# 키워드 입력 안해도 검색 가능 Optional
# 페이지네이션을 위한 max_results
def search_books(keyword: Optional[str], max_results: int =10) -> SearchBooks:
    search_result = [book for book in books if keyword in book.title] if keyword else books
    return SearchBooks(results=search_result[:max_results]) # validation Checking