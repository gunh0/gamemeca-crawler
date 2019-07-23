# Python Requests + BeautifulSoup

### Web Crawler

우리가 어떤 정보를 브라우저에서만 보는 것 뿐 아니라 그 정보들을 내가 이용하기 편한 방식(ex: json)으로 로컬에 저장하고 싶을 때가 있다.

HTTrack의 경우에는 웹을 그대로 자신의 컴퓨터로 복사를 해오지만, 내가 원하는 방식으로의 가공까지는 제공해주지 않는다.

Python을 이용하면 간단한 코드 몇줄 만으로도 쉽게 웹 사이트에서 원하는 정보만을 가져올 수 있다.



### Parsing? Parser?

파싱이란 어떤 데이터를 원하는 모양으로 만들어 내는걸 말한다.



**1. Parsing(파싱) :** 

1) 특정문서(XML 따위)를 읽어 들여서 이를 다른 프로그램이나 서브루틴이 사용할 수 있는 내부 의 표현 방식으로 변환시켜 주는 것이다. XML 문서를 보시면 HTML처럼 <>태그가 보일 것입니다. 사용자가 이렇게 입력하지만 컴터가 알아 볼 수 있도록 바꿔주는 과정을 의미한다.

2) 컴파일러의 일부로써 원시 프로그램의 명령문이나 온라인 명령문, HTML 문서등에서 마크업태그등을 입력으로 받아들여서 구문을 해석 할수 있는 단위로 여러부분으로 분할해 주는 역할을 한다.



**2. Parser(파서) :**

1) 파서는 파싱을 하는 프로세서를 파서라고 한다. 즉, 파서가 파싱 작업을 하는 것이다.

2) 파서(parser)란 컴파일러의 일부로서 원시 프로그램즉, 컴퍼일러나 인터프리터에서 원시 프로그램을 읽어 들여, 그문장의 구조를 알아내는 구문 분석(parsing)을 행하는 프로그램을 말한다.



### Requests

Python에는 requests라는 유명한 http request 라이브러리가 있다.



### BeautifulSoup

BeautifulSoup는 HTML과 XML 파일의 데이터를 가져오기 위한 파이썬 라이브러리이다.

Requests는 정말 좋은 라이브러리이지만, html을 ‘의미있는’, 즉 Python이 이해하는 객체 구조로 만들어주지는 못한다. 위에서 req.text는 python의 문자열(str)객체를 반환할 뿐이기 때문에 정보를 추출하기가 어렵다.

따라서 BeautifulSoup을 이용하게 된다. 이 BeautifulSoup은 html 코드를 Python이 이해하는 객체 구조로 변환하는 Parsing을 맡고 있고, 이 라이브러리를 이용해 우리는 제대로 된 ‘의미있는’ 정보를 추출해 낼 수 있다.



---



**https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642**

![image](https://user-images.githubusercontent.com/41619898/74377566-8200c100-4e27-11ea-9276-8b2520328a7b.png)

![image](https://user-images.githubusercontent.com/41619898/74377692-bf654e80-4e27-11ea-823d-b883ce93b39c.png)