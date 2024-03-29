from pydantic import BaseModel
from typing import Optional # description은 있어도 되고 없어도 되니까

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

# 위에서는 id 값을 유저가 보내줘야되기에 이를 해결하기 위해
# id를 제외한 나머지 columns을 재정의 해줌
# id를 빼야 validation을 통과할 수 있음
    
class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class SearchBook(BaseModel):
    results: Optional[Book]

from typing import List
class SearchBooks(BaseModel):
    results: List[Book]