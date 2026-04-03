"""
Bài 52: Tổng Hợp Kiến Thức Python Cơ Bản
Tác giả: [Tên bạn]
Mô tả: File Python tổng hợp các kiến thức cơ bản về biến, kiểu dữ liệu, cấu trúc điều khiển,
vòng lặp, hàm, danh sách, từ điển và xử lý lỗi.
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python có các kiểu dữ liệu phổ biến: int, float, str, bool
ten = "Python"          # chuỗi (str)
tuoi = 25               # số nguyên (int)
chieu_cao = 1.75        # số thực (float)
la_sinh_vien = True     # boolean (bool)

# In thông tin ra màn hình
print("=== Thông tin cá nhân ===")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Cấu trúc điều khiển: if-elif-else
print("\n=== Kiểm tra độ tuổi ===")
if tuoi < 18:
    print("Bạn là vị thành niên.")
elif 18 <= tuoi < 65:
    print("Bạn là người trưởng thành.")
else:
    print("Bạn là người cao tuổi.")

# 3. Vòng lặp: for và while
print("\n=== In dãy số từ 1 đến 5 ===")
for i in range(1, 6):
    print(i, end=" ")
print()  # xuống dòng

# Ví dụ while: đếm ngược
print("\n=== Đếm ngược từ 3 về 1 ===")
dem = 3
while dem > 0:
    print(dem)
    dem -= 1
print("Hết!")

# 4. Danh sách (list) và các thao tác
danh_sach_mon_hoc = ["Toán", "Lý", "Hóa"]
print(f"\nDanh sách môn học: {danh_sach_mon_hoc}")

# Thêm phần tử
danh_sach_mon_hoc.append("Sinh")
print(f"Sau khi thêm 'Sinh': {danh_sach_mon_hoc}")

# Duyệt danh sách
print("Các môn học:")
for mon in danh_sach_mon_hoc:
    print(f" - {mon}")

# 5. Từ điển (dictionary)
thong_tin_hoc_sinh = {
    "ten": "An",
    "lop": "10A1",
    "diem_tb": 8.5
}
print(f"\nThông tin học sinh: {thong_tin_hoc_sinh}")
print(f"Học sinh {thong_tin_hoc_sinh['ten']} học lớp {thong_tin_hoc_sinh['lop']}")

# 6. Hàm (function)
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    :param a: số thứ nhất
    :param b: số thứ hai
    :return: tổng của a và b
    """
    return a + b

def chao_tan_su(ten, loi_chao="Xin chào"):
    """
    Hàm chào hỏi
    """
    print(f"{loi_chao}, {ten}!")

# Gọi hàm
print("\n=== Sử dụng hàm ===")
ket_qua = tinh_tong(10, 20)
print(f"Tổng 10 + 20 = {ket_qua}")

chao_tan_su("Bình")
chao_tan_su("Lan", "Chào mừng")

# 7. Xử lý ngoại lệ (try-except)
print("\n=== Xử lý lỗi chia cho 0 ===")
so_a = 10
so_b = 0

try:
    ket_qua_chia = so_a / so_b
    print(f"Kết quả: {ket_qua_chia}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print(f"Lỗi không xác định: {e}")

# 8. Bài tập nhỏ: Tính điểm trung bình và xếp loại học lực
"""
Bài tập: Viết chương trình nhập vào danh sách điểm, tính điểm trung bình và xếp loại:
- 9.0 trở lên: Xuất sắc
- 8.0 - 8.9: Giỏi
- 6.5 - 7.9: Khá
- 5.0 - 6.4: Trung bình
- Dưới 5.0: Yếu
"""

def xep_loai_hoc_luc(diem):
    """Hàm xếp loại học lực"""
    if diem >= 9.0:
        return "Xuất sắc"
    elif diem >= 8.0:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def bai_tap_tinh_diem():
    """Bài tập nhỏ"""
    print("\n=== Bài tập: Tính điểm trung bình và xếp loại ===")
    diem_so = []
    n = int(input("Nhập số lượng môn học: "))
    
    for i in range(n):
        diem = float(input(f"Nhập điểm môn {i+1}: "))
        diem_so.append(diem)
    
    diem_tb = sum(diem_so) / len(diem_so)
    loai = xep_loai_hoc_luc(diem_tb)
    
    print(f"Điểm trung bình: {diem_tb:.2f}")
    print(f"Xếp loại: {loai}")

# 9. Hàm chính
def main():
    print("Chào mừng đến với Bài 52: Tổng Hợp Kiến Thức Python Cơ Bản!")
    
    # Chạy bài tập nhỏ
    bai_tap_tinh_diem()
    
    print("\nCảm ơn bạn đã thực hành các kiến thức cơ bản của Python!")

# Gọi hàm main khi chạy file
if __name__ == "__main__":
    main()
```