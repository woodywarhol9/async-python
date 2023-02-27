import requests
import time
import os
import threading


def fetcher(session, url):
    # os.getpid() : 현재 프로세스의 pid를 반환
    # threading.get_ident() : 스레드의 id를 반환
    print(f"{os.getpid()} process | {threading.get_ident()} url {url}")
    # url에 해당하는 데이터 반환
    with session.get(url) as response:
        return response.text


def main():
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
