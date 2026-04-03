"""
Bài học: Python 57 - Lập Trình Cơ Bản Cho Người Mới Bắt Đầu
Mục tiêu:
- Giới thiệu cú pháp cơ bản của Python
- Sử dụng biến, kiểu dữ liệu, vòng lặp, điều kiện
- Viết hàm đơn giản và nhập xuất dữ liệu
"""

# 1. In thông điệp chào mừng
print("Chào mừng bạn đến với bài học Python cơ bản!")

# 2. Biến và kiểu dữ liệu cơ bản
ten = "An"           # Chuỗi (string)
tuoi = 16            # Số nguyên (int)
chieu_cao = 1.75     # Số thực (float)
la_hoc_sinh = True   # Boolean (True/False)

# In thông tin ra màn hình
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} mét")
print(f"Là học sinh: {la_hoc_sinh}")

# 3. Nhập dữ liệu từ người dùng
ho_ten = input("Nhập họ tên của bạn: ")
nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = 2025
tuoi_hien_tai = nam_hien_tai - nam_sinh

print(f"Xin chào {ho_ten}, bạn {tuoi_hien_tai} tuổi.")

# 4. Cấu trúc điều kiện (if-elif-else)
if tuoi_hien_tai < 13:
    print("Bạn là thiếu nhi.")
elif tuoi_hien_tai < 18:
    print("Bạn là thanh thiếu niên.")
else:
    print("Bạn đã trưởng thành.")

# 5. Vòng lặp for - in ra các số từ 1 đến 5
print("\nIn các số từ 1 đến 5:")
for i in range(1, 6):
    print(i)

# 6. Vòng lặp while - đếm ngược từ 5 về 1
print("\nĐếm ngược:")
dem = 5
while dem > 0:
    print(dem)
    dem -= 1  # giảm 1 đơn vị
print("Hết giờ!")

# 7. Định nghĩa hàm đơn giản
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    :param a: số thứ nhất
    :param b: số thứ hai
    :return: tổng của a và b
    """
    return a + b

def chao_mung(ten):
    """
    Hàm chào mừng người dùng
    """
    print(f"Xin chào {ten}! Rất vui được gặp bạn.")

# Gọi hàm
chao_mung("Bình")
ket_qua = tinh_tong(10, 25)
print(f"Tổng của 10 và 25 là: {ket_qua}")

# 8. Danh sách (list) và thao tác cơ bản
danh_sach_mon_hoc = ["Toán", "Văn", "Anh", "Lý"]
print(f"\nDanh sách môn học: {danh_sach_mon_hoc}")

# Thêm môn học mới
danh_sach_mon_hoc.append("Hóa")
print(f"Sau khi thêm Hóa: {danh_sach_mon_hoc}")

# Duyệt danh sách bằng vòng lặp
print("Các môn học bạn đang học:")
for mon in danh_sach_mon_hoc:
    print(f"- {mon}")

# 9. Ví dụ thực tế: Kiểm tra số chẵn/lẻ
so = int(input("\nNhập một số nguyên: "))
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# 10. Bài tập nhỏ: Tính điểm trung bình
"""
Bài tập: Viết chương trình nhập 3 điểm Toán, Văn, Anh
Tính điểm trung bình và xếp loại:
- Nếu ĐTB >= 8.0: Giỏi
- Nếu 6.5 <= ĐTB < 8.0: Khá
- Nếu 5.0 <= ĐTB < 6.5: Trung bình
- Nếu ĐTB < 5.0: Yếu
"""

print("\n--- BÀI TẬP NHỎ: TÍNH ĐIỂM TRUNG BÌNH ---")
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))

diem_trung_binh = (toan + van + anh) / 3
print(f"Điểm trung bình: {diem_trung_binh:.2f}")

if diem_trung_binh >= 8.0:
    xep_loai = "Giỏi"
elif diem_trung_binh >= 6.5:
    xep_loai = "Khá"
elif diem_trung_binh >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Xếp loại: {xep_loai}")

# 11. Kết thúc chương trình
print("\nChúc mừng bạn đã hoàn thành bài học Python cơ bản!")
print("Hãy luyện tập thường xuyên để thành thạo hơn!")

def main():
    """
    Hàm chính để chạy chương trình
    """
    # Toàn bộ chương trình đã được thực thi tuần tự
    # Có thể thêm logic điều khiển ở đây nếu cần
    pass

if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn gọn:**
- Chương trình giới thiệu các khái niệm cơ bản: biến, kiểu dữ liệu, nhập/xuất, điều kiện, vòng lặp, hàm, danh sách.
- Có 2 ví dụ rõ ràng: kiểm tra số chẵn/lẻ và tính điểm trung bình.
- Bài tập nhỏ giúp người mới luyện tập ngay.

🎯 **Gợi ý mở rộng:**
- Thêm xử lý lỗi (dùng `try-except`) khi nhập dữ liệu.
- Lưu điểm số vào danh sách và tính trung bình bằng vòng lặp.