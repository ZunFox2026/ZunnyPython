# exercises.py - Bài tập thực hành Bài 25

# Bài 1: Viết hàm nhap_va_in_tong() yêu cầu người dùng nhập hai số
# và in ra tổng của chúng. Sử dụng try-except để xử lý lỗi nhập liệu.
# Nếu thành công, in "Tổng là: ...", nếu lỗi, in thông báo phù hợp.
def nhap_va_in_tong():
    # Gợi ý: Dùng try-except với ValueError
    pass


# Bài 2: Viết hàm doc_dong_dau_tien(ten_file) đọc và in ra dòng đầu tiên của file.
# Xử lý các lỗi: file không tồn tại, không có quyền truy cập, và lỗi chung.
# Dùng khối finally để in "Hoàn tất cố gắng đọc file."
def doc_dong_dau_tien(ten_file):
    # Gợi ý: Dùng try-except-finally, đọc file với with open
    pass


# Bài 3: Tạo lớp ngoại lệ tùy chỉnh TenKhongHopLeError.
# Viết hàm kiem_tra_ten(ho_ten) kiểm tra:
# - Nếu tên rỗng hoặc chỉ chứa khoảng trắng -> raise lỗi
# - Nếu tên dài quá 50 ký tự -> raise lỗi
# In thông báo thành công nếu hợp lệ.
class TenKhongHopLeError(Exception):
    # Gợi ý: kế thừa Exception, viết __init__ và __str__
    pass

def kiem_tra_ten(ho_ten):
    # Gợi ý: Dùng try-except để bắt lỗi tùy chỉnh
    pass
