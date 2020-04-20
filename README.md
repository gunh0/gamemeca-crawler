# Python `requests` + BeautifulSoup

### Web Crawler

Python allows us to easily retrieve specific information from a website with just a few lines of code. This is useful when we not only want to view information in a web browser but also want to store that information locally in a format that is convenient for us to use, such as JSON.

By utilizing web crawling techniques, we can programmatically navigate through web pages, extract the desired data, and save it for further processing or analysis. With Python's libraries like requests and BeautifulSoup, we can send HTTP requests to web servers, parse the HTML content of web pages, and extract the relevant information.

Web crawling offers great flexibility, enabling us to scrape data from multiple pages, follow links, handle pagination, and apply various filters to retrieve precisely the information we need. With a well-designed web crawler, we can automate the process of gathering data from the web, saving us time and effort.

<br/>

### Parsing? Parser?

Parsing refers to the process of transforming data into a desired format or structure.

**1. Parsing:**

Parsing involves taking a specific document (such as XML) and converting it into an internal representation that can be utilized by other programs or subroutines. For example, when you look at an XML document, you will notice tags enclosed in angle brackets (<>) similar to HTML. Parsing is the process of converting such input into a format that can be understood by a computer.

As part of a compiler, parsing plays a crucial role in reading source code, online commands, HTML documents, or similar inputs and dividing them into syntactically interpretable units. It analyzes the structure of the input and determines its components and relationships.

**2. Parser:**

A parser is the component responsible for carrying out the parsing process. It is a program or module that performs parsing tasks.

In the context of a compiler or interpreter, a parser reads the source code or raw program and performs syntax analysis (parsing). It examines the structure of the program's statements or commands, ensuring they adhere to the specified grammar or rules. The parser identifies the components of the input and constructs a representation (such as an abstract syntax tree) that can be further processed by the compiler or interpreter.

<br/>

### Requests

Python에는 requests라는 유명한 http request 라이브러리가 있다.

###### HTTP methods such as `GET` and `POST`, determine which action you’re trying to perform when making an HTTP request.

###### One of the most common HTTP methods is `GET`. The `GET` method indicates that you’re trying to get or retrieve data from a specified resource. To make a `GET` request, invoke `requests.get()`.

###### To test this out, you can make a `GET` request to GitHub’s Root REST API by calling `get()` with the following URL:

```python
>>> requests.get('https://api.github.com')
<Response [200]>
```

### BeautifulSoup

BeautifulSoup는 HTML과 XML 파일의 데이터를 가져오기 위한 파이썬 라이브러리이다.

Requests는 정말 좋은 라이브러리이지만, html을 ‘의미있는’, 즉 Python이 이해하는 객체 구조로 만들어주지는 못한다. 위에서 req.text는 python의 문자열(str)객체를 반환할 뿐이기 때문에 정보를 추출하기가 어렵다.

따라서 BeautifulSoup을 이용하게 된다. 이 BeautifulSoup은 html 코드를 Python이 이해하는 객체 구조로 변환하는 Parsing을 맡고 있고, 이 라이브러리를 이용해 우리는 제대로 된 ‘의미있는’ 정보를 추출해 낼 수 있다.

###### Beautiful Soup Documentation : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

---

**https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642**

![image](https://user-images.githubusercontent.com/41619898/74377566-8200c100-4e27-11ea-9276-8b2520328a7b.png)

![image](https://user-images.githubusercontent.com/41619898/74377692-bf654e80-4e27-11ea-823d-b883ce93b39c.png)
