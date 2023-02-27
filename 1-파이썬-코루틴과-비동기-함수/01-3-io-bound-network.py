import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    # 네트워크에 의한 io-bound 발생
    for i in range(10):
        result = io_bound_func()
    print(result)
