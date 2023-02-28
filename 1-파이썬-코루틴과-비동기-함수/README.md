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