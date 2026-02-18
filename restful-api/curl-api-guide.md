<a href="#"><img src="https://img.shields.io/badge/Curl-073551?style=for-the-badge&logo=curl&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Consuming Data from an API Using `curl`


### 1. Introduction to `curl`

`curl` (Client URL) is a command-line tool that allows you to transfer data to or froma server using various protocols (HTTP, HTTPS, FTP and more).
It is widely used to 
* Test REST APIs.
* Debug server issues
* Quickly prototype HTTP requests.


### 2. Installing and Veryfying `curl`

**Installation**
* **Linux / macOS:** usually pre-installed or via package managers:

```bash
sudo apt install curl  # Ubuntu/Debian
brew install curl  # macOS
```

* **Windows**: Install via WSL (Ubuntu) or download the Windows version from the official site.

**Verification**

```bash
curl --version
```

Example output:
```code
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.19
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
```


### 3. Fetching Data from an API

We will use the public JSONPlaceholder API: https://jsonplaceholder.typicode.com/

**Example: Get all posts**
```bash
curl https://jsonplaceholder.typicode.com/posts
```

* Output: a JSON array of posts with the following fields:
  * `userid`
  * `id`
  * `title`
  * `body`

For a more readable format (optional)
```bash
curl https://jsonplaceholder.typicode.com/posts | jq  # Install the jq tool first
```


### 4. Fetching Only Response Headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

* Output: only the **HTTP headers**, for example:
```code
HTTP/2 200 
date: Wed, 18 Feb 2026 16:23:03 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
...
```

* Useful for diagnosing server settings or checking content type.


### 5. Sending Data to the API (`POST`)

**Example: Create a new post**
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

* `-X POST`specifies the HTTP Method.
* `-d` sends the request data.
* Sample response (JSONPlaceholder simulates creation):

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```
* Note: JSONPlaceholder does **not actually save** the post; it only simulates the creation.


### 6. Other Useful Options

* Add a **custom header**

```bash
curl -H "Content-Type: application/json" https://jsonplaceholder.typicode.com/posts
```

* Save output to a file:

```bash
curl -o posts.json https://jsonplaceholder.typicode.com/posts
```

* Follow redirects automatically:

```bash
curl -L http://example.com
```


### 7. Conclusion

Using `curl`, you can:

* Quickly test APIs.
* Inspect responses and headers.
* Send data to a server.
* Automate API requests from the command line.

`curl` is a powerful tool for anyone working with web services.
