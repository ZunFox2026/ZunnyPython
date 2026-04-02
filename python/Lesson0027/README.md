# Làm quen với thư viện requests
## Giới thiệu
Thư viện requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi các yêu cầu HTTP. Với thư viện này, bạn có thể dễ dàng gửi các yêu cầu GET, POST, PUT, DELETE, v.v. và nhận lại phản hồi từ máy chủ. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện requests và các phương thức cơ bản của nó.

## Lý thuyết
Thư viện requests cung cấp một cách đơn giản và trực quan để gửi các yêu cầu HTTP. Để sử dụng thư viện này, bạn cần import nó vào chương trình của mình bằng câu lệnh `import requests`. Sau đó, bạn có thể sử dụng các phương thức như `requests.get()`, `requests.post()`, `requests.put()`, `requests.delete()` để gửi các yêu cầu tương ứng.

Các phương thức này đều trả về một đối tượng Response, chứa thông tin về phản hồi từ máy chủ. Đối tượng Response có các thuộc tính như `status_code` (mã trạng thái), `text` (nội dung phản hồi), `json()` (nội dung phản hồi dạng JSON), v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện requests để gửi yêu cầu GET:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print("Mã trạng thái:", response.status_code)
print("Nội dung phản hồi:", response.text)
```
Khi chạy đoạn mã này, chương trình sẽ gửi yêu cầu GET đến địa chỉ `https://www.example.com` và in ra mã trạng thái cũng như nội dung phản hồi từ máy chủ.

## Bài tập
Để luyện tập kỹ năng sử dụng thư viện requests, bạn có thể thực hiện các bài tập sau:

* Gửi yêu cầu GET đến địa chỉ `https://jsonplaceholder.typicode.com/posts` và in ra nội dung phản hồi.
* Gửi yêu cầu POST đến địa chỉ `https://jsonplaceholder.typicode.com/posts` với dữ liệu `{ "title": "Bài viết mới", "body": "Nội dung bài viết" }` và in ra mã trạng thái cũng như nội dung phản hồi.
* Tìm hiểu về các phương thức khác của thư viện requests như `requests.put()`, `requests.delete()` và thực hiện các bài tập tương tự.

Hy vọng qua bài này, bạn đã có một cái nhìn tổng quan về thư viện requests và cách sử dụng nó trong Python. Hãy luyện tập và khám phá thêm về thư viện này để trở thành một lập trình viên Python giỏi!