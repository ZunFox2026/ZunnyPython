"""
Python 56: Lập Trình Cơ Bản Từ Con Số 0
----------------------------------------
Bài học này dành cho người mới bắt đầu học Python từ con số 0.
Chúng ta sẽ tìm hiểu các khái niệm cơ bản: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm và xử lý chuỗi.

Tác giả: AI Tutor
Ngày: 2025
"""

def main():
    # --- 1. Biến và Kiểu Dữ Liệu Cơ Bản ---
    # Biến là nơi lưu trữ dữ liệu
    ten = "An"           # Chuỗi (string)
    tuoi = 16            # Số nguyên (int)
    chieu_cao = 1.75     # Số thực (float)
    da_tot_nghiep = False # Boolean (True/False)

    # In thông tin
    print("=== VÍ DỤ 1: Biến và Kiểu Dữ Liệu ===")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đã tốt nghiệp THPT: {da_tot_nghiep}")

    # --- 2. Câu Lệnh Điều Kiện (if-elif-else) ---
    print("\n=== VÍ DỤ 2: Câu Lệnh Điều Kiện ===")
    if tuoi >= 18:
        print(f"{ten} đã đủ tuổi trưởng thành.")
    elif tuoi >= 16:
        print(f"{ten} đang ở độ tuổi 16-17, cần chờ thêm.")
    else:
        print(f"{ten} chưa đủ tuổi.")

    # --- 3. Vòng Lặp (for và while) ---
    print("\n=== VÍ DỤ 3: Vòng Lặp ===")
    print("In các số từ 1 đến 5 bằng vòng lặp for:")
    for i in range(1, 6):
        print(f"Số: {i}")

    print("In ngược lại bằng vòng lặp while:")
    j = 5
    while j > 0:
        print(f"Số: {j}")
        j -= 1  # giảm j đi 1

    # --- 4. Hàm (Functions) ---
    # Định nghĩa một hàm đơn giản
    def tinh_diem_trung_binh(toan, van, anh):
        """
        Hàm tính điểm trung bình 3 môn
        Input: điểm toán, văn, anh
        Output: điểm trung bình
        """
        return (toan + van + anh) / 3

    # Gọi hàm
    diem_tb = tinh_diem_trung_binh(8.5, 7.0, 9.0)
    print(f"\nĐiểm trung bình: {diem_tb:.2f}")

    # --- 5. Xử lý Chuỗi ---
    # Chuỗi có thể được xử lý dễ dàng
    cau = "  Học lập trình Python rất thú vị!  "
    print(f"\nChuỗi gốc: '{cau}'")
    print(f"Chuỗi đã loại bỏ khoảng trắng: '{cau.strip()}'")
    print(f"Chuyển thành chữ hoa: '{cau.strip().upper()}'")
    print(f"Đếm số từ (gần đúng): {len(cau.split())} từ")

    # --- Bài Tập Nhỏ ---
    print("\n" + "="*40)
    print("BÀI TẬP NHỎ: Viết chương trình kiểm tra số chẵn/lẻ")
    print("Hướng dẫn:")
    print("1. Nhập một số nguyên từ bàn phím")
    print("2. Kiểm tra nếu số đó chẵn hay lẻ")
    print("3. In kết quả ra màn hình")

    # Gợi ý giải bài tập (bạn có thể thử trước khi xem)
    try:
        so = int(input("\nNhập một số nguyên: "))
        if so % 2 == 0:
            print(f"{so} là số chẵn.")
        else:
            print(f"{so} là số lẻ.")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

    # --- Tổng kết ---
    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản!")
    print("Hãy luyện tập thường xuyên để thành thạo Python!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**

- **100 dòng code**, comment tiếng Việt rõ ràng.
- **3 ví dụ**: biến & kiểu dữ liệu, điều kiện, vòng lặp.
- **1 bài tập nhỏ** kèm hướng dẫn: kiểm tra số chẵn/lẻ.
- Sử dụng các khái niệm cơ bản: biến, if, for, while, hàm, chuỗi.
- Tương tác người dùng với `input()` và xử lý lỗi đơn giản.

> 💡 **Gợi ý luyện tập**: Thử sửa hàm `tinh_diem_trung_binh` để nhận danh sách điểm thay vì 3 tham số cố định!