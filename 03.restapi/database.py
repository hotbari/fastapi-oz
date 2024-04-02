from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


## 동기용 데이터 베이스 접속 명령어 -> 은행
# pymysql 사용해서 DB 연결 해줌
# oz-password은 DB 이름
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:oz-password@localhost/oz-fastapi'
# 해당 url에 접속 요청
engine = create_engine(SQLALCHEMY_DATABASE_URL) 
# 세션을 만드는 이유?
# 요청 할 때마다 DB 접속하는게 비효율적이라서 세션 기반으로 연결 상태 유지
# sessionmaker로 ... 뭐 관리
SessionLocal = sessionmaker(bind=engine)


## 비동기용 데이터 베이스 접속 명령어 (aiomysql) -> 랭킹 같은거
# 무거운 I/O 요청이 먼저 와도, 뒤에 가벼운 I/O 작업 요청이 들어오면 먼저 끝냄
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
ASYNC_SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://root:oz-password@localhost/oz-fastapi'
engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL) 
AsyncSessionLocal = sessionmaker(bind = engine, class_=AsyncSession)

from sqlalchemy.ext.declarative import declarative_base
# 나중에 이 베이스를 각각의 모델이 상속 받도록 함, 테이블 매핑, 컬럼 생성 등 
# models.py에 import해서 상속받게 함
Base = declarative_base() 