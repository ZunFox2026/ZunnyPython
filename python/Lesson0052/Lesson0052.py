# Import thư viện requests để thực hiện các yêu cầu HTTP
import requests

# Thực hiện yêu cầu GET đến địa chỉ URL
def lay_noi_dung(url):
    # Gửi yêu cầu GET và lưu kết quả vào biến response
    response = requests.get(url)
    
    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Trả về nội dung của trang web
        return response.text
    else:
        # Trả về thông báo lỗi nếu yêu cầu không thành công
        return "Lỗi: " + str(response.status_code)

# Thực hiện yêu cầu POST để gửi dữ liệu đến server
def gui_du_lieu(url, du_lieu):
    # Gửi yêu cầu POST với dữ liệu và lưu kết quả vào biến response
    response = requests.post(url, data=du_lieu)
    
    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Trả về nội dung của trang web sau khi gửi dữ liệu
        return response.text
    else:
        # Trả về thông báo lỗi nếu yêu cầu không thành công
        return "Lỗi: " + str(response.status_code)

# Ví dụ sử dụng
url = "http://example.com"
print(lay_noi_dung(url))

du_lieu = {"ten": "Nguyễn Văn A", "tuoi": 25}
print(gui_du_lieu(url, du_lieu))