### Static pages(정적 페이지)

---

![](https://user-images.githubusercontent.com/86637320/235352292-bb736237-79a5-42d9-84d6-26eea69d8bfa.png)
html, css, javascript 등으로 **미리 작성**된 **파일** 등을 서버에 저장해 놓고, 매 클라이언트 **요청**마다 **동일한 페이지**를 반환하는 경우다. 동적인 요소가 없기 때문에 별도의 DB 없이 `Web Server`(웹 서버)만으로 **처리**할 수 있는 영역이다.

미리 저장된 파일을 불러오기 때문에 **로딩** 자체가 **빠르**고, 공격적인 캐시 설정을 통해 이를 극대화할 수 있다는 장점이 있다. 다만 페이지 **내용 변경** 시 서버에 업로드해야 하는 과정이 필요한 만큼, 수정이 **불편**한 단점이 있다.

</br>

### Dynamic pages(동적 페이지)

---

![Untitled1](https://user-images.githubusercontent.com/86637320/235352333-e0344977-02a5-485c-9d63-d6bda24d6cd9.png)

클라이언트 요청에 따라 데이터를 **가공**해 맞춤형 결과를 반환하는 경우다. 동적 페이지를 위해선 Web Application Server(**WAS**)와 **DB**가 필요하며, 추가적인 서버 요청도 필요하다. 

사용자 별 맞춤 결과를 보여줄 수 있다는 것이 큰 장점이다. 당연하게도 로딩 속도가 느리고, 내용이 계속 변경되는 만큼 캐시 사용도 어렵다.

---

******참고******

[LINE에서 하루 만에 정적 웹 페이지 개발해서 배포하는 방법](https://engineering.linecorp.com/ko/blog/how-to-quickly-develop-static-pages-in-line)

[정적, 동적 웹페이지 차이는?](https://velog.io/@ppyooy336/정적-동적-웹페이지-차이는)