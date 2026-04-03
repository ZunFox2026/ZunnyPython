#############################
# Bài tập 1: Hàm chia hai số #
#############################
def chia_hai_so(a, b):
    try:
        # Chuyển đổi sang float để xử lý cả số thập phân
        ket_qua = float(a) / float(b)
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
        return None
    except (ValueError, TypeError):
        print("Lỗi: Vui lòng nhập hai số hợp lệ.")
        return None
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
        return None

# Kiểm thử
# print(chia_hai_so(10, 2))  # 5.0
# print(chia_hai_so(10, 0))  # Lỗi chia cho 0
# print(chia_hai_so('abc', 2))  # Lỗi kiểu

#############################################
# Bài tập 2: Đọc file số và tính tổng       #
#############################################
def tinh_tong_tu_file(file_path):
    tong = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for dong in f:
                dong = dong.strip()  # Xóa khoảng trắng đầu cuối
                if dong == '':
                    continue  # Bỏ qua dòng trống
                try:
                    so = float(dong)
                    tong += so
                except ValueError:
                    print(f"Bỏ qua dòng không hợp lệ: '{dong}'")
        return tong
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{file_path}'.")
        return None
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Kiểm thử: tạo file 'so.txt' với nội dung: 1\n2\nabc\n3.5\n\n4
# print(f"Tổng các số: {tinh_tong_tu_file('so.txt')}")

#############################################
# Bài tập 3: Hàm đăng nhập                  #
#############################################
def dang_nhap(username, password):
    try:
        if not username or username.strip() == '':
            raise ValueError("Tên đăng nhập không được để trống.")
        if len(password) < 6:
            raise ValueError("Mật khẩu phải có ít nhất 6 ký tự.")
        print(f"Đăng nhập thành công với tên: {username}")
    except ValueError as ve:
        print(f"Lỗi đăng nhập: {ve}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Kiểm thử
# dang_nhap("user1", "123456")     # Thành công
# dang_nhap("", "123456")           # Lỗi username
# dang_nhap("user", "123")           # Lỗi password

#############################################
# Bài tập 4: Nhập 5 số từ người dùng        #
#############################################
def nhap_nam_so():
    danh_sach = []
    while len(danh_sach) < 5:
        try:
            nhap = input(f"Nhập số thứ {len(danh_sach) + 1}: ")
            so = float(nhap)
            danh_sach.append(so)
            print(f"Đã thêm {so}")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
        except KeyboardInterrupt:
            print("\nNgười dùng đã hủy nhập.")
            break
        except Exception as e:
            print(f"Lỗi không mong muốn: {e}")
    return danh_sach

# Kiểm thử
# print("Danh sách số đã nhập:", nhap_nam_so())

#############################################
# Bài tập 5: Mở file và đọc dòng đầu tiên   #
#############################################
def mo_file_va_doc_dong_dau(file_path):
    dong_dau = None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            dong_dau = f.readline().strip()
            if dong_dau == '':
                print("File rỗng.")
            else:
                print(f"Dòng đầu tiên: {dong_dau}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{file_path}'.")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập file '{file_path}'.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    finally:
        print("--- Hoàn tất thao tác đọc file ---")
    return dong_dau

# Kiểm thử
# mo_file_va_doc_dong_dau('data.txt')