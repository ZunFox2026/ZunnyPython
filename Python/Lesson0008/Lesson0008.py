# =============================================
# PYTHON 8 CẤP CƠ BẢN - BÀI HỌC TỔNG HỢP
# File: python_8_cap_co_ban.py
# Mục tiêu: Giới thiệu 8 cấp cơ bản của Python
# từ biến, kiểu dữ liệu đến hàm và cấu trúc điều khiển
# =============================================

def cap_1_bien_va_kieu_du_lieu():
    """Cấp 1: Biến và Kiểu dữ liệu cơ bản"""
    # Biến lưu trữ dữ liệu
    ten = "An"               # Chuỗi (str)
    tuoi = 15                # Số nguyên (int)
    chieu_cao = 1.75         # Số thực (float)
    hoc_gioi = True          # Boolean (True/False)

    print("=== Cấp 1: Biến và Kiểu dữ liệu ===")
    print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Học giỏi: {hoc_gioi}")


def cap_2_cau_truc_dieu_kien():
    """Cấp 2: Cấu trúc điều kiện (if-elif-else)"""
    print("\n=== Cấp 2: Cấu trúc điều kiện ===")
    diem = 85

    if diem >= 90:
        print("Xếp loại: Xuất sắc")
    elif diem >= 80:
        print("Xếp loại: Giỏi")  # Ví dụ này sẽ in dòng này
    elif diem >= 70:
        print("Xếp loại: Khá")
    else:
        print("Xếp loại: Trung bình")


def cap_3_vong_lap():
    """Cấp 3: Vòng lặp (for và while)"""
    print("\n=== Cấp 3: Vòng lặp ===")
    
    # Ví dụ 1: Dùng for để in số từ 1 đến 5
    print("Vòng lặp for - In số từ 1 đến 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()

    # Ví dụ 2: Dùng while để đếm ngược
    print("Vòng lặp while - Đếm ngược từ 3:")
    dem = 3
    while dem > 0:
        print(dem)
        dem -= 1


def cap_4_ham():
    """Cấp 4: Hàm (Function)"""
    print("\n=== Cấp 4: Hàm ===")

    def tinh_tong(a, b):
        """Hàm tính tổng 2 số"""
        return a + b

    # Gọi hàm
    ket_qua = tinh_tong(10, 20)
    print(f"Tổng của 10 và 20 là: {ket_qua}")


def cap_5_danh_sach_va_tu_dien():
    """Cấp 5: Danh sách (list) và Từ điển (dict)"""
    print("\n=== Cấp 5: Danh sách và Từ điển ===")

    # Danh sách học sinh
    hoc_sinh = ["Mai", "Lan", "Nam"]
    print("Danh sách học sinh:", hoc_sinh)

    # Từ điển thông tin học sinh
    thong_tin = {
        "ten": "Mai",
        "tuoi": 14,
        "lop": "8A"
    }
    print("Thông tin học sinh:", thong_tin)
    print(f"{thong_tin['ten']} học lớp {thong_tin['lop']}")


def cap_6_xu_ly_chuoi():
    """Cấp 6: Xử lý chuỗi"""
    print("\n=== Cấp 6: Xử lý chuỗi ===")
    chuoi = "  Học Python rất vui!  "
    print("Chuỗi gốc:", f"'{chuoi}'")
    print("Sau khi strip():", f"'{chuoi.strip()}'")
    print("In hoa:", chuoi.strip().upper())
    print("Tách từ:", chuoi.strip().split())


def cap_7_xu_ly_loi():
    """Cấp 7: Xử lý lỗi với try-except"""
    print("\n=== Cấp 7: Xử lý lỗi ===")
    try:
        so = int(input("Nhập một số (có thể bỏ qua bằng cách nhấn Enter): "))
        print(f"Bình phương số bạn nhập: {so ** 2}")
    except ValueError:
        print("Lỗi: Bạn phải nhập số!")


def cap_8_tap_tin_don_gian():
    """Cấp 8: Đọc/Ghi file đơn giản"""
    print("\n=== Cấp 8: Đọc/Ghi file ===")
    ten_file = "hello.txt"
    
    # Ghi file
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("Chào bạn! Đây là file được tạo bằng Python.\n")
        f.write("Học lập trình vui lắm!")
    
    # Đọc file
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
        print("Nội dung file:")
        print(noi_dung)


# Bài tập nhỏ cho người học
def bai_tap_nho():
    """Bài tập: Viết hàm kiểm tra số chẵn/lẻ"""
    print("\n=== BÀI TẬP NHỎ ===")
    print("Viết chương trình kiểm tra một số là chẵn hay lẻ.")
    
    def kiem_tra_chan_le(n):
        if n % 2 == 0:
            return "chẵn"
        else:
            return "lẻ"
    
    # Kiểm thử
    print(f"Số 4 là số {kiem_tra_chan_le(4)}")
    print(f"Số 7 là số {kiem_tra_chan_le(7)}")


def main():
    """Hàm chính thực thi tất cả các cấp"""
    print("🎯 CHÀO MỪNG ĐẾN KHÓA HỌC: PYTHON 8 CẤP CƠ BẢN\n")
    
    cap_1_bien_va_kieu_du_lieu()
    cap_2_cau_truc_dieu_kien()
    cap_3_vong_lap()
    cap_4_ham()
    cap_5_danh_sach_va_tu_dien()
    cap_6_xu_ly_chuoi()
    
    # Cấp 7: Có thể nhập hoặc không
    cap_7_xu_ly_loi()
    
    cap_8_tap_tin_don_gian()
    bai_tap_nho()

    print("\n✅ Hoàn thành 8 cấp cơ bản của Python!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

### 📝 Hướng dẫn sử dụng:
1. Lưu đoạn code trên vào file `python_8_cap_co_ban.py`
2. Chạy bằng lệnh: `python python_8_cap_co_ban.py`
3. Quan sát kết quả hiển thị từng cấp độ

---

### 📚 Mục tiêu bài học:
- Hiểu 8 khái niệm cơ bản nhất trong Python
- Áp dụng vào thực hành và bài tập nhỏ
- Làm nền tảng cho các bài học nâng cao

> 💡 Gợi ý: Sau bài này, hãy thử mở rộng bài tập kiểm tra chẵn lẻ thành chương trình nhập nhiều số và lưu kết quả vào file!