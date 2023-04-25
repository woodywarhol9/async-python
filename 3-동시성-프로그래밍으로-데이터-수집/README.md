### 웹 서버-클라이언트 사이 통신 과정

---

- `HTTP` 규칙에 따라 이뤄짐
1. 사용자(클라이언트)가 웹브라우저에 접속해 URL 입력
2. 사용자 입력한 URL 주소는 사실 **DNS 서비스**에 의해서 설정된 **별칭** → 원래 IP로 변환하여 요청할 서버 확인
3. **서버**에 데이터 **요청** 및 응답 **반환**
4. 서버로부터 받은 응답을 클라이언트에 반환

### POSTMAN?

---

- API 개발, 테스트, 공유 및 문서화하는데 활용되는 API 클라이언트

![image](https://user-images.githubusercontent.com/86637320/234279685-59713411-8d9f-4e01-a634-af255c2cde75.png)

> **Naver 뉴스 검색의 OPEN API**
> 
- Naver 뉴스에 cat을 검색 했을 때 결과 출력 기대 → But 실패

```python
https://openapi.naver.com/v1/search/news?query=cat
```

- `"Not Exist Client ID : Authentication failed. (인증에 실패했습니다.)”` 에러 발생
    - `HEADER`를 통해 Client 정보 추가로 전달해야 함
- 파라미터 → 요청 시 옵션 전달하는 역할
    - display `파라미터` 전달을 통해 검색 결과 개수 50개로 변경

```python
https://openapi.naver.com/v1/search/news?query=cat&display=50
```

### HEADERS 등에 활용되는 SECRET Key 관리하기

---

- `secrets.json` 과 같은 파일에 **정보**를 **저장**하고, 이를 불러오는 별도의 `config.py` 파일 구성하는 것이 좋음

### aiofiles를 활용한 비동기 파일 처리

---

- `aiohttp`을 활용한 비동기 크롤링으로 이미지 `src` 주소를 받아왔다고 가정
- 각 src를 활용해 이미지 저장할 때 `aiofiles`를 활용하면 비동기 파일 처리가 가능함

```python
async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)
```