
# Requests 库错误演示和解释

## 1. ConnectionError

当网络连接出现问题时，例如DNS查询失败，拒绝连接等，会抛出此错误。

### 示例代码

```python
import requests
try:
    response = requests.get('http://example.commmmm')  # 故意写错域名以触发错误
except requests.ConnectionError:
    print('连接错误，请检查你的网络连接或网址是否正确。')
```

## 2. HTTPError

当HTTP请求返回了不成功的状态码，例如404(页面未找到)或500(服务器内部错误)时，会抛出此错误。

### 示例代码

```python
import requests
from requests.exceptions import HTTPError

response = requests.get('http://httpbin.org/status/404')  # 访问一个会返回404状态码的网址
try:
    response.raise_for_status()  # 这会抛出HTTPError，因为状态码是404
except HTTPError:
    print(f'HTTP错误，状态码： {response.status_code}')
```

## 3. Timeout

当请求超出了设定的时间限制时，会抛出此错误。这可以分为连接超时和读取超时。

### 示例代码

```python
import requests
from requests.exceptions import Timeout

try:
    response = requests.get('http://httpbin.org/delay/5', timeout=1)  # 设置超时时间小于响应时间
except Timeout:
    print('请求超时，请检查网络或调整超时设置。')
```

## 4. TooManyRedirects

当请求遇到了过多的重定向时，会抛出此错误。通常是网站配置问题引起的。

### 示例代码

```python
import requests
from requests.exceptions import TooManyRedirects

try:
    response = requests.get('http://httpbin.org/redirect/10', allow_redirects=True)  # 请求重定向次数超过最大限制
except TooManyRedirects:
    print('过多重定向，请检查请求的URL。')
```
