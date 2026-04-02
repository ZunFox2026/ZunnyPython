# Import thư viện requests
import requests

# Gửi yêu cầu GET đến trang web
def gui_yeu_cau_get():
    # Đường dẫn URL của trang web
    url = "https://www.google.com"
    
    # Gửi yêu cầu GET
    response = requests.get(url)
    
    # In trạng thái yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung trang web
    print("Nội dung trang web:")
    print(response.text)

# Gửi yêu cầu POST đến trang web
def gui_yeu_cau_post():
    # Đường dẫn URL của trang web
    url = "https://httpbin.org/post"
    
    # Dữ liệu gửi đi
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    
    # Gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # In trạng thái yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung trang web
    print("Nội dung trang web:")
    print(response.text)

# Gửi yêu cầu GET với tham số
def gui_yeu_cau_get_voi_tham_so():
    # Đường dẫn URL của trang web
    url = "https://httpbin.org/get"
    
    # Tham số gửi đi
    params = {
        "key1": "value1",
        "key2": "value2"
    }
    
    # Gửi yêu cầu GET với tham số
    response = requests.get(url, params=params)
    
    # In trạng thái yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung trang web
    print("Nội dung trang web:")
    print(response.text)

# Gửi yêu cầu GET với header
def gui_yeu_cau_get_voi_header():
    # Đường dẫn URL của trang web
    url = "https://httpbin.org/get"
    
    # Header gửi đi
    headers = {
        "Accept": "application/json"
    }
    
    # Gửi yêu cầu GET với header
    response = requests.get(url, headers=headers)
    
    # In trạng thái yêu cầu
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In nội dung trang web
    print("Nội dung trang web:")
    print(response.text)

# Chạy các hàm
gui_yeu_cau_get()
gui_yeu_cau_post()
gui_yeu_cau_get_voi_tham_so()
gui_yeu_cau_get_voi_header()