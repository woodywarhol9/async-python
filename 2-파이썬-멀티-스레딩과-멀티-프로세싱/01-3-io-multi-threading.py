# thread를 활용한 비동기 처리
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    # 1.5초 정도 걸림
    # 다른 스레드를 concurrency하게 수행
    # 스레드를 구성하고, 우선 순위를 부여하는 것도 쉽지 않음
    # 코루틴 추천!
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10
    # max_workers : 스레드 개수 설정
    executor = ThreadPoolExecutor(max_workers = 10)
    # 세션을 열었다가, 바로 자동으로 닫기 위해서
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)