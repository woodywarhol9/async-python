import aiohttp
import asyncio
import time
import os
import threading


# 비동기 처리할 함수
async def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    # url에 해당하는 데이터 반환
    # await return을 위해서 async 적어줌
    async with session.get(url) as response:
        # awaitable한 method
        return await response.text()


async def main():
    # 1 초 정도 걸림
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10
    # 세션을 열었다가, 바로 자동으로 닫기 위해서
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)

if __name__ == "__main__":
    start = time.time()
    # 윈도우 환경에서 RuntimeError 해결
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)
