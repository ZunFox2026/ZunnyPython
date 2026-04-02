# Bài 16: Làm quen với thư viện requests
# Thư viện requests được sử dụng để gửi các yêu cầu HTTP trong Python

# Import thư viện requests
import requests

# Gửi yêu cầu GET đến một trang web
def gui_yeu_cau_get():
    # Địa chỉ URL của trang web
    url = "https://www.google.com"
    
    # Gửi yêu cầu GET
    response = requests.get(url)
    
    # In trạng thái của yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung yêu cầu:", response.text)

# Gửi yêu cầu POST đến một trang web
def gui_yeu_cau_post():
    # Địa chỉ URL của trang web
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Dữ liệu được gửi trong yêu cầu
    data = {
        "title": "Bài tập",
        "body": "Nội dung bài tập",
        "userId": 1
    }
    
    # Gửi yêu cầu POST
    response = requests.post(url, json=data)
    
    # In trạng thái của yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung yêu cầu:", response.json())

# Chạy các hàm
gui_yeu_cau_get()
gui_yeu_cau_post()