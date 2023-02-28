### 컴퓨터 구성 요소

- CPU : 명령어를 해석하여 실행하는 장치
- 메모리
    - 주 메모리 : 작업에 필요한 프로그램과 데이터를 저장
        - RAM
    - 보조 메모리 : 저장 장치라고 불리며 데이터를 일시적 또는 영구적으로 저장
        - HDD, SSD
- 입출력 장치
    - 키보드, 마우스, 디스플레이 등등
- 시스템 버스
    - 각각의 구성 요소를 연결해주는 역할

### 프로세스

- 프로그램 : 저장 장치에 저장된 정적인 상태
- 프로세스 : 실행을 위해 주 메모리에 올라온 동적인 상태
- 프로그램 : 어떤 문제를 해결하기 위해 컴퓨터에게 주어지는 처리 방법과 순서를 기술한 일련의 명령문의 집합체
    - 개발자가 작성한 정적인 상태의 코드들
    - 프로그램은 HDD, SSD와 같은 보조 메모리에 보관 됨
- 프로그램의 실행
    - 해당 프로그램의 코드들이 주 메모리에 올라와서 작업이 진행돼야 함 → 프로세스가 돼야 함
    - 프로세스가 생성되면, CPU는 필요한 작업을 처리한다.
        - CPU가 처리하는 작업의 단위가 바로 스레드

**멀티 프로세스**

- 프로세스를 fork해서 활용

### 스레드

- 스레드 : 프로세스 내에서 실행되는 여러 작업의 단위
- 스레드가 한 개로 동작하면 싱글 스레드, 여러 개의 스레드가 동작하면 멀티 스레딩
- 멀티 스레딩에선, 스레드 사이 **메모리 공유**와 **통신**이 가능
    - 자원의 낭비를 막고 효율성을 향상하기 위함
    - 한 스레드에 문제가 생기면 전체 프로세스에 영향이 간다는 특징
- 스레드의 종류
    - 사용자 수준 스레드
    - 커널 수준 스레드

---

### 동시성(Concurrency)

- 한 번에 여러 작업을 동시에 다루는 것(다른 시간에)을 의미

### 병렬성(Parallelism)

- 한 번에 여러 작업을 병렬적(같은 시간에)으로 다루는 것을 의미
    - 멀티 프로세스
    - 멀티 스레딩

### 멀티 스레딩

- 메모리 공유 → 문제가 생기면 다른 스레드에도 영향

### GIL(Global interpreter Lock) : 한 순간에 한 개의 스레드만 사용할 수 있도록

- 병렬 처리 불가!
- CPU Bound 코드의 경우 멀티 스레딩 사용 시 효과 X
    - I/O Bound의 경우, I/O wait 동안 다른 스레딩이 활성회 되기 때문에 효과 개선 가능

- [Python Global Interpreter Lock(GIL)이란?](https://seoyeonhwng.medium.com/python-global-interpreter-lock-gil-이란-2e519d4491a1)

### Python → GIL이 있으니 멀티 프로세싱을 활용!

- 멀티 프로세싱의 단점?
    - 메모리 공유가 없기 때문에, 프로세스 간 추가로 통신이 필요함

---

### requests : 동기 크롤링

- 10초 정도 소요

```python
import requests
import time

def fetcher(session, url):
    # url에 해당하는 데이터 반환
    with session.get(url) as response:
        return response.text

def main():#
    # Blocking 발생
    # 10초 정도 걸림
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
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
```

### aiohttp : 비동기 크롤링

- 1초 정도 소요
    - 속도 더 올리기 → aiodns, cchardet 설치하면 됨

  - 참고 : [aiohttp로 하는 비동기 HTTP 요청 - 이상한모임](https://blog.weirdx.io/post/52588)

```python
import aiohttp
import asyncio
import time

# 비동기 처리할 함수
async def fetcher(session, url):
    # url에 해당하는 데이터 반환
    # await return을 위해서 async 적어줌
    async with session.get(url) as response:
        # awaitable한 method
        return await response.text()

async def main():
    # 1 초 정도 걸림
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
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
```