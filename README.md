


# Building Python Web APIs with FastAPI

<a href="https://www.packtpub.com/product/building-python-web-apis-with-fastapi/9781801076630?utm_source=github&utm_medium=repository&utm_campaign=9781801076630"><img src="https://static.packt-cdn.com/products/9781801076630/cover/smaller" alt="Building Python Web APIs with FastAPI" height="256px" align="right"></a>

This is the code repository for [Building Python Web APIs with FastAPI](https://www.packtpub.com/product/building-python-web-apis-with-fastapi/9781801076630?utm_source=github&utm_medium=repository&utm_campaign=9781801076630), published by Packt.

**A fast-paced guide to building high-performance, robust web APIs with very little boilerplate code**

## What is this book about?
RESTful web services are commonly used to create APIs for web-based applications owing to their light weight and high scalability. This book will show you how FastAPI, a high-performance web framework for building RESTful APIs in Python, allows you to build robust web APIs that are simple and intuitive and makes it easy to build quickly with very little boilerplate code.

This book covers the following exciting features:
* Set up a FastAPI application that is fully functional and secure
* Understand how to handle errors from requests and send proper responses in FastAPI
* Integrate and connect your application to a SQL and NoSQL (MongoDB) database
* Perform CRUD operations using SQL and FastAPI
* Manage concurrency in FastAPI applications

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1801076634) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter05.

The code will look like the following:
```
from pydantic import BaseModel
from typing import List
class Event(BaseModel):
   id: int
   title: str
   image: str
   description: str
   tags: List[str]
   location: str  
```

**Following is what you need for this book:**

This book is for Python developers who want to learn FastAPI in a pragmatic way to create robust web APIs with ease. If you are a Django or Flask developer looking to try something new that's faster, more efficient, and produces fewer bugs, this FastAPI Python book is for you. The book assumes intermediate-level knowledge of Python programming.

With the following software and hardware list you can run all code files present in the book (Chapter 1-09).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-09     | Python 3.10                         | Windows, Mac OS X, and Linux       |
| 1-09     | Git 2.36.0                          | Windows, Mac OS X, and Linux       |



We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/qqhpc).


### Related products <Other books you may enjoy>
* Python Web Development with Sanic [[Packt]](https://www.packtpub.com/product/python-web-development-with-sanic/9781801814416?_ga=2.134911217.1837201707.1657723916-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801814416) [[Amazon]](https://www.amazon.com/dp/1801814414)

* Becoming an Enterprise Django Developer [[Packt]](https://www.packtpub.com/product/becoming-an-enterprise-django-developer/9781801073639?_ga=2.127463693.1837201707.1657723916-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801073639) [[Amazon]](https://www.amazon.com/dp/1801073635)

## Errata 
 * Page 14 (Code Snippet 1 line 1):  **FROM PYTHON:3.8** _should be_ **FROM python:3.8**
 * Page 15 (last line):  **FROM PYTHON:3.8** _should be_ **(venv)$ uvicorn api:app --port 8080 --reload**
 * Page 10,11,12 :  Page 10 should display the picture of page 11. Page 11 should display the picture of page 12. Page 12 should display the picture of page 10.
 
## Get to Know the Author
**Abdulazeez Abdulazeez Adeshina**
is a skilled Python developer, backend software engineer, and technical writer, with a wide range of technical skill sets in his arsenal. His background has led him to build command-line applications, backend applications in FastAPI, and algorithm-based treasure-hunting tools. He also enjoys teaching Python and solving mathematical-oriented problems through his blog. Abdulazeez is currently in his penultimate year of a water resources and environmental engineering program. His work experience as a guest technical author includes the likes of Auth0, LogRocket, Okteto, and TestDriven.




### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801076630">https://packt.link/free-ebook/9781801076630 </a> </p>
