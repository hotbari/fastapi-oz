from fastapi import APIRouter
import time

router = APIRouter()

@router.get('/slow-sync-ping')
def slow_sync_ping():
    time.sleep(5) # 10초가 걸리는 작업
    return {'msg':'pong'}

# 비동기 동작
import asyncio
@router.get('/slow-async-ping')
async def slow_async_ping():
    await asyncio.sleep(5) # 10초를 기다리지만 다른 코드들은 계속 실행 중

    return {'msg':'pong'}

## 10초가 걸리는 작업은 동기? 비동기? -> 오래 걸리는 작업은 비동기로 하면 안됨 왜요왜요
# CPU에 부하가 걸리는 복잡한 연산은 동기!
# Input/Output(I/O)는 비동기!

def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    result = fibonacci(35)
    return result

# Worst case
# CPU가 굉장히 많이 사용되는 알고리즘 코드인데 FastAPI 성능 자체에 문제가 생기고
# CPU 부하로 인해 Event Loop에 부하가 걸린다
# 비동기에서 썡으로 쓰는 케이스
async def cpu_hard_tast():
    result = await cpu_intensive_task()
    return {'msg':result}


# Good case
# CPU에 부하가 많이 걸리는 작업은 Event Loop에서 분리 후
# 별도의 프로세스에서 실행시킨다
# FastAPI는 프로세스에 접근하게 해준다
from concurrent.futures import ProcessPoolExecutor
def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task
        )

    return {'result':result}
