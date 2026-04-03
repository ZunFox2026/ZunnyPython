# -*- coding: utf-8 -*-
"""
Python 4 Cấp Độ Cơ Bản - Bài học tổng hợp
Tác giả: Học viên Python
Mục tiêu:
- Giới thiệu 4 cấp độ cơ bản trong Python: Biến, Câu điều kiện, Vòng lặp, Hàm
- Mỗi phần có ví dụ minh họa và bài tập nhỏ
"""

# Cấp độ 1: Biến và Kiểu dữ liệu
# Biến dùng để lưu trữ dữ liệu
# Các kiểu dữ liệu phổ biến: int, float, str, bool

# Ví dụ 1: Khai báo biến
ten = "An"              # chuỗi
tuoi = 15               # số nguyên
chieu_cao = 1.75        # số thực
la_hoc_sinh = True      # boolean

print("Cấp độ 1 - Biến:")
print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

# Cấp độ 2: Câu điều kiện (if-elif-else)
# Dùng để rẽ nhánh chương trình dựa trên điều kiện

# Ví dụ 2: Kiểm tra tuổi để xếp loại
print("\nCấp độ 2 - Câu điều kiện:")
if tuoi < 13:
    loai = "thiếu nhi"
elif tuoi < 18:
    loai = "thiếu niên"
else:
    loai = "người lớn"

print(f"{ten} thuộc nhóm: {loai}")

# Bài tập nhỏ 1: Viết điều kiện kiểm tra chieu_cao > 1.7 thì in "cao", ngược lại in "thấp"
if chieu_cao > 1.7:
    print("cao")
else:
    print("thấp")

# Cấp độ 3: Vòng lặp
# Dùng để lặp lại một đoạn mã nhiều lần

# Ví dụ 3: In bảng cửu chương nhỏ của số 5
print("\nCấp độ 3 - Vòng lặp:")
print("Bảng cửu chương 5:")
for i in range(1, 6):  # lặp từ 1 đến 5
    print(f"5 x {i} = {5 * i}")

# Ví dụ 4: Dùng while để đếm ngược
dem = 3
print("Đếm ngược:")
while dem > 0:
    print(dem)
    dem -= 1
print("Khởi động!")

# Bài tập nhỏ 2: Dùng for in các số chẵn từ 2 đến 10
print("Các số chẵn từ 2 đến 10:")
for i in range(2, 11, 2):
    print(i)

# Cấp độ 4: Hàm (Function)
# Hàm giúp gói gọn đoạn mã để tái sử dụng

# Ví dụ 5: Hàm tính diện tích hình chữ nhật
def tinh_dien_tich(h, w):
    """
    Hàm tính diện tích hình chữ nhật
    h: chiều cao, w: chiều rộng
    Trả về diện tích
    """
    return h * w

# Gọi hàm
dien_tich = tinh_dien_tich(5, 3)
print(f"\nCấp độ 4 - Hàm:")
print(f"Diện tích hình chữ nhật 5x3: {dien_tich}")

# Ví dụ 6: Hàm chào hỏi
def xin_chao(ten_nguoi, gio):
    """
    Hàm chào theo thời gian
    """
    if gio < 12:
        chao = "Chào buổi sáng"
    elif gio < 18:
        chao = "Chào buổi chiều"
    else:
        chao = "Chào buổi tối"
    print(f"{chao}, {ten_nguoi}!")

# Gọi hàm
xin_chao("Bình", 10)
xin_chao("Lan", 19)

# Bài tập nhỏ 3: Viết hàm tinh_bmi(can_nang, chieu_cao) -> trả về BMI
def tinh_bmi(can_nang, chieu_cao):
    """
    Tính chỉ số BMI = cân nặng / (chiều cao)^2
    """
    return can_nang / (chieu_cao ** 2)

# Kiểm thử hàm
bmi = tinh_bmi(60, 1.70)
print(f"Chỉ số BMI: {bmi:.2f}")

# Hàm main - điểm bắt đầu chương trình
def main():
    print("=" * 50)
    print("PYTHON 4 CẤP ĐỘ CƠ BẢN - BÀI TẬP TỔNG HỢP")
    print("=" * 50)

    # Gọi lại một số ví dụ
    print(f"Xin chào, tôi là {ten}, {tuoi} tuổi.")
    
    # Gọi hàm xin_chao
    xin_chao(ten, 14)

    # Tính BMI cho người này (giả sử cân 50kg)
    bmi_an = tinh_bmi(50, chieu_cao)
    print(f"BMI của {ten}: {bmi_an:.2f}")

    print("\nChương trình kết thúc. Cảm ơn bạn!")

# Chạy chương trình
if __name__ == "__main__":
    main()

# Gợi ý mở rộng:
# - Thử nhập dữ liệu từ người dùng bằng input()
# - Dùng list và dictionary ở cấp độ nâng cao hơn
# - Viết hàm kiểm tra số nguyên tố
```