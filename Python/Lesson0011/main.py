# main.py - Các ví dụ minh họa về xử lý ngoại lệ trong Python

# ------------------- VÍ DỤ 1: Xử lý chia cho 0 -------------------
print("=== Ví dụ 1: Xử lý chia cho 0 ===")

def chia_hai_so(a, b):
    try:
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")

# Thử với các giá trị khác nhau
chia_hai_so(10, 2)
chia_hai_so(5, 0)

# ------------------- VÍ DỤ 2: Nhập liệu người dùng -------------------
print("\n=== Ví dụ 2: Nhập số từ người dùng ===")

def nhap_so_nguyen():
    while True:
        try:
            so = int(input("Nhập một số nguyên: "))
            print(f"Bạn đã nhập: {so}")
            break  # Thoát vòng lặp nếu nhập đúng
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

# Gọi hàm (bạn có thể bỏ comment để chạy)
# nhap_so_nguyen()

# ------------------- VÍ DỤ 3: Đọc file an toàn -------------------
print("\n=== Ví dụ 3: Đọc file với xử lý lỗi ===")

def doc_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Hoàn tất thao tác đọc file.")

# Gọi hàm (tạo trước file 'data.txt' để kiểm tra)
# doc_file("data.txt")
doc_file("khong_ton_tai.txt")