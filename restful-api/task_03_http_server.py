#!/usr/bin/python3

import json
import http.server
from http.server import HTTPServer

host = "localhost"
port = 8000


class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested URL was not found on this server.")


server = HTTPServer((host, port), Server)

try:
    print(f"Server successfully started on http://{host}:{port}")
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped by user")
finally:
    server.server_close()
