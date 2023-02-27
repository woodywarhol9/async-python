import requests
import time


def fetcher(session, url):
    # url에 해당하는 데이터 반환
    with session.get(url) as response:
        return response.text


def main():
    # Blocking 발생
    # 10초 정도 걸림
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10
    # 세션을 열었다가, 바로 자동으로 닫기 위해서
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        # 모든 데이터 반환
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
