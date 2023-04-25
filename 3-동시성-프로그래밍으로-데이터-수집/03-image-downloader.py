import os
import aiohttp
import asyncio
from config import get_secret
import aiofiles


async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url):
    headers = {"X-Naver-Client-Id": get_secret("NAVER_API_ID"),
               "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET")}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result['items']
        images = [item["link"] for item in items]
        # 파일 저장에도 비동기 처리 필요
        await asyncio.gather(*(img_downloader(session, img) for img in images))


async def main():
    # 네이버 검색 OPEN API : 이미지
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    # 1 ~ 10 페이지
    urls = [
        f"{BASE_URL}?query={keyword}&display=20&start={1+i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        # 1 ~ 10까지의 페이지를 동시성으로 크롤링
        await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__main__":
    # Windows의 aiohttp 오류 방지
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
