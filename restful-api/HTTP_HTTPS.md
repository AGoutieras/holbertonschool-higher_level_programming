<a href="#"><img src="https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=Wireshark&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Differences between HTTP and HTTPS

# Table of contents
* [HTTP (HyperText Transfer Protocol)](#http-hypertext-transfer-protocol)
* [HTTPS (HyperText Transfer Protocol Secure](#https-hypertext-transfer-protocol-secure)
* [Structure of an HTTP Request and Response](#structure-of-an-http-request-and-response)
* [Observing Traffic with Wireshark](#observing-traffic-with-wireshark)
* [Common HTTP Methods](#common-http-methods)
* [Common HTTP Status Codes](#common-http-status-codes)


### HTTP (HyperText Transfer Protocol)

HTTP is the Protocol used to transfer data between a web browser and a web server.

**Characteristics:**

* ❌ Data is not encrypted
* ❌ Vulnerable to eavesdropping (Man-in-the-Middle attacks)
* ❌ Passwords, forms, and sensitive data can be intercepted
* ✅ Slightly faster (no encryption overhead)

![HTTP Diagram](https://study-ccna.com/wp-content/images/http_process_explained.jpg)


### HTTPS (HyperText Transfer Protocol Secure

HTTPS is the secure version of HTTP.

It uses SSL/TLS encryption to protect communication between the client and the server.

**Characteristics:**

* ✅ Data is encrypted
* ✅ Protects against interception
* ✅ Authenticates the server using SSL/TLS certificates
* 🔒 Essential for banking, e-commerce, email services and login systems

![HTTPS Diagram](https://i.ibb.co/GQQgYTvH/Sans-titre.png)


### Comparison Summary

| Feature        | HTTP           | HTTPS                         |
|----------------|----------------|-------------------------------|
| Encryption     | ❌ No          | ✅ Yes (TLS/SSL)             |
| Security Level | Low            | High                          |
| Default Port   | 80             | 443                           |
| Typical Usage  | Basic websites | Secure and sensitive websites |

# Structure of an HTTP Request and Response

When you open your browser's **Developer Tools -> Network tab**, you can observe the structure of HTTP communication.

```bash
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Main Components:**

* **Method** -> `GET`
* **PATH** -> `/index.html`
* **HTTP Version** -> `HTTP/1.1`
* **Headers** -> Additional metadata (browser info, accepted formats, etc.)
* **Body (optional)** -> Data sent to the server (e.g., from data in `POST` requests)

### HTTP Response Structure

Exemple:
```bash
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>
  ...
</html>
```

**Components:**

* **Status Line**
* **Status Code**
* **Headers**
* **Body (Content returned)**


# Observing Traffic with Wireshark

If you use Wireshark:
* HTTP traffic appears readable
* HTTPS traffic appears encrypted


### HTTP Traffic in Wireshark
![Wireshark HTTP Capture](https://i.ibb.co/prL4Xx98/Capture-d-cran-2026-02-18-130846.png)

You should clearly see:

* `GET / HTTP/1.1` request line
* Headers such as `Host`, `User-Agent`, `Accept` and `Referer`
* The full request URI (`http://httpforever.com/`)
* Plain-text content that is fully readable

### HTTPS Traffic in Wireshark
![Wireshark HTTPS Capture](https://i.ibb.co/zTsbB9TB/Capture-d-cran-2026-02-18-132458.png)

You should clearly see:

* `TLS` handshake packets (Client Hello/Server Hello)
* `Encrypted Application Data` (cannot be read)
* No readable `GET` request or headers
* Hexadecimal content representing encrypted HTTP traffic

  
# Common HTTP Methods

### `GET`
* **Description:** Retrieves data
* **Use Case:** Loading a webpage

### `POST`
* **Description:** Sends data to server
* **Use Case:** Submitting a form

### `PUT`
* **Description:** Replaces an existing resource
* **Use Case:** Editing a profile

### `DELETE`
* **Description:** Deletes a resource
* **Use Case:** Removing a record

![HTTP Methods](https://i.ibb.co/ksCVWnF6/Sans-titre2.png)


# Common HTTP Status Codes

Status codes are grouped by category:

* **1xx** -> Informational
* **2xx** -> Success
* **3xx** -> Redirection
* **4xx** -> Client Error
* **5xx** -> Server Error

### `200` – OK
Request successful.

### `301` – Moves Permanently
Permanent redirection.

### `400` – Bad Request
Invalid client request.

### `404` – Not Found
Resource does not exist.

### `500` – Internal Server Error
Server-side issue.

![HTTP Status Code Groups](https://miro.medium.com/v2/resize:fit:720/format:webp/1*w_iicbG7L3xEQTArjHUS6g.jpeg)

# ✅ Conclusion
Understanding HTTP and HTTPS is fundamental for:

* Web developement
* Cybersecurity
* Network analysis
* API developement
