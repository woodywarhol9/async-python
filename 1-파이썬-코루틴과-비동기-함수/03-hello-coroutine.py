# 일반적인 서브 루틴
"""
def hello_world():
    print("hello world")
    
 
if __name__ == "__main__":
    print(hello_world())
"""
# 코루틴으로 변경
# runtime error : 코루틴 함수가 awaited 되지 않았음
"""
async def hello_world():
    print("hello world")
    
 
if __name__ == "__main__":
    print(hello_world())
"""
# await 처리
# SyntaxError : await가 함수 밖에서 실행됨
"""
async def hello_world():
    print("hello world")
    
 
if __name__ == "__main__":
    await hello_world()
"""
# asyncio를 통해 코루틴을 파이썬에서 실행할 수 있게 됨
"""
import asyncio

async def hello_world():
    print("hello world")
    return 123
    
 
if __name__ == "__main__":
    asyncio.run(hello_world())
"""
# await을 아무 곳에나 추가해도 되는지?
# Nonetype 객체는 await 표현을 사용하면 안됨
# awaitable 객체에만 사용할 수 있음


async def hello_world():
    await print("hello world")
    return 123


if __name__ == "__main__":
    asyncio.run(hello_world())
