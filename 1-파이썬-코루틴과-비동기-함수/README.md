### Bound(바운드)

> CPU 바운드
> 
- 프로그램의 실행 속도가 CPU 속도에 의해 제한되는 현상
- 복잡한 수학적인 연산을 할 경우 발생

```python
# 연산량이 커지면, 프로그램 실행 속도가 영향
# CPU - 바운드
def cpu_bound_func(number: int):
    total = 1
    arange = range(1, number + 1)
    for i in arange:
        for j in arange:
            for k in arange:
                total += i * j * k

    return total

if __name__ == "__main__":
    result = cpu_bound_func(200)
    print(result)
```

> I/O 바운드
> 
- I(input), O(ouput)에 의해 프로그램 실행 속도가 제한되는 경우
- 사람의 입, 출력에 의해서 발생할 수 있음

```python
# i : input, o : ouput
# 입-출력에 의해 프로그램 실행 속도가 제한되는 경우
def io_bound_func():
    print("값을 입력해주세요.")
    input_value = input()
    return int(input_value) + 100

if __name__ == "__main__":
    result = io_bound_func()
    print(result)
```

- 서버 사이 네트워크 통신에 의해서도 발생 가능
    - 웹 브라우저의 개발자 모드로 확인 가능

![Untitled](https://user-images.githubusercontent.com/86637320/221741874-e84c7da2-86f6-4b08-94d6-064e58c5fd6d.png)

```python
import requests

def io_bound_func():
    result = requests.get("https://google.com")
    return result

if __name__ == "__main__":
    # 네트워크에 의한 io-bound 발생
    for i in range(10):
        result = io_bound_func()
    print(result)
```

### Blocking(블로킹)

- 바운드에 의해서 코드가 멈추게 되는 현상이 발생하는 것
- 바운드에 의해 코드가 멈추지 않는 경우 → **Non-Blocking**
---

### ************************동기 - 비동기************************

- 프로세스의 실행 순서와 관련된 개념

### ********************************블록 - 논블록********************************

- 프로세스의 유휴 상태(wait)와 관련된 개념

### 동기(synchronous)

코드가 반드시 작성된 순서대로 실행된다.

```python
# 동기 방식 : 배달 -> 식사 끝날때 까지 기다렸다가 그릇 수거
# 비효율적!
import time

def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    # 식사 완료까지 대기
    time.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")

def main():
    delivery("A", 3)
    delivery("B", 3)
    delivery("C", 4)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```

### 비동기(asynchronous)

코드가 반드시 작성된 순서대로 실행되지는 않는다.

항상 도움이 되는 것은 아니고 → 입 - 출력 처리가 많을 경우 중요!

```python
import time
# 비동기 처리를 위한 라이브러리
import asyncio
# 비동기 처리할 함수
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")
    
async def main():
    await asyncio.gather(
        delivery("A", 3),
        delivery("B", 3),
        delivery("C", 4),
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
```

---

참고할 링크

[동기(Synchronous)는 정확히 무엇을 의미하는걸까?](https://evan-moon.github.io/2019/09/19/sync-async-blocking-non-blocking/)

[Block, Non-Block, Sync, Async](https://velog.io/@markyang92/Block-Non-Block-Sync-Async)

[[python] for / while / generator / yield / coroutine / futures / asyncio](https://velog.io/@markyang92/python-for-while#이터레이터-제어)

[블럭,논블럭,동기,비동기 이야기](http://hamait.tistory.com/930)

---
### 코루틴 관련 용어 정리

- Routine(루틴) : 일련의 명령(흐름)
    - Main-Routine(메인 루틴) : 프로그램 메인 코드의 흐름
- Sub-Routine(서브 루틴) : 일반적인 함수나 메소드(메인 루틴을 보조하는 역할)
    - 프로그램이 실행되면 서브 루틴은 별도의 공간(스코프)에 해당 로직들을 저장하고 대기
    - 서브 루틴이 호출되면, 해당 스코프로 이동했다가, return을 통해 원래 호출 시점(메인 루틴)으로 복귀함
    
    → 하나의 진입점과 하나의 탈출점이 있는 루틴임
    
    - `return` 이 명시되지 않은 함수더라도, return None이 되기 때문에 탈출점은 항상 있음

### Coroutine(코루틴)

- 서브 루틴의 일반화된 형태
    - 일반화 → ‘진입점과 탈출점이 여러 개’

```python
import time
# 비동기 처리를 위한 라이브러리
import asyncio
# coroutine : 진입점과 탈출점이 여러 개 존재하는 루틴
# 추가로 await가 진입 - 탈출점 역할을 함
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")
    
async def main():
    await asyncio.gather(
        delivery("A", 1),
        delivery("B", 1),
        delivery("C", 1),
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

>>
A에게 배달 완료! # await asyncio.sleep(mealtime)을 통해서 탈출
B에게 배달 완료!
C에게 배달 완료!
A 식사 완료, 1 시간 소요... # await asyncio.sleep(mealtime)을 통해서 진입
A 그릇 수거 완료
B 식사 완료, 1 시간 소요...
B 그릇 수거 완료
C 식사 완료, 1 시간 소요...
C 그릇 수거 완료
1.0226211547851562
```

- await?
    - awaitable한 객체에서 사용 가능
    - awaitable 객체
        - `코루틴`, `태스크`, `퓨쳐`
- 태스크 객체
    - 미리 예약해뒀다가, await 를 만나면 실행 됨

```python
# 태스크 객체 활용
task1 = asyncio.create_task(delevery("A", 2))
task2 = asyncio.create_task(delevery("B", 1))

await task1
await task2

# 코루틴 객체 그대로 활용
await delivery("A", 2)
```

- 퓨처 객체
    - 멀티 스레딩, 멀티 프로세싱 때 활용

### 명령어 알아보기

- `asyncio.run()` : 실행
- `asyncio.gather()` : 동시에 실행하기
    - concurrency하게 실행 됨
    - return도 가능 → List 각 성분에 맞도록 return 됨

```python
await asyncio.gather(
    delivery("A", 3),
    delivery("B", 3),
    delivery("C", 4),)

result = await asyncio.gather(
    delivery("A", 3),
    delivery("B", 3),
    delivery("C", 4),)
print(result)
```

- `asyncio.sleep()`

---

참고할 링크

[Python 비동기 프로그래밍 제대로 이해하기(1/2) - Asyncio, Coroutine](https://blog.humminglab.io/posts/python-coroutine-programming-1/#yield-from)

[Coroutine, Thread 와의 차이와 그 특징](https://aaronryu.github.io/2019/05/27/coroutine-and-thread/)

[코틀린 코루틴(coroutine) 개념 익히기 · 쾌락코딩](https://wooooooak.github.io/kotlin/2019/08/25/코틀린-코루틴-개념-익히기/)

[[Python 입문] yield에 대해 알아보자](https://blog.naver.com/PostView.naver?blogId=shino1025&logNo=222164930611&categoryNo=14&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=10&userTopListManageOpen=false&userTopListCurrentPage=1)