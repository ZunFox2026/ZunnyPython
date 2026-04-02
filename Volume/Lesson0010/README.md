# Tìm hiểu về thư viện requests
## Giới thiệu
Thư viện requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi các yêu cầu HTTP và tương tác với các máy chủ web. Thư viện này cung cấp một cách đơn giản và dễ sử dụng để gửi các yêu cầu GET, POST, PUT, DELETE, v.v. và nhận phản hồi từ máy chủ. Trong bài học này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện requests để gửi các yêu cầu HTTP và xử lý phản hồi.

## Lý thuyết
Thư viện requests cung cấp các phương thức sau để gửi các yêu cầu HTTP:
- `requests.get()`: Gửi yêu cầu GET đến máy chủ.
- `requests.post()`: Gửi yêu cầu POST đến máy chủ.
- `requests.put()`: Gửi yêu cầu PUT đến máy chủ.
- `requests.delete()`: Gửi yêu cầu DELETE đến máy chủ.

Khi gửi yêu cầu, bạn có thể truyền các tham số như URL, dữ liệu, header, v.v. Thư viện requests cũng cung cấp các phương thức để xử lý phản hồi từ máy chủ, như `response.text`, `response.json()`, v.v.

## Ví dụ
Dưới đây là ví dụ về cách sử dụng thư viện requests để gửi yêu cầu GET đến trang web google.com:
```python
import requests

url = "https://www.google.com"
response = requests.get(url)

print(response.status_code)  # In mã trạng thái của phản hồi
print(response.text)  # In nội dung của phản hồi
```
Hoặc ví dụ về cách gửi yêu cầu POST đến máy chủ với dữ liệu:
```python
import requests

url = "https://example.com/api/create"
data = {"name": "John", "age": 30}
response = requests.post(url, json=data)

print(response.status_code)  # In mã trạng thái của phản hồi
print(response.json())  # In nội dung của phản hồi dưới dạng JSON
```
## Bài tập
Bài tập 1: Gửi yêu cầu GET đến trang web wikipedia.org và in nội dung của phản hồi.
Bài tập 2: Gửi yêu cầu POST đến máy chủ với dữ liệu {"name": "Alice", "age": 25} và in mã trạng thái của phản hồi.
Bài tập 3: Tìm hiểu về cách sử dụng các phương thức khác của thư viện requests, như `requests.put()`, `requests.delete()`, v.v. và thực hiện các bài tập tương ứng.