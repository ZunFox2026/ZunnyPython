# Bài tập 1: Viết hàm chia hai số với xử lý ngoại lệ
def chia_hai_so(a, b):
    try:
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
    except TypeError:
        print("Lỗi: Cả hai tham số phải là số.")


# Bài tập 2: Đọc danh sách tên từ file
def doc_danh_sach_tu_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            noi_dung = f.read().strip()
        
        if not noi_dung:
            raise ValueError("File rỗng")
        
        danh_sach = [ten.strip() for ten in noi_dung.split(",") if ten.strip()]
        
        if not danh_sach:
            raise ValueError("Không tìm thấy tên hợp lệ trong file")
        
        return danh_sach
    
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'")
        return []
    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")
        return []


# Bài tập 3: Kiểm tra mật khẩu với ngoại lệ tùy chỉnh
class MatKhauYeuError(Exception):
    """Ngoại lệ khi mật khẩu không đủ mạnh"""
    pass


def kiem_tra_mat_khau(password):
    if len(password) < 8:
        raise MatKhauYeuError("Mật khẩu phải có ít nhất 8 ký tự")
    
    if not any(c.isupper() for c in password):
        raise MatKhauYeuError("Mật khẩu phải có ít nhất 1 chữ in hoa")
    
    if not any(c.isdigit() for c in password):
        raise MatKhauYeuError("Mật khẩu phải có ít nhất 1 chữ số")
    
    print("Mật khẩu mạnh!")