"""
Bài 24: Python Cơ bản
Tài liệu học tập về các khái niệm cơ bản trong Python
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị

# Số nguyên (int)
tuoi = 20
print(f"Tuổi: {tuoi}, Kiểu: {type(tuoi)}")

# Số thực (float)
chieu_cao = 1.75
print(f"Chiều cao: {chieu_cao}, Kiểu: {type(chieu_cao)}")

# Chuỗi (string)
ho_ten = "Nguyễn Văn A"
print(f"Họ tên: {ho_ten}, Kiểu: {type(ho_ten)}")

# Boolean (True/False)
la_sinh_vien = True
print(f"Là sinh viên: {la_sinh_vien}, Kiểu: {type(la_sinh_vien)}")


# 2. Cấu trúc điều kiện: if-elif-else
def danh_gia_tuoi(tuoi):
    """
    Hàm đánh giá độ tuổi theo nhóm
    """
    if tuoi < 13:
        return "Trẻ em"
    elif 13 <= tuoi < 18:
        return "Vị thành niên"
    elif 18 <= tuoi < 65:
        return "Người trưởng thành"
    else:
        return "Người cao tuổi"

# Ví dụ sử dụng
print(f"Đánh giá tuổi 10: {danh_gia_tuoi(10)}")
print(f"Đánh giá tuổi 25: {danh_gia_tuoi(25)}")


# 3. Vòng lặp cơ bản: for và while
# Ví dụ 1: Dùng for để in các số từ 1 đến 5
print("In số từ 1 đến 5:")
for i in range(1, 6):
    print(i, end=" ")
print()  # Xuống dòng

# Ví dụ 2: Dùng while để đếm ngược từ 5 về 1
print("Đếm ngược từ 5 về 1:")
dem = 5
while dem > 0:
    print(dem, end=" ")
    dem -= 1
print()


# 4. Danh sách (list) và thao tác cơ bản
# Tạo danh sách các môn học
mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
print(f"Danh sách môn học: {mon_hoc}")

# Thêm phần tử
mon_hoc.append("Văn")
print(f"Sau khi thêm Văn: {mon_hoc}")

# Truy cập phần tử
print(f"Môn học đầu tiên: {mon_hoc[0]}")

# Duyệt danh sách
print("Các môn học:")
for mon in mon_hoc:
    print(f" - {mon}")


# 5. Hàm (functions)
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    """
    return a + b

def tinh_diem_tb(diem_toan, diem_ly, diem_hoa):
    """
    Hàm tính điểm trung bình 3 môn
    """
    tong = tinh_tong(diem_toan, diem_ly)
    tong = tinh_tong(tong, diem_hoa)
    return tong / 3

# Sử dụng hàm
print(f"Tổng 3 + 5 = {tinh_tong(3, 5)}")
print(f"Điểm trung bình Toán 8, Lý 7, Hóa 9: {tinh_diem_tb(8, 7, 9):.2f}")


# 6. Bài tập nhỏ
def bai_tap_nho():
    """
    Bài tập: Viết chương trình yêu cầu người dùng nhập tên và điểm số,
    sau đó in ra xếp loại học lực.
    """
    print("\n=== BÀI TẬP NHỎ ===")
    print("Nhập thông tin học sinh:")

    # Nhập dữ liệu
    ten = input("Nhập tên: ")
    diem = float(input("Nhập điểm (0-10): "))

    # Xếp loại
    if diem >= 8.5:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    # In kết quả
    print(f"\nHọc sinh: {ten}")
    print(f"Điểm: {diem}")
    print(f"Xếp loại: {xep_loai}")

    # Gợi ý cải tiến: có thể mở rộng để nhập nhiều học sinh, tính trung bình lớp, v.v.


# 7. Hàm chính
def main():
    """
    Hàm chính để chạy chương trình
    """
    print("=" * 50)
    print("BÀI 24: PYTHON CƠ BẢN - TÀI LIỆU HỌC TẬP")
    print("=" * 50)

    # Chạy các ví dụ
    print("\n1. KIỂU DỮ LIỆU CƠ BẢN")
    # (đã in ở phần trên)

    print("\n2. CẤU TRÚC ĐIỀU KIỆN")
    # (đã in ở phần trên)

    print("\n3. VÒNG LẶP")
    # (đã in ở phần trên)

    print("\n4. DANH SÁCH")
    # (đã in ở phần trên)

    print("\n5. HÀM")
    # (đã in ở phần trên)

    # Chạy bài tập nhỏ
    bai_tap_nho()

    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản về Python!")


# 8. Chạy chương trình
if __name__ == "__main__":
    main()
```

---

**Mô tả nội dung:**
- Code khoảng 100 dòng, đầy đủ comment tiếng Việt.
- Bao gồm: biến, kiểu dữ liệu, điều kiện, vòng lặp, danh sách, hàm.
- 3 ví dụ minh họa rõ ràng.
- 1 bài tập nhỏ cho người học thực hành.
- Có `main()` và cấu trúc chuẩn Python.

**Cách dùng:**
- Lưu file với tên `bai_24_python_co_ban.py`
- Chạy bằng lệnh: `python bai_24_python_co_ban.py`