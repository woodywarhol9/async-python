# 각 페이지에 대해서 fetch 실행
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
import sys


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        # select를 활용하면 더 깔끔하게 처리할 수 있음
        titles = soup.select("div.cont_thumb > p.txt_thumb")
        for title in titles:
            if title is not None:
                print(title.text)

 
async def main():
    # 비제이리퍼블릭의 전체 출간 도서 URL
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    # 1 ~ 10 페이지
    urls = [f"{BASE_URL}?page{i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        # 1 ~ 10까지의 페이지를 동시성으로 크롤링
        await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__main__":
    # Windows의 aiohttp 오류 방지
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)