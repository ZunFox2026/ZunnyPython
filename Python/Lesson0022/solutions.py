# solutions.py - Lời giải Bài 22

import random

# Bài 1: Viết hàm chia_hai_so(a, b) trả về a/b. Xử lý lỗi.
def chia_hai_so(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except TypeError:
        print("Lỗi: Vui lòng nhập các giá trị số!")
        return None

# Bài 2: Đọc file số, tính trung bình
def tinh_trung_binh_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            tong = 0
            dem = 0
            for line in f:
                line = line.strip()
                if line:  # Bỏ qua dòng trống
                    so = float(line)
                    tong += so
                    dem += 1
            if dem == 0:
                print("File rỗng!")
                return None
            return tong / dem
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return None
    except ValueError:
        print("Dữ liệu trong file không hợp lệ (không phải số).")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Bài 3: Kiểm tra 3 cạnh tam giác
def kiem_tra_tam_giac(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a <= 0 or b <= 0 or c <= 0:
            print("Các cạnh phải lớn hơn 0.")
            return False
        # Kiểm tra bất đẳng thức tam giác
        if (a + b > c) and (a + c > b) and (b + c > a):
            print("Ba cạnh tạo thành một tam giác.")
            return True
        else:
            print("Ba cạnh không tạo thành tam giác.")
            return False
    except (ValueError, TypeError):
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return False

# Bài 4: Đọc danh sách tên từ file
def doc_danh_sach_tu_file(filename):
    try:
        danh_sach = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                ten = line.strip()
                if ten:  # Chỉ thêm nếu không rỗng
                    danh_sach.append(ten)
        return danh_sach
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return []
    except PermissionError:
        print(f"Không có quyền đọc file: {filename}")
        return []
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return []

# Bài 5: Đoán số từ 1 đến 100
def doan_so():
    so_bi_mat = random.randint(1, 100)
    print("Đoán số từ 1 đến 100!")
    while True:
        try:
            doan = int(input("Nhập số bạn đoán: "))
            if doan < 1 or doan > 100:
                print("Vui lòng nhập số từ 1 đến 100.")
            elif doan < so_bi_mat:
                print("Quá nhỏ!")
            elif doan > so_bi_mat:
                print("Quá lớn!")
            else:
                print("Chúc mừng! Bạn đã đoán đúng!")
                break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")