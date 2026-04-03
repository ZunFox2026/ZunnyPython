# main.py - Bài học 12: Xử lý ngoại lệ trong Python

# --- Ví dụ 1: Xử lý người dùng nhập sai kiểu dữ liệu ---
print("=== Ví dụ 1: Nhập số nguyên an toàn ===")

def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập một số nguyên: "))
            return n
        except ValueError:
            print("Lỗi: Bạn phải nhập một số nguyên!")

# Gọi hàm (chỉ chạy khi không comment)
# so = nhap_so_nguyen()
# print(f"Bạn đã nhập: {so}")


# --- Ví dụ 2: Đọc file an toàn ---
print("\n=== Ví dụ 2: Đọc file an toàn ===")

def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Đọc file thành công:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: File '{ten_file}' không tồn tại!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Thử đọc một file (chỉ chạy nếu file tồn tại)
# doc_file_an_toan("file_khong_ton_tai.txt")


# --- Ví dụ 3: Xử lý nhiều loại lỗi cùng lúc ---
print("\n=== Ví dụ 3: Tính chia hai số với xử lý lỗi ===")

def chia_hai_so():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        ket_qua = a / b
    except ValueError:
        print("Lỗi: Bạn phải nhập một số!")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        # Chạy nếu không có lỗi
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    finally:
        # Luôn chạy
        print("Cảm ơn bạn đã sử dụng chương trình chia số!")

# Gọi hàm (chỉ chạy khi không comment)
# chia_hai_so()


# --- Ví dụ 4: Dùng finally để dọn dẹp tài nguyên ---
print("\n=== Ví dụ 4: Sử dụng finally để đóng tài nguyên ===")

tep = None
try:
    tep = open("du_lieu.txt", "w", encoding="utf-8")
    tep.write("Dữ liệu quan trọng\n")
    # Giả sử có lỗi xảy ra ở đây
    ket_qua = 10 / 0
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
finally:
    if tep:  # Nếu file đã được mở
        tep.close()
        print("File đã được đóng an toàn.")
