# 비동기 도서 정보 수집기
- `FastAPI`와 `MongoDB`를 활용한 비동기 도서 정보 수집기
- `Naver Book API`를 활용해 해당 키워드에 대한 100 건의 도서 목록 수집

### Project Structure
---
``` bash
|-- README.md
|-- requirements.txt
|-- app
|   |-- main.py
|   |-- book_scraper.py
|   |-- config.py
|   |-- models
|   |   |-- __init__.py
|   |   |-- database.py
|   |   `-- book.py
|   `-- templates
|       `-- index.html
|-- server.py
`-- secrets.json
```

</br>

### 실행 화면

![image](https://github.com/woodywarhol9/woodywarhol9/assets/86637320/3cd39a63-99a8-405e-a930-efe25370e884)