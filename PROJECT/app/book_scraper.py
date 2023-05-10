import asyncio
import aiohttp
import sys
from app.config import get_secret


class NaverBookScraper:
    """
    Naver Book api를 활용한 도서 정보 수집기
    """

    BASE_URL = "https://openapi.naver.com/v1/search/book"
    API_ID = get_secret("NAVER_API_ID")
    API_SECRET = get_secret("NAVER_API_SECRET")

    @staticmethod
    async def fetch(session, url, headers):
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    json = await response.json()
                    return json["items"]
        except aiohttp.ClientError as e:
            print(f"Client Error : {e}")

    def unit_url(self, keyword, start):
        return {
            "url": f"{self.BASE_URL}?query={keyword}&display=10&start={start}",
            "headers": {
                "X-Naver-Client-Id": self.API_ID,
                "X-Naver-Client-Secret": self.API_SECRET,
            },
        }

    async def search(self, keyword, total_page):
        apis = [self.unit_url(keyword, 1 + i * 10) for i in range(total_page)]
        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[
                    NaverBookScraper.fetch(session, api["url"], api["headers"])
                    for api in apis
                ]
            )
        result = [data for data in all_data if data is not None]
        result = sum(result, [])
        return result

    def run(self, keyword, total_page):
        return asyncio.run(self.search(keyword, total_page))


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    scraper = NaverBookScraper()
    scraper.run("파이썬", 3)
