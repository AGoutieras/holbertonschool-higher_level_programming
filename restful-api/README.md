<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# RESTful API

## [2. Consuming and processing data from an API using Python](task_02_requests.py)

# Background:
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The `requests` library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python's built-in libraries and tools enable effortless data manipulation and processing.

# Objective:
At the end of this exercise, students should be able to:
  1. Utilize the `requests` library to send HTTP requests and process responses.
  2. Parse and manipulate JSON data using Python.
  3. Convert structured data into other formats, e.g., CSV.

# Resources:
  1. [Python Requests Library](https://docs.python-requests.org/en/latest/)
  2. [Working with JSON data in Python](https://realpython.com/python-json/)
  3. Public API to experiment with: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

# Instructions:
  1. If not installed, install the `requests` library using pip: `pip install requests`.

  2. Write a basic Python script to fetch posts from JSONPlaceholder using requests.get().

  * Create a function `fetch_and_print_posts()` that fetches all post from JSONPlaceholder.

    * Print the status code of the response i.e. `Status Code: 200`
    * If the request was sucessfull, parse the fetched data into a JSON object using the `.json()` method of the response object.
    * Iterate through the parsed JSON data and print out the titles of all the posts.

  * Create a function `fetch_and_save_posts()` that fetches all post from JSONPlaceholder.

    * If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for `id`, `title`, and `body`.
    * Using Python's `csv` module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        data = r.json()

        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        data = r.json()

        filtered_posts = []

        for post in data:
            post_data = {}
            post_data["id"] = post["id"]
            post_data["title"] = post["title"]
            post_data["body"] = post["body"]
            filtered_posts.append(post_data)

        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_posts)
```
</details>

---

## [3. Develop a simple API using Python with the `http.server` module](task_03_http_server.py)

# Background:
The `http.server` module in Python's standard library provides basic classes for implementing web servers. While it's not typically used for production applications, it's a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.

# Objective:
At the end of this exercise, students should be able to:

  1. Set up a basic web server using the `http.server` module.
  2. Handle different types of HTTP requests (GET, POST, etc.).
  3. Serve JSON data in response to specific endpoints.

# Resources:
  1. [Python docs: http.server — HTTP servers](https://docs.python.org/3/library/http.server.html)
  2. [A simple example of using Python's http.server](https://www.afternerd.com/blog/python-http-server/)

# Instructions:
1. **Setting Up a Basic HTTP Server:**

    * Use the `http.server` module to set up a simple HTTP server. Start by creating a subclass of `http.server.BaseHTTPRequestHandler`.
    * Implement the `do_GET` method to handle GET requests. Within this method, send a simple text response back to the client: "Hello, this is a simple API!".
    * Start the server on a specific port (8000) and test it by visiting `http://localhost:8000` in your browser or using `curl`.

2. **Serving JSON Data**

    * Modify the do_GET method in your server class to serve a sample JSON data when the endpoint /data is accessed.
    * You should return a simple dataset: {"name": "John", "age": 30, "city": "New York"}.
    * Ensure that the correct content type (application/json) header is set in the response.

3. **Handling Different Endpoints:**

    * Add an /status endpoint to check the API status. It shoud return OK.
    * Implement error handling. If the user tries to access an undefined endpoint, return a 404 Not Found status with an appropriate message.
  
# Hints:

1. When sending headers using `http.server`, the `send_response` method is handy. You can also use `send_header` to specify specific headers, and don't forget to end headers with `end_headers`.

2. For serving JSON data, you'll want to convert a Python dictionary to a JSON string. The `json` module in Python's standard library will be beneficial.

3. When checking the path of the request, the `path` attribute of the request handler (`self.path`) can be used to route requests to different endpoints.

# Expected Output:

1. On visiting `http://localhost:8000`, you should see the text: "Hello, this is a simple API!".

2. On accessing the endpoint `/data`, a JSON response with the sample dataset should be returned: `{"name": "John", "age": 30, "city": "New York"}`.

3. When visiting `/info`, you might see something like: `{"version": "1.0", "description": "A simple API built with http.server"}`.

4. Accessing any other undefined endpoint should return a `404 Not Found` status with a message like "Endpoint not found".

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Simple HTTP API"""
import json
import http.server
from http.server import HTTPServer


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler"""
    
    def do_GET(self):
        """Handles GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    PORT = 8000
    server_address = ('', PORT)
    server = HTTPServer(server_address, SimpleHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
```
</details>

---


## []()



<details>
<summary>Show answer</summary>

```python

```
</details>

---


## []()



<details>
<summary>Show answer</summary>

```python

```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 16/02/26 to 20/02/26 for Holberton School Bordeaux
