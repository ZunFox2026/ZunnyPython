### Lời giải bài tập - Bài 15: Xử lý ngoại lệ

# Bài 1: Viết hàm chia hai số
# Hàm chia(a, b) trả về a/b, xử lý lỗi chia cho 0

def chia(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None

# Kiểm thử
print("Bài 1:")
print(chia(10, 2))  # 5.0
print(chia(10, 0))  # Lỗi chia cho 0


# Bài 2: Đọc số từ file
# Hàm đọc file chứa các số, mỗi dòng một số

def doc_so_tu_file(filename):
    danh_sach = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()  # Xóa khoảng trắng
                if dong:  # Nếu dòng không rỗng
                    so = float(dong)
                    danh_sach.append(so)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'!")
    except ValueError:
        print(f"Lỗi: Dữ liệu trong file không phải là số!")
    except Exception as e:
        print(f"Lỗi khác: {e}")
    return danh_sach

# Kiểm thử (giả sử file không tồn tại)
print("\nBài 2:")
print(doc_so_tu_file("so.txt"))


# Bài 3: Tìm phần tử lớn nhất trong danh sách

def tim_lon_nhat(danh_sach):
    try:
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng, không thể tìm phần tử lớn nhất.")
        return max(danh_sach)
    except TypeError:
        print("Lỗi: Danh sách chứa phần tử không so sánh được!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

print("\nBài 3:")
print(tim_lon_nhat([5, 3, 9, 1]))  # 9
print(tim_lon_nhat([]))             # Lỗi rỗng
print(tim_lon_nhat([1, 2, 'a']))   # Lỗi kiểu


# Bài 4: Chuyển chuỗi thành số thực

def chuyen_chuoi_thanh_so(chuoi):
    try:
        return float(chuoi)
    except ValueError:
        print(f"Lỗi: '{chuoi}' không phải là số hợp lệ!")
        return None
    except TypeError:
        print(f"Lỗi: Đầu vào không phải là chuỗi!")
        return None

print("\nBài 4:")
print(chuyen_chuoi_thanh_so("12.5"))  # 12.5
print(chuyen_chuoi_thanh_so("abc"))   # Lỗi
print(chuyen_chuoi_thanh_so(123))      # Lỗi kiểu


# Bài 5: Mở file và in từng dòng, đảm bảo đóng file

def in_dong_file(filename):
    file = None
    try:
        file = open(filename, "r", encoding="utf-8")
        for dong in file:
            print(dong.strip())
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    finally:
        if file:  # Nếu file đã được mở
            file.close()
            print("File đã được đóng.")

# Kiểm thử
print("\nBài 5:")
in_dong_file("test.txt")