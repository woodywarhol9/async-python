import aiohttp
import asyncio
from config import get_secret


async def fetch(session, url):
    headers = {"X-Naver-Client-Id": get_secret("NAVER_API_ID"),
               "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET")}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result['items']
        images = [item["link"] for item in items]
        print(images)


async def main():
    # 네이버 검색 OPEN API : 이미지
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    # 1 ~ 10 페이지
    urls = [
        f"{BASE_URL}?query={keyword}&display=20&start={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        # 1 ~ 10까지의 페이지를 동시성으로 크롤링
        await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__main__":
    # Windows의 aiohttp 오류 방지
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())