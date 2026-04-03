### Bài học 15: Xử lý ngoại lệ (Exception Handling)

# --- Ví dụ 1: Xử lý lỗi nhập số ---
print("=== Ví dụ 1: Nhập số nguyên an toàn ===")

while True:
    try:
        n = int(input("Nhập một số nguyên: "))
        print(f"Bạn đã nhập: {n}")
        break  # Thoát vòng lặp nếu nhập đúng
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")


# --- Ví dụ 2: Đọc file an toàn ---
print("\n=== Ví dụ 2: Đọc file an toàn ===")

filename = "data.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("Nội dung file:")
        print(content)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{filename}'!")
except PermissionError:
    print(f"Lỗi: Không có quyền đọc file '{filename}'!")
except Exception as e:
    print(f"Lỗi không mong muốn: {e}")
else:
    print("Đọc file thành công!")
finally:
    print("Hoàn tất thao tác đọc file.")


# --- Ví dụ 3: Tính trung bình với xử lý lỗi ---
print("\n=== Ví dụ 3: Tính trung bình danh sách ===")

def tinh_trung_binh(danh_sach):
    try:
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng, không thể tính trung bình.")
        tong = sum(danh_sach)
        trung_binh = tong / len(danh_sach)
        return trung_binh
    except TypeError:
        print("Lỗi: Danh sách chứa phần tử không phải số!")
        return None
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Thử với các trường hợp
print("Kết quả:")
print(f"[1, 2, 3, 4]: {tinh_trung_binh([1, 2, 3, 4])}")
print(f"[]: {tinh_trung_binh([])}")
print(f"[1, 'a', 3]: {tinh_trung_binh([1, 'a', 3])}")