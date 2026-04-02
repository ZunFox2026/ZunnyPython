# Import thư viện requests
import requests

# Gửi yêu cầu GET đến một URL
def gui_yeu_cau_get(url):
    # Sử dụng phương thức get() của requests
    response = requests.get(url)
    
    # In ra trạng thái của yêu cầu
    print("Trạng thái:", response.status_code)
    
    # In ra nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu POST đến một URL
def gui_yeu_cau_post(url, data):
    # Sử dụng phương thức post() của requests
    response = requests.post(url, data=data)
    
    # In ra trạng thái của yêu cầu
    print("Trạng thái:", response.status_code)
    
    # In ra nội dung của yêu cầu
    print("Nội dung:", response.text)

# Ví dụ sử dụng
url = "https://www.google.com"
gui_yeu_cau_get(url)

# Ví dụ sử dụng với yêu cầu POST
url_post = "https://httpbin.org/post"
data = {"key": "value"}
gui_yeu_cau_post(url_post, data)