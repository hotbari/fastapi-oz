heap-stack 차이
힙은 공유되고 스택은 . 왜안됌?
동기 비동기 머라는거임?

ORM을 가능하게 하는 SQLalchemy... -> 설치하면 ORM 쿼리 사용 가능
pymysql -> 디비에 접근 간으하게 해줌 순수 파이썬으로 만들어서 오류가 적지만 속도는 좀 느림 = 동기방식
aiomysql -> 비동기 I/O를 통해 테이터베이스 연산 수행

찾아볼 것ㅌ
DB index -> B tree
비동기-동기오류

파이썬 백엔드씬 탑4
플라스크, 장고, FastAPI, AWS Lambda = 서버리스, slack BOT의 뉴스 알람, 관련 서비스 알람을 만들 수 있다, 가성비 개굿

grafana로 트래픽 보면서 재미 보셨대요


< 수업 과정 >
models.py, database.py, main.py 생성

models.py 코드 작성
sqlalchemy 설치해서 ORM 방식으로 작성 중, 문법은 장고와 좀 다르다.

여기서 User()안에 뭐가 들어가야할 거 ㅅ같은데.. DB연결로 넘어갑니다
오 쉣 database.py 뭐가 뭔지 하나도 모르겠음 ㅈ됌


CRUD를 만들기 위해 crud_orm.py 생성

와! database.py는 하나도 모르겠다!


