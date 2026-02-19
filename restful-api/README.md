<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# RESTful API

# [2. Consuming and processing data from an API using Python](task_02_requests.py)

## Background:
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The `requests` library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python's built-in libraries and tools enable effortless data manipulation and processing.

## Objective:
At the end of this exercise, students should be able to:
  1. Utilize the `requests` library to send HTTP requests and process responses.
  2. Parse and manipulate JSON data using Python.
  3. Convert structured data into other formats, e.g., CSV.

## Resources:
  1. [Python Requests Library](https://docs.python-requests.org/en/latest/)
  2. [Working with JSON data in Python](https://realpython.com/python-json/)
  3. Public API to experiment with: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Instructions:
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

# [3. Develop a simple API using Python with the `http.server` module](task_03_http_server.py)

## Background:
The `http.server` module in Python's standard library provides basic classes for implementing web servers. While it's not typically used for production applications, it's a handy tool for building simple web servers and understanding the basics of web programming without relying on third-party libraries.

## Objective:
At the end of this exercise, students should be able to:

  1. Set up a basic web server using the `http.server` module.
  2. Handle different types of HTTP requests (GET, POST, etc.).
  3. Serve JSON data in response to specific endpoints.

## Resources:
  1. [Python docs: http.server — HTTP servers](https://docs.python.org/3/library/http.server.html)
  2. [A simple example of using Python's http.server](https://www.afternerd.com/blog/python-http-server/)

## Instructions:
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
  
## Hints:

1. When sending headers using `http.server`, the `send_response` method is handy. You can also use `send_header` to specify specific headers, and don't forget to end headers with `end_headers`.

2. For serving JSON data, you'll want to convert a Python dictionary to a JSON string. The `json` module in Python's standard library will be beneficial.

3. When checking the path of the request, the `path` attribute of the request handler (`self.path`) can be used to route requests to different endpoints.

## Expected Output:

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


# [4. Develop a Simple API using Python with Flask](task_04_flask.py)

## Background:
Flask is a lightweight web framework for Python, which is especially popular for creating small to medium web applications and RESTful APIs. Its minimalist and modular approach makes it a great choice for beginners to delve into web development without the overhead of more complex frameworks.

## Objective:
At the end of this exercise, students should be able to:

  1. Set up a Flask application and run a development server.
  2. Define and handle routes with Flask to respond to different endpoints.
  3. Serve JSON data using Flask.
  4. Understand the basics of request handling and response formation in Flask.
  5. Handle POST requests to add new data to the API.

## Resources:
  * [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/) Start with the Quickstart section: "A Minimal Application" to get an overall idea on how the framework works.

## Instructions:
  1. **Setting Up Flask**:
      * Install Flask using pip: `pip install Flask`.
      * Create a new Python file and import Flask: `from flask import Flask`.
      * Instantiate a Flask web server from the Flask module: `app = Flask(__name__)`.

  2. **Creating Your First Endpoint**:
      * Define a route for the root URL ("/") and create a function (`def home():`) to handle this route. Within the function, return a string: "Welcome to the Flask API!".
      * Run the Flask development server with: `if __name__ == "__main__": app.run()`.
      * Visit `http://localhost:5000` in your browser or use `curl` to see the message.

  3. **Setting Up Flask**:
      * Import the `jsonify` function from Flask: `from flask import jsonify`.
      * Create a new route `/data` and associate a function with it. Inside this function, return a JSON response using `jsonify()`. This should return a list of all the usernames stored in the API.
      * Users will be stored in memory using a dictionary with `username` as the key and the whole object (dictionary) as the value.
      * Example dictionary: `users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}`
        * **NOTE: To avoid problem with the checker, do not include your testing data when pushing your code.**

  5. **Expanding Your API**:
      * Add a few more endpoints to simulate different functionalities:
      * `/status`: It should return `OK`.
      * `/users/<username>`: Returns the full object corresponding to the provided `username`. (Hint: Use Flask's dynamic route feature)
      * If the user does not exist, return a **404** with `{"error": "User not found"}`.

  6. **Handling POST Requests**:
      * Import the request object from Flask: `from flask import request`.
      * Create a new route `/add_user` that accepts POST requests.
      * This route should:

        1 Parse the incoming JSON data. Example data: `{"username": "john", "name": "John", "age": 30, "city": "New York"}`
        
        2 Add the new user to the users dictionary using `username` as the key.
        
        3 Return a confirmation message with the added user's data.
        
        4 If the request body is not valid JSON, return **400** with `{"error":"Invalid JSON"}`.
        
        5 If `username` is missing, return **400** with `{"error":"Username is required"}`.
        
        6 If `username` already exists, return **409** with `{"error":"Username already exists"}`.

## Test your code:
Test your application using the `flask` CLI to run the development server.

```bash
$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

> Use `curl` or a `python` script to test your API.

## Hints:
  1. Flask routes are defined using the `@app.route()` decorator, followed by a function that returns the desired response for that route.
  2. For serving dynamic content in routes, Flask allows you to add variables to the route (e.g., `<variable_name>`). These can be captured in your function parameters.
  3. The `jsonify()` function in Flask turns a Python dictionary or list into a response with `application/json` content-type.
  4. Flask's development server reloads automatically on code changes. However, for certain types of changes (like adding new files), you might need to restart the server.

## Expected Output:
  * Accessing `http://localhost:5000` should show the message: `"Welcome to the Flask API!"`.
  * Visiting `http://localhost:5000/data` should return a JSON response with a list of all usernames stored in the API. For example, if the `users` dictionary contains `{"jane": {"username": "jane", "name":     "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}`, the response should be:
  ```json
  ["jane", "john"]
  ```

  * The `/status` endpoint should return the string: `"OK"`.
  * Accessing `/users/jane` should return the full object corresponding to the username "jane". For example:
  ```json
  {
        "username": "jane", 
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
  }
  ```

  * Similarly, accessing `/users/john` should return:
  ```json
  {
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
  }
  ```

  * But if it doesn't exist, return a **404** with:
  ```json
  {"error": "User not found"}
  ```

  * Posting a new user to `/add_user` should add the user to the `users` dictionary and return a **201** status code with a confirmation message with the user's data. For example, posting:
  ```json
  {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
  }
  ```

  should return:
  ```json
  {
        "message": "User added",
        "user": {
                "username": "alice",
                "name": "Alice",
                "age": 25,
                "city": "San Francisco"
        }
  }
  ```

  * Posting a new user to `/add_user` without a `username` should return a **400** code error with the message:
  ```json
  {
        "error": "Username is required"
  }
  ```

  * Posting a new user to `/add_user` with a duplicate `username` (i.e., the username already exists) should return a **409** code error with the message:
  ```json
  {
        "error": "Username already exists"
  }
  ```

  * Posting a new user to `/add_user` with an invalid JSON body should return a **400** code error with the message:
  ```json
  {
        "error": "Invalid JSON"
  }
  ```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])

    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if user_data is None:
        return jsonify({"error":"Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error":"Username is required"}), 400

    if username in users:
        return jsonify({"error":"Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()
```
</details>

---


# [5. API Security and Authentication Techniques](task_05_basic_security.py)

## Background
API security is of paramount importance, especially when the API is exposed to the wider internet. There are many risks, including unauthorized data access, data tampering, and denial-of-service attacks. One fundamental method of securing APIs is to use authentication and authorization mechanisms, ensuring only authorized users can access certain resources.

## Objective
At the end of this exercise, students should be able to:

  1. Understand the importance of API security.
  2. Implement basic authentication using Flask.
  3. Set up token-based authentication with JSON Web Tokens (JWT).
  4. Differentiate between authentication and authorization.

## Resources:
  1. [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
  2. [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
  3. [Introduction to JSON Web Tokens](https://www.jwt.io/introduction#what-is-json-web-token)

## Instructions:
Basic Authentication:

  1. **Install Flask-HTTPAuth:**
  * Run: `pip install Flask-HTTPAuth`.

  1. **Set up Basic HTTP Authentication:**
  * Create a list of users and their hashed passwords.
  * Use the `werkzeug.security` library for password hashing and verification.

  1. **Protect Routes with Basic Authentication:**
  * Use the `@auth.login_required` decorator to protect certain routes.

Token-based Authentication with JWT:
  1. **Install Flask-JWT-Extended:**
  * Run: `pip install Flask-JWT-Extended`.

  1. **Set up JWT-based Authentication:**
  * Use a secret key for token generation and validation.
  * Create a route `/login` where users can log in with their credentials and receive a JWT token.

  1. **Protect Routes with JWT Tokens:**
  * Use the `@jwt_required()` decorator to protect certain routes.

  1. **Implement Role-based Access Control:**
  * Add roles (e.g., `admin`, `user`) to your users.
  * Create routes that should only be accessible to certain roles.
  * Implement checks to ensure the user's role matches the required role for accessing specific routes.

Hints:
  * For basic authentication, store passwords securely using `werkzeug.security.generate_password_hash` and verify them using `werkzeug.security.check_password_hash`.
  * Embed user information, such as roles, within the JWT token payload.
  * Use a strong secret key for JWT token generation and validation.
  * Utilize `get_jwt_identity()` to retrieve user information from the current JWT token.

## API Specifications:
User Data:
  * Users should be stored in memory using a dictionary with the following structure:
```python
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
```

Endpoints:
  1. Basic Authentication:
  * Protected Route:
    * URL: `/basic-protected`
    * Method: `GET`
    * Description: Returns a message `"Basic Auth: Access Granted"` if the user provides valid basic authentication credentials.
    * Authentication: Basic

  1. JWT Authentication:
  * **Login:**
    * URL: `/login`
    * Method: `POST`
    * Description: Accepts JSON payload with `username` and `password`. Returns a JWT token if credentials are valid.
    * Example Request:
    ```json
       {
         "username": "user1",
         "password": "password"
     }
    ```

    * Example Response:

    ```json
       {
       "access_token": "<JWT_TOKEN>"
     }
    ```
    
  * **JWT Protected Route:**
    * URL: `/jwt-protected`
    * Method: `GET`
    * Description: Returns a message `"JWT Auth: Access Granted"` if the user provides a valid JWT token.
    * Authentication: JWT
   
  * **Role-based Protected Route:**
    * URL: `/admin-only`
    * Method: `GET`
    * Description: Returns a message `"Admin Access: Granted"` if the user is an admin.
    * Authentication: JWT with role check

Expected Output:
  1. Accessing `/basic-protected` without credentials should return a `401 Unauthorized` response.
  2. Accessing `/basic-protected` with valid credentials should return `"Basic Auth: Access Granted"`.
  3. Posting valid credentials to `/login` should return a JWT token.
  4. Accessing `/jwt-protected` without a token or with an invalid token should return a `401 Unauthorized` response.
  5. Accessing `/jwt-protected` with a valid token should return `"JWT Auth: Access Granted"`.
  6. Accessing `/admin-only` with a non-admin token should return a `403 Forbidden` response `{"error": "Admin access required"}`.
  7. Accessing `/admin-only` with an admin token should return `"Admin Access: Granted"`.

## Important Note:
When implementing authentication in your Flask API, ensure that all authentication errors return a `401 Unauthorized response`. This includes errors due to missing, invalid, expired, or malformed tokens. Returning a consistent `401` status code for authentication errors is crucial for passing the automated tests. Failure to return a `401` status code for these errors may result in failing tests.

## Hints:
  * **Custom Error Handlers**: Use `Flask-JWT-Extended`'s decorators to create custom error handlers for different types of JWT errors.

Here are some examples:
  ```python
    from flask_jwt_extended import JWTManager

    app = Flask(__name__)
    jwt = JWTManager(app)
  
    @jwt.unauthorized_loader
    def handle_unauthorized_error(err):
        return jsonify({"error": "Missing or invalid token"}), 401
  
    @jwt.invalid_token_loader
    def handle_invalid_token_error(err):
        return jsonify({"error": "Invalid token"}), 401
  
    @jwt.expired_token_loader
    def handle_expired_token_error(err):
        return jsonify({"error": "Token has expired"}), 401
  
    @jwt.revoked_token_loader
    def handle_revoked_token_error(err):
        return jsonify({"error": "Token has been revoked"}), 401
  
    @jwt.needs_fresh_token_loader
    def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401
  ```
<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret_key'

auth = HTTPBasicAuth()

jwt = JWTManager(app)

users = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=["POST"])
def login():
    user_data = request.get_json()
    username = user_data.get("username")
    password = user_data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token})

    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted"

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 16/02/26 to 20/02/26 for Holberton School Bordeaux
