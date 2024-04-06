# `requests` Common properties and methods of the library

When using the `requests` library to interact with the API, in addition to using `r.text` to obtain the response content, there are several common properties and methods that can help you better process the response data. The following are some commonly used properties and methods:

## Common properties

- **`r.status_code`**: Returns the status code of the HTTP request. Status code 200 means the request was successful, 404 means the resource was not found, 500 means a server error, etc.

- **`r.json()`**: When the response content is in JSON format, you can use this method to parse the content into a Python dictionary. This is a very common situation when handling REST API responses.

- **`r.headers`**: Return response headers in dictionary form. Can be used to obtain some information such as content type, server information, content length, etc.

- **`r.content`**: Returns the binary form of the response content. Suitable for downloading binary content such as files or images.

- **`r.url`**: Returns the URL from which the response was obtained, useful for tracking redirects.

- **`r.encoding`**: Get or set the encoding of the response content. If no encoding is specified in the header, `requests` will guess based on its own rules.

- **`r.cookies`**: Returns a `RequestsCookieJar` that contains all cookies sent by the server. Can be used to send these cookies on subsequent requests.

- **`r.raise_for_status()`**: This method will throw an exception if the response status code indicates an HTTP error. This is useful to ensure the request is successful.

- **`r.history`**: If the request has been redirected, `r.history` will contain a list of `Response` objects, representing each step in the redirection process.

- **`r.elapsed`**: Returns a `timedelta` object representing the time it took for the request to be sent and the response to be returned.

- **`r.request`**: Returns a `PreparedRequest` object, which represents the actual request sent. Can be used to debug or inspect the final form of the request, such as viewing the final URL, headers or body.

## Usage example

### Get JSON response content

```python
import requests

response = requests.get('https://api.github.com/events')
if response.status_code == 200:
     data = response.json()
     print(data)
else:
     print("Request failed, status code: ", response.status_code)
```

### Handling redirects

```python
response = requests.get('http://github.com')
print("Requested final URL:", response.url)
print("Redirect history:", response.history)
```

### Check response headers

```python
response = requests.get('https://api.github.com/events')
print("Response header information: ", response.headers)
```

These properties and methods make the requests library very flexible and powerful when handling HTTP requests. Through them, you can get almost all the information you need and process the response content in an appropriate way.
