"""
Bài học: Python 34 cấp Cơ bản - Chương trình minh họa các khái niệm cơ bản trong Python
Tác giả: Học viên Python
Ngày: 2025

Mục tiêu:
- Ôn tập các khái niệm cơ bản: biến, kiểu dữ liệu, vòng lặp, hàm, điều kiện, danh sách, chuỗi
- Áp dụng vào ví dụ thực tế và bài tập nhỏ
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python hỗ trợ nhiều kiểu dữ liệu: int, float, str, bool, list, tuple, dict, set

ten = "Nguyen Van A"        # chuỗi (str)
tuoi = 20                   # số nguyên (int)
chieu_cao = 1.75            # số thực (float)
la_sinh_vien = True         # boolean (True/False)

# In thông tin
print("=== THÔNG TIN CÁ NHÂN ===")
print(f"Họ tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Cấu trúc điều kiện (if-elif-else)
def xep_loai_hoc_tap(diem):
    """
    Hàm xếp loại học tập dựa trên điểm số
    """
    if diem >= 9.0:
        return "Xuất sắc"
    elif diem >= 7.0:
        return "Giỏi"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Ví dụ 1: Sử dụng hàm xếp loại
print("\n=== VÍ DỤ 1: XẾP LOẠI HỌC TẬP ===")
diem_toan = 8.5
loai = xep_loai_hoc_tap(diem_toan)
print(f"Điểm Toán: {diem_toan} => Xếp loại: {loai}")

# Ví dụ 2: Xử lý danh sách điểm
print("\n=== VÍ DỤ 2: XỬ LÝ DANH SÁCH ĐIỂM ===")
danh_sach_diem = [9.5, 6.0, 8.0, 4.5, 10.0]
print("Điểm các môn học:", danh_sach_diem)

# Duyệt danh sách điểm và in xếp loại từng môn
for i, diem in enumerate(danh_sach_diem, start=1):
    loai = xep_loai_hoc_tap(diem)
    print(f"Môn {i}: {diem} điểm -> {loai}")

# 3. Hàm tính trung bình cộng
def tinh_diem_trung_binh(danh_sach):
    """
    Tính điểm trung bình của danh sách điểm
    """
    if len(danh_sach) == 0:
        return 0
    return sum(danh_sach) / len(danh_sach)

# Tính điểm trung bình
dtb = tinh_diem_trung_binh(danh_sach_diem)
xep_loai_chung = xep_loai_hoc_tap(dtb)
print(f"\nĐiểm trung bình: {dtb:.2f}")
print(f"Xếp loại học lực chung: {xep_loai_chung}")

# 4. Bài tập nhỏ: Đếm số chẵn trong danh sách
def dem_so_chan(danh_sach):
    """
    Đếm số lượng số chẵn trong danh sách số nguyên
    """
    dem = 0
    for so in danh_sach:
        if so % 2 == 0:
            dem += 1
    return dem

# Ví dụ 3: Bài tập đếm số chẵn
print("\n=== VÍ DỤ 3: BÀI TẬP ĐẾM SỐ CHẴN ===")
so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
so_chan = dem_so_chan(so_nguyen)
print(f"Danh sách số: {so_nguyen}")
print(f"Số lượng số chẵn: {so_chan}")

# 5. Bài tập nhỏ: Tìm phần tử lớn nhất
def tim_so_lon_nhat(danh_sach):
    """
    Tìm số lớn nhất trong danh sách
    Giả sử danh sách không rỗng
    """
    so_lon_nhat = danh_sach[0]  # giả sử phần tử đầu là lớn nhất
    for so in danh_sach[1:]:
        if so > so_lon_nhat:
            so_lon_nhat = so
    return so_lon_nhat

# Kiểm thử hàm tìm số lớn nhất
max_value = tim_so_lon_nhat(so_nguyen)
print(f"Số lớn nhất trong danh sách: {max_value}")

# 6. Tổng kết và in lời chào
print("\n=== KẾT THÚC CHƯƠNG TRÌNH ===")
print("Chúc mừng bạn đã hoàn thành bài học cơ bản về Python!")
print("Hãy luyện tập thêm với các bài tập nhỏ sau:")

# Gợi ý bài tập về nhà
print("\n--- BÀI TẬP VỀ NHÀ ---")
print("1. Viết hàm tính tổng các số lẻ trong danh sách.")
print("2. Viết hàm kiểm tra một số có phải số nguyên tố không.")
print("3. Tạo danh sách tên bạn bè và in ra theo thứ tự bảng chữ cái.")

# Hàm chính
def main():
    """
    Hàm chính để chạy chương trình
    """
    print("Chương trình học Python cơ bản - 34 cấp")
    # Các lệnh đã chạy ở trên, có thể thêm logic nếu cần
    pass

# Gọi hàm main() nếu chạy trực tiếp file
if __name__ == "__main__":
    main()
```

---

### 📌 Hướng dẫn sử dụng:
- Lưu đoạn code trên vào file `python_co_ban.py`
- Chạy bằng lệnh: `python python_co_ban.py`
- Kết quả: In ra thông tin, ví dụ, và kết quả xử lý

---

### ✅ Mục tiêu đạt được:
- Hiểu biến, kiểu dữ liệu, hàm, vòng lặp, điều kiện
- Áp dụng vào ví dụ thực tế: xếp loại học lực, xử lý danh sách
- Có bài tập nhỏ để luyện tập thêm

Chúc bạn học tốt với Python! 🐍