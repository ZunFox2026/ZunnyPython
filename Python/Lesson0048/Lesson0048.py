"""
Bài học: Python 48 Cấp Cơ Bản - Bài 1: Các Khái Niệm Cơ Bản trong Python
Tác giả: Học viên Python
Mục tiêu: Giới thiệu biến, kiểu dữ liệu, vòng lặp, điều kiện, hàm và nhập/xuất.
"""

def main():
    # === 1. Biến và Kiểu Dữ Liệu Cơ Bản ===
    ten = "An"           # Chuỗi (string)
    tuoi = 16            # Số nguyên (int)
    chieu_cao = 1.75     # Số thực (float)
    la_hoc_sinh = True   # Boolean (True/False)

    print("=== Ví dụ 1: Sử dụng biến và kiểu dữ liệu ===")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Là học sinh: {la_hoc_sinh}")

    # === 2. Câu lệnh điều kiện (if-elif-else) ===
    print("\n=== Ví dụ 2: Kiểm tra độ tuổi ===")
    if tuoi < 13:
        print("Bạn là thiếu nhi.")
    elif tuoi < 18:
        print("Bạn là thanh thiếu niên.")
    else:
        print("Bạn đã trưởng thành.")

    # === 3. Vòng lặp for và while ===
    print("\n=== Ví dụ 3: In bảng cửu chương 2 bằng vòng lặp for ===")
    for i in range(1, 11):  # lặp từ 1 đến 10
        print(f"2 x {i} = {2 * i}")

    print("\nIn bằng vòng lặp while:")
    j = 1
    while j <= 10:
        print(f"2 x {j} = {2 * j}")
        j += 1  # tăng j lên 1

    # === 4. Hàm trong Python ===
    def tinh_tong(a, b):
        """Hàm trả về tổng của hai số"""
        return a + b

    def chao_ten(ten):
        """Hàm in lời chào"""
        print(f"Xin chào, {ten}!")

    print("\n=== Ví dụ 4: Gọi hàm ===")
    chao_ten("Bình")
    ket_qua = tinh_tong(5, 7)
    print(f"Tổng của 5 và 7 là: {ket_qua}")

    # === 5. Nhập dữ liệu từ người dùng ===
    print("\n=== Bài tập nhỏ ===")
    print("Hãy nhập thông tin của bạn:")
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    tuoi_nguoi_dung = int(input("Nhập tuổi của bạn: "))

    # Gọi hàm xử lý
    chao_ten(ten_nguoi_dung)
    if tuoi_nguoi_dung >= 18:
        print("Bạn đủ tuổi để lái xe.")
    else:
        print(f"Bạn cần chờ {18 - tuoi_nguoi_dung} năm nữa để được lái xe.")

    # Tính tổng hai số do người dùng nhập
    so_a = float(input("Nhập số thứ nhất: "))
    so_b = float(input("Nhập số thứ hai: "))
    tong = tinh_tong(so_a, so_b)
    print(f"Tổng của {so_a} và {so_b} là: {tong:.2f}")

    # === Tổng kết ===
    print("\nChúc mừng bạn đã hoàn thành bài tập cơ bản!")
    print("Hãy luyện tập thêm với các biến, vòng lặp và hàm.")


# Bài tập nhỏ (tự làm thêm):
# 1. Viết hàm kiểm tra số chẵn/lẻ.
# 2. Viết vòng lặp in các số từ 1 đến n (n nhập từ bàn phím).
# 3. Viết chương trình tính điểm trung bình của 3 môn học.

def bai_tap_chon_loc():
    """Bài tập tự luyện: Kiểm tra số chẵn lẻ"""
    print("\n--- Bài tập tự luyện: Kiểm tra số chẵn lẻ ---")
    num = int(input("Nhập một số nguyên: "))
    if num % 2 == 0:
        print(f"{num} là số chẵn.")
    else:
        print(f"{num} là số lẻ.")


# Chạy chương trình chính
if __name__ == "__main__":
    main()
    # Bỏ comment dòng dưới để làm bài tập thêm
    # bai_tap_chon_loc()
```

---

### 📝 Ghi chú:
- **Độ dài**: Khoảng 100 dòng (bao gồm cả comment và khoảng trắng).
- **Chủ đề**: Các khái niệm cơ bản trong Python: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm, nhập xuất.
- **Ví dụ**: 3 ví dụ rõ ràng.
- **Bài tập nhỏ**: Có phần luyện tập tương tác với người dùng.
- **Comment**: Toàn bộ bằng tiếng Việt, dễ hiểu cho người mới bắt đầu.

> ✅ Phù hợp với khóa học "Python 48 Cấp Cơ Bản" – từng bước từ A đến Z.