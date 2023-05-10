from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.models import mongodb, BookModel
from app.book_scraper import NaverBookScraper


BASE_DIR = Path(__file__).resolve().parent  # app 경로를 절대 경로로 지정

app = FastAPI()

templates = Jinja2Templates(
    directory=f"{BASE_DIR}/templates"
)  # dir : serving할 HTML 파일 위치 -> 절대 경로 지정


# 라우팅 : 요청받은 URL을 해석 하여 그에 맞는 함수를 실행하고, 결과를 리턴하는 행위
@app.get("/", response_class=HTMLResponse)  # response_class : Jinja를 사용하니 HTML
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "도서 정보 수집기"}
    )


# search form에 결과 전달
@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    # 조건 1 : 검색어 입력이 없는 경우
    if not q:
        return templates.TemplateResponse(
            "index.html", {"request": request, "title": "도서 정보 수집기"}
        )
    # 조건 2 : 기존 검색 목록이 있는 경우
    if await mongodb.engine.find_one(BookModel, BookModel.keyword == q):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == q)
        return templates.TemplateResponse(
            "index.html", {"request": request, "title": "도서 정보 수집기", "books": books}
        )

    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(q, 10)
    book_models = []
    for book in books:
        book_models.append(
            BookModel(
                keyword=q,
                publisher=book["publisher"],
                discount=book["discount"],
                image=book["image"],
            )
        )
    # save_all : asyncio.gather와 동일
    await mongodb.engine.save_all(book_models)
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "도서 정보 수집기", "books": books}
    )


# 서버 시작 시
@app.on_event("startup")
def on_app_start():
    mongodb.connect()


# 서버 다운 시
@app.on_event("shutdown")
async def on_app_shutdown():
    mongodb.close()
