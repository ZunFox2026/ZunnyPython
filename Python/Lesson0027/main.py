# main.py
# Bài học 27: Xử lý ngoại lệ trong Python

# --- Ví dụ 1: Xử lý nhập số từ người dùng ---
print("=== Ví dụ 1: Nhập số an toàn ===")

def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập một số nguyên: "))
            return n
        except ValueError:
            print("Lỗi: Bạn phải nhập một số nguyên!")

# Gọi hàm
so = nhap_so_nguyen()
print(f"Bạn đã nhập số: {so}")

# --- Ví dụ 2: Đọc file an toàn ---
print("\n=== Ví dụ 2: Đọc file an toàn ===")

def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
        return None
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
        return None
    else:
        print("Đọc file thành công!")
        return noi_dung
    finally:
        print("Khối finally luôn được thực thi.")

# Gọi hàm (file 'data.txt' có thể không tồn tại)
noi_dung = doc_file_an_toan('data.txt')
if noi_dung:
    print("Nội dung file:", noi_dung)

# --- Ví dụ 3: Xử lý nhiều loại ngoại lệ ---
print("\n=== Ví dụ 3: Xử lý nhiều loại ngoại lệ ===")

danh_sach = [1, 2, 3]

try:
    chi_so = int(input("Nhập chỉ số muốn truy cập (0-2): "))
    print(f"Giá trị tại chỉ số {chi_so}: {danh_sach[chi_so]}")
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")
except IndexError:
    print("Lỗi: Chỉ số vượt quá danh sách!")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
else:
    print("Truy cập thành công!")
finally:
    print("Hoàn tất xử lý truy cập danh sách.")