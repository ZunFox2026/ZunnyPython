### Bài tập thực hành - Xử lý ngoại lệ

# Bài 1: Nhập tuổi hợp lệ
def nhap_tuoi():
    # Viết hàm yêu cầu người dùng nhập tuổi (1-120)
    # Xử lý ValueError và kiểm tra phạm vi
    # Trả về tuổi nếu hợp lệ
    pass

# Bài 2: Đọc danh sách tên từ file
def doc_danh_sach_ten(ten_file):
    # Đọc từng dòng trong file, mỗi dòng là một tên
    # Xử lý FileNotFoundError, PermissionError
    # Nếu file rỗng hoặc không có tên hợp lệ, trả về danh sách rỗng
    # Trả về danh sách tên
    pass

# Bài 3: Tính trung bình các số
def tinh_trung_binh(danh_sach):
    # Tính trung bình các phần tử trong danh sách
    # Xử lý danh sách rỗng
    # Bắt lỗi nếu có phần tử không phải số (ValueError)
    # Trả về trung bình hoặc None nếu lỗi
    pass

# Bài 4: Kiểm tra email hợp lệ
class InvalidEmailError(Exception):
    # Tạo ngoại lệ tùy chỉnh cho email
    pass

def kiem_tra_email(email):
    # Kiểm tra email đơn giản: phải có @ và .
    # Nếu không hợp lệ, ném InvalidEmailError
    # Nếu hợp lệ, in "Email hợp lệ"
    pass

# Bài 5: Tính chỉ số BMI
def tinh_bmi(can_nang, chieu_cao):
    # Tính BMI = cân nặng / (chiều cao)^2
    # Xử lý các lỗi: kiểu dữ liệu, chia cho 0, giá trị âm
    # In kết quả và phân loại BMI
    pass