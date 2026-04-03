### Bài học 20: Xử lý lỗi và ngoại lệ

# Ví dụ 1: Đọc file an toàn
def doc_file_an_toan():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("Nội dung file:")
            print(content)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'data.txt'.")
    except PermissionError:
        print("Lỗi: Không có quyền đọc file.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Gọi hàm (bạn có thể tạo file data.txt để kiểm tra)
doc_file_an_toan()

# Ví dụ 2: Nhập tuổi an toàn
print("\n--- Nhập tuổi ---")
while True:
    try:
        tuoi = int(input("Nhập tuổi của bạn: "))
        if tuoi < 0:
            raise ValueError("Tuổi không thể là số âm.")
        print(f"Cảm ơn! Tuổi của bạn là {tuoi}.")
        break
    except ValueError as ve:
        # Nếu lỗi do không phải số hoặc do raise thì đều xử lý
        if "không phải số" in str(ve):
            print("Bạn phải nhập một số nguyên!")
        else:
            print(f"Lỗi: {ve}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

# Ví dụ 3: Tính trung bình cộng an toàn
def tinh_trung_binh(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("Đầu vào phải là danh sách hoặc bộ số.")
        if len(numbers) == 0:
            raise ZeroDivisionError("Danh sách rỗng, không thể tính trung bình.")
        
        tong = sum(numbers)
        avg = tong / len(numbers)
        return avg
    except ZeroDivisionError:
        print("Lỗi: Danh sách rỗng.")
        return None
    except TypeError as te:
        print(f"Lỗi kiểu dữ liệu: {te}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Kiểm thử hàm
danh_sach_1 = [10, 20, 30, 40]
danh_sach_2 = []
danh_sach_3 = [1, 2, "a", 4]

danh_sach_4 = "khong_phai_danh_sach"

print(f"\nTrung bình {danh_sach_1}: {tinh_trung_binh(danh_sach_1)}")
print(f"Trung bình {danh_sach_2}: {tinh_trung_binh(danh_sach_2)}")
print(f"Trung bình {danh_sach_3}: {tinh_trung_binh(danh_sach_3)}")
print(f"Trung bình {danh_sach_4}: {tinh_trung_binh(danh_sach_4)}")