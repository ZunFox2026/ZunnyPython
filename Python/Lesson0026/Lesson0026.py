# Python 26: Lập Trình Cơ Bản Từ A đến Z
# Bài học: Làm quen với các khái niệm lập trình cơ bản bằng Python
# Bao gồm: Biến, kiểu dữ liệu, vòng lặp, điều kiện, hàm và xử lý danh sách

def main():
    """
    Hàm chính để chạy chương trình
    Đây là nơi bắt đầu thực thi chương trình
    """

    # --- 1. KHỞI TẠO BIẾN VÀ KIỂU DỮ LIỆU ---
    print("=== 1. Biến và Kiểu Dữ Liệu ===")
    ten = "Nguyen Van A"        # Chuỗi (string)
    tuoi = 20                   # Số nguyên (int)
    chieu_cao = 1.75            # Số thực (float)
    dang_hoc = True             # Boolean (True/False)

    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đang học: {dang_hoc}")

    # --- 2. CẤU TRÚC ĐIỀU KIỆN (if-elif-else) ---
    print("\n=== 2. Cấu Trúc Điều Kiện ===")
    if tuoi >= 18:
        print(f"{ten} đã đủ tuổi trưởng thành.")
    else:
        print(f"{ten} chưa đủ tuổi trưởng thành.")

    # Ví dụ 2: Phân loại học lực
    diem = 8.5
    if diem >= 9:
        xep_loai = "Xuất sắc"
    elif diem >= 8:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    else:
        xep_loai = "Cần cố gắng"
    print(f"Điểm: {diem} → Xếp loại: {xep_loai}")

    # --- 3. VÒNG LẶP (for và while) ---
    print("\n=== 3. Vòng Lặp ===")
    # Ví dụ: In các số từ 1 đến 5
    print("In số từ 1 đến 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()  # Xuống dòng

    # Ví dụ: Dùng while để đếm ngược
    print("Đếm ngược từ 3 về 1:")
    dem = 3
    while dem > 0:
        print(dem)
        dem -= 1
    print("Hết!")

    # --- 4. DANH SÁCH (list) VÀ HÀM ---
    print("\n=== 4. Danh Sách và Hàm ===")

    # Danh sách điểm số
    diem_so = [7.5, 8.0, 9.2, 6.8, 8.7]

    # Hàm tính trung bình
    def tinh_trung_binh(danh_sach):
        """
        Tính trung bình cộng của danh sách số
        """
        if len(danh_sach) == 0:
            return 0
        return sum(danh_sach) / len(danh_sach)

    # Gọi hàm và in kết quả
    trung_binh = tinh_trung_binh(diem_so)
    print(f"Danh sách điểm: {diem_so}")
    print(f"Điểm trung bình: {trung_binh:.2f}")

    # --- 5. BÀI TẬP NHỎ ---
    print("\n=== 5. Bài Tập Nhỏ ===")
    """
    Bài tập: Viết chương trình kiểm tra số chẵn/lẻ trong danh sách
    Yêu cầu: Duyệt danh sách số, in ra số chẵn và số lẻ
    """
    danh_sach = [1, 4, 7, 8, 10, 15, 16, 20]

    print(f"Danh sách: {danh_sach}")
    so_chan = []
    so_le = []

    for so in danh_sach:
        if so % 2 == 0:
            so_chan.append(so)
        else:
            so_le.append(so)

    print(f"Số chẵn: {so_chan}")
    print(f"Số lẻ: {so_le}")

    # Gợi ý mở rộng: Viết hàm để làm việc này
    def tach_chan_le(danh_sach):
        chan = [x for x in danh_sach if x % 2 == 0]
        le = [x for x in danh_sach if x % 2 != 0]
        return chan, le

    chan, le = tach_chan_le(danh_sach)
    print(f"(Dùng hàm) Chẵn: {chan}, Lẻ: {le}")

    print("\nChúc mừng bạn đã hoàn thành bài học Python cơ bản!")


# Gọi hàm chính để thực thi chương trình
if __name__ == "__main__":
    main()

# --- Ghi chú học tập ---
# ✅ Biến: lưu trữ dữ liệu
# ✅ Kiểu dữ liệu: int, float, str, bool
# ✅ Điều kiện: if-elif-else
# ✅ Vòng lặp: for, while
# ✅ Hàm: def để tạo hàm, tái sử dụng mã
# ✅ Danh sách: lưu nhiều phần tử, dùng list
# 💡 Bài tập: Thử thay đổi danh sách, thêm điều kiện, in theo định dạng khác
```