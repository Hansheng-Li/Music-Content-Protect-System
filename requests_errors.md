# Requests library error demonstration and explanation

## 1. ConnectionError

This error is thrown when there is a problem with the network connection, such as DNS query failure, connection refused, etc.

### Sample code

```python
import requests
try:
     response = requests.get('http://example.commmmm') # Deliberately write the wrong domain name to trigger an error
except requests.ConnectionError:
     print('Connection error, please check whether your network connection or URL is correct.')
```

## 2. HTTPError

This error is thrown when an HTTP request returns an unsuccessful status code such as 404 (Page Not Found) or 500 (Internal Server Error).

### Sample code

```python
import requests
from requests.exceptions import HTTPError

response = requests.get('http://httpbin.org/status/404') # Access a URL that will return a 404 status code
try:
     response.raise_for_status() # This will throw an HTTPError because the status code is 404
except HTTPError:
     print(f'HTTP error, status code: {response.status_code}')
```

## 3. Timeout

This error is thrown when the request exceeds the set time limit. This can be divided into connection timeout and read timeout.

### Sample code

```python
import requests
from requests.exceptions import Timeout

try:
     response = requests.get('http://httpbin.org/delay/5', timeout=1) # Set the timeout to be less than the response time
except Timeout:
     print('The request timed out, please check the network or adjust the timeout setting.')
```

## 4. TooManyRedirects

This error is thrown when a request encounters too many redirects. Usually caused by website configuration issues.

### Sample code

```python
import requests
from requests.exceptions import TooManyRedirects

try:
     response = requests.get('http://httpbin.org/redirect/10', allow_redirects=True) # The number of request redirects exceeds the maximum limit
except TooManyRedirects:
     print('Too many redirects, please check the requested URL.')
```
