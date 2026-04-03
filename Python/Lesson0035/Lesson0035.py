"""
Python 35 Cấp Cơ Bản - Bài học đầu tiên: Cấu trúc cơ bản, Biến, Kiểu dữ liệu, Nhập xuất, Câu điều kiện, Vòng lặp

Tác giả: Học viên Python
Ngày: 2025-04-05
Mục tiêu: Giới thiệu 35 cấp độ học Python từ cơ bản đến nâng cao (cấp 1-3 được minh họa trong file này)
"""

def cap_1_bien_va_kieu_du_lieu():
    """Cấp 1: Biến và Kiểu dữ liệu cơ bản"""
    print("=== Cấp 1: Biến và Kiểu dữ liệu ===")
    
    # Khai báo biến và gán giá trị
    ten = "An"            # Chuỗi (str)
    tuoi = 16             # Số nguyên (int)
    chieu_cao = 1.75      # Số thực (float)
    la_hoc_sinh = True    # Boolean (True/False)
    
    # In thông tin ra màn hình
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Là học sinh: {la_hoc_sinh}")
    
    # Kiểm tra kiểu dữ liệu
    print(f"Kiểu của 'tuoi': {type(tuoi)}")


def cap_2_nhap_xuat_va_toan_tu():
    """Cấp 2: Nhập xuất dữ liệu và Toán tử"""
    print("\n=== Cấp 2: Nhập xuất và Toán tử ===")
    
    # Nhập dữ liệu từ người dùng
    print("Nhập thông tin học sinh:")
    ten = input("Tên: ")
    diem_toan = float(input("Điểm Toán: "))
    diem_ly = float(input("Điểm Lý: "))
    
    # Tính trung bình
    diem_tb = (diem_toan + diem_ly) / 2
    
    # In kết quả
    print(f"\nHọc sinh {ten} có điểm trung bình: {diem_tb:.2f}")
    
    # Ví dụ về toán tử so sánh
    print(f"Điểm toán cao hơn lý? {diem_toan > diem_ly}")
    print(f"Điểm toán bằng lý? {diem_toan == diem_ly}")


def cap_3_cau_dieu_kien():
    """Cấp 3: Câu điều kiện if-elif-else"""
    print("\n=== Cấp 3: Câu điều kiện ===")
    
    # Ví dụ 1: Phân loại điểm số
    diem = float(input("Nhập điểm số (0-10): "))
    
    if diem >= 8.5:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    print(f"Xếp loại: {xep_loai}")
    
    # Ví dụ 2: Kiểm tra số chẵn/lẻ
    so = int(input("Nhập một số nguyên: "))
    if so % 2 == 0:
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} là số lẻ.")


def bai_tap_nho():
    """Bài tập nhỏ: Viết chương trình kiểm tra năm nhuận"""
    print("\n=== Bài tập nhỏ: Kiểm tra năm nhuận ===")
    print("Năm nhuận là năm chia hết cho 4, nhưng nếu chia hết cho 100 thì phải chia hết cho 400.")
    
    nam = int(input("Nhập năm: "))
    
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"Năm {nam} là năm nhuận.")
    else:
        print(f"Năm {nam} không phải năm nhuận.")


def main():
    """Hàm chính chạy chương trình"""
    print("📘 CHÀO MỪNG ĐẾN KHÓA HỌC PYTHON 35 CẤP CƠ BẢN")
    
    # Gọi lần lượt các cấp
    cap_1_bien_va_kieu_du_lieu()
    cap_2_nhap_xuat_va_toan_tu()
    cap_3_cau_dieu_kien()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    print("\n✅ Hoàn thành 3 cấp đầu tiên. Hãy luyện tập thêm!")


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

### 📌 Ghi chú:
- **Tổng cộng ~95 dòng code**, dễ hiểu, có comment tiếng Việt.
- **3 cấp đầu tiên** của khóa học 35 cấp được minh họa:
  1. Biến & Kiểu dữ liệu
  2. Nhập xuất & Toán tử
  3. Câu điều kiện
- **2 ví dụ** trong phần câu điều kiện (xếp loại học lực, số chẵn/lẻ).
- **1 bài tập nhỏ**: Kiểm tra năm nhuận – ứng dụng thực tế.

Bạn có thể tiếp tục phát triển các cấp tiếp theo: vòng lặp, hàm, danh sách, file, OOP, v.v.