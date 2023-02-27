import time
# 비동기 처리를 위한 라이브러리
import asyncio
# coroutine : 진입점과 탈출점이 여러 개 존재하는 루틴
# 추가로 await가 진입 - 탈출점 역할을 함


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")


async def main():
    await asyncio.gather(
        delivery("A", 3),
        delivery("B", 3),
        delivery("C", 4),
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
