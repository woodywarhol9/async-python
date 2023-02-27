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
