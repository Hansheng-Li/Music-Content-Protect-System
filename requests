
# `requests` 库常用属性和方法

在使用 `requests` 库与API进行交互时，除了使用 `r.text` 获取响应内容外，还有几个常用的属性和方法可以帮助你更好地处理响应数据。以下是一些常用的属性和方法：

## 常用属性

- **`r.status_code`**: 返回HTTP请求的状态码。状态码200表示请求成功，404表示未找到资源，500表示服务器错误等。

- **`r.json()`**: 当响应内容是JSON格式时，可以使用此方法将内容解析为Python字典。这是处理REST API响应时非常常见的一种情况。

- **`r.headers`**: 以字典形式返回响应头。可以用来获取一些如内容类型、服务器信息、内容长度等信息。

- **`r.content`**: 返回响应内容的二进制形式。适用于下载文件或图片等二进制内容。

- **`r.url`**: 返回获取响应的URL，这对于跟踪重定向很有用。

- **`r.encoding`**: 获取或设置响应内容的编码。如果header中没有指定编码，`requests`将会根据自己的规则猜测。

- **`r.cookies`**: 返回一个`RequestsCookieJar`，它包含了服务器发送的所有cookies。可以用来在后续请求中发送这些cookies。

- **`r.raise_for_status()`**: 如果响应的状态码指示了一个HTTP错误，这个方法会抛出一个异常。这对于确保请求成功非常有用。

- **`r.history`**: 如果请求经过了重定向，`r.history`会包含`Response`对象的列表，代表了重定向过程中的每一步。

- **`r.elapsed`**: 返回一个`timedelta`对象，表示请求发送到响应返回所花费的时间。

- **`r.request`**: 返回一个`PreparedRequest`对象，表示的是实际发送的请求。可以用来调试或检查请求的最终形态，如查看最终的URL、headers或body。

## 使用示例

### 获取JSON响应内容

```python
import requests

response = requests.get('https://api.github.com/events')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("请求失败，状态码：", response.status_code)
```

### 处理重定向

```python
response = requests.get('http://github.com')
print("请求的最终URL：", response.url)
print("重定向历史：", response.history)
```

### 检查响应头

```python
response = requests.get('https://api.github.com/events')
print("响应头信息：", response.headers)
```

这些属性和方法让`requests`库在处理HTTP请求时非常灵活和强大。通过它们，你可以获取几乎所有你需要的信息，并以合适的方式处理响应内容。
