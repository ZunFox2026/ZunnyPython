# Thư viện requests giúp chúng ta gửi yêu cầu HTTP đến một trang web
import requests

# Gửi yêu cầu GET đến một trang web
def gui_yeu_cau_get():
    # URL của trang web mà chúng ta muốn gửi yêu cầu đến
    url = "https://www.google.com"
    
    # Gửi yêu cầu GET
    response = requests.get(url)
    
    # In ra mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In ra nội dung của trang web
    print("Nội dung:", response.text)

# Gửi yêu cầu POST đến một trang web
def gui_yeu_cau_post():
    # URL của trang web mà chúng ta muốn gửi yêu cầu đến
    url = "https://httpbin.org/post"
    
    # Dữ liệu mà chúng ta muốn gửi đi
    data = {"key": "value"}
    
    # Gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # In ra mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In ra nội dung của trang web
    print("Nội dung:", response.text)

# Gửi yêu cầu GET với tham số
def gui_yeu_cau_get_voi_tham_so():
    # URL của trang web mà chúng ta muốn gửi yêu cầu đến
    url = "https://httpbin.org/get"
    
    # Tham số mà chúng ta muốn gửi đi
    params = {"key": "value"}
    
    # Gửi yêu cầu GET với tham số
    response = requests.get(url, params=params)
    
    # In ra mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In ra nội dung của trang web
    print("Nội dung:", response.text)

# Gửi yêu cầu với header
def gui_yeu_cau_voi_header():
    # URL của trang web mà chúng ta muốn gửi yêu cầu đến
    url = "https://httpbin.org/get"
    
    # Header mà chúng ta muốn gửi đi
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Gửi yêu cầu GET với header
    response = requests.get(url, headers=headers)
    
    # In ra mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In ra nội dung của trang web
    print("Nội dung:", response.text)

# Chạy các hàm
gui_yeu_cau_get()
gui_yeu_cau_post()
gui_yeu_cau_get_voi_tham_so()
gui_yeu_cau_voi_header()