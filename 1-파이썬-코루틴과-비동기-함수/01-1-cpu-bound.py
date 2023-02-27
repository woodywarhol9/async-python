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
