# Import thư viện requests
import requests

# Định nghĩa URL của trang web muốn truy cập
url = "https://www.google.com"

# Gửi yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra trạng thái của yêu cầu
if response.status_code == 200:
    # Nếu yêu cầu thành công, in ra nội dung của trang web
    print("Nội dung của trang web:")
    print(response.text)
else:
    # Nếu yêu cầu thất bại, in ra thông báo lỗi
    print("Lỗi:", response.status_code)

# Định nghĩa URL của trang web muốn truy cập với tham số
url_params = "https://www.google.com/search"

# Định nghĩa tham số cho yêu cầu
params = {
    "q": "Python"  # Tìm kiếm với từ khóa "Python"
}

# Gửi yêu cầu GET đến URL với tham số
response_params = requests.get(url_params, params=params)

# Kiểm tra trạng thái của yêu cầu
if response_params.status_code == 200:
    # Nếu yêu cầu thành công, in ra nội dung của trang web
    print("Nội dung của trang web với tham số:")
    print(response_params.text)
else:
    # Nếu yêu cầu thất bại, in ra thông báo lỗi
    print("Lỗi:", response_params.status_code)

# Định nghĩa URL của API muốn truy cập
url_api = "https://jsonplaceholder.typicode.com/posts"

# Gửi yêu cầu GET đến API
response_api = requests.get(url_api)

# Kiểm tra trạng thái của yêu cầu
if response_api.status_code == 200:
    # Nếu yêu cầu thành công, in ra nội dung của API
    print("Nội dung của API:")
    print(response_api.json())
else:
    # Nếu yêu cầu thất bại, in ra thông báo lỗi
    print("Lỗi:", response_api.status_code)