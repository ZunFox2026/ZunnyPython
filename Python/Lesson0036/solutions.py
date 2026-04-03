# Lời giải bài tập Python - Bài 36

# Bài 1: Viết hàm nhap_so_nguyen()
# Yêu cầu người dùng nhập một số nguyên.
# Nếu nhập sai, yêu cầu nhập lại đến khi đúng.
def nhap_so_nguyen():
    while True:
        try:
            so = int(input("Nhập một số nguyên: "))
            return so
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng số nguyên.")

# Bài 2: Viết hàm doc_danh_sach_tu_file(ten_file)
# Đọc file chứa các số, mỗi dòng một số.
# Bỏ qua các dòng lỗi.
def doc_danh_sach_tu_file(ten_file):
    danh_sach = []
    try:
        with open(ten_file, 'r', encoding='utf-8') as file:
            for dong in file:
                dong = dong.strip()  # Xóa khoảng trắng
                if dong == '':
                    continue
                try:
                    so = float(dong)  # Dùng float để hỗ trợ số thập phân
                    danh_sach.append(so)
                except ValueError:
                    print(f"Bỏ qua dòng không hợp lệ: '{dong}'")
    except FileNotFoundError:
        print(f"File '{ten_file}' không tồn tại. Trả về danh sách rỗng.")
    except PermissionError:
        print(f"Không có quyền đọc file '{ten_file}'.")
    finally:
        print("Hoàn thành việc đọc file.")
    return danh_sach

# Bài 3: Kiểm tra mật khẩu hợp lệ
# Yêu cầu: >=8 ký tự, có chữ hoa, chữ thường, số
def kiem_tra_mat_khau(mat_khau):
    if len(mat_khau) < 8:
        raise ValueError("Mật khẩu phải có ít nhất 8 ký tự.")
    
    co_chu_hoa = any(c.isupper() for c in mat_khau)
    co_chu_thuong = any(c.islower() for c in mat_khau)
    co_so = any(c.isdigit() for c in mat_khau)
    
    if not co_chu_hoa:
        raise ValueError("Mật khẩu phải có ít nhất một chữ cái in hoa.")
    if not co_chu_thuong:
        raise ValueError("Mật khẩu phải có ít nhất một chữ cái thường.")
    if not co_so:
        raise ValueError("Mật khẩu phải có ít nhất một chữ số.")
    
    return True

# Bài 4: Chia một số cho từng phần tử trong danh sách
def chia_list(a, b_list):
    ket_qua = []
    try:
        for b in b_list:
            try:
                ket_qua.append(a / b)
            except ZeroDivisionError:
                print(f"Cảnh báo: Không thể chia cho 0 (b={b}), bỏ qua.")
            except TypeError:
                print(f"Cảnh báo: Giá trị '{b}' không hợp lệ để chia, bỏ qua.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    finally:
        print("Hoàn thành quá trình chia danh sách.")
    return ket_qua
