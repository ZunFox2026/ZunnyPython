"""
Python 58: Lập Trình Cơ Bản - Bài 1
Chủ đề: Làm quen với Python - Biến, kiểu dữ liệu, nhập xuất cơ bản
Tác giả: Học viên Python 58
Ngày: 2025

Mục tiêu bài học:
- Hiểu cách khai báo biến trong Python
- Biết các kiểu dữ liệu cơ bản: int, float, str, bool
- Sử dụng lệnh in (print) và nhập (input)
- Viết chương trình đơn giản với các thao tác cơ bản
"""

def main():
    # --- 1. KHAI BÁO BIẾN VÀ KIỂU DỮ LIỆU ---
    
    # Biến số nguyên (integer)
    tuoi = 20
    so_sach = 15
    
    # Biến số thực (float)
    chieu_cao = 1.75
    diem_trung_binh = 8.7
    
    # Biến chuỗi (string)
    ten = "Nguyen Van A"
    lop_hoc = "Python 58"
    
    # Biến logic (boolean)
    da_tot_nghiep = False
    dang_hoc = True
    
    # In thông tin cơ bản
    print("=== BÀI 1: LÀM QUEN VỚI PYTHON ===")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đang học lớp: {lop_hoc}")
    print(f"Đã tốt nghiệp: {da_tot_nghiep}")
    
    # --- 2. NHẬP DỮ LIỆU TỪ NGƯỜI DÙNG ---
    
    print("\n--- NHẬP THÔNG TIN CÁ NHÂN ---")
    
    # Nhập tên
    ho_ten = input("Nhập họ tên của bạn: ")
    
    # Nhập tuổi - cần chuyển đổi kiểu dữ liệu
    tuoi_nhap = int(input("Nhập tuổi của bạn: "))
    
    # Nhập điểm trung bình
    diem = float(input("Nhập điểm trung bình (0.0 - 10.0): "))
    
    # Nhập trạng thái
    tra_loi = input("Bạn có đang học không? (có/không): ")
    dang_hoc_nhap = tra_loi.lower() in ['có', 'co', 'yes', 'y']
    
    # --- 3. XỬ LÝ VÀ HIỂN THỊ KẾT QUẢ ---
    
    print("\n=== THÔNG TIN BẠN VỪA NHẬP ===")
    print(f"Họ tên: {ho_ten}")
    print(f"Tuổi: {tuoi_nhap}")
    print(f"Điểm trung bình: {diem}")
    print(f"Đang học: {dang_hoc_nhap}")
    
    # Tính năm sinh
    nam_hien_tai = 2025
    nam_sinh = nam_hien_tai - tuoi_nhap
    print(f"Năm sinh: {nam_sinh}")
    
    # Đánh giá học lực
    if diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    print(f"Xếp loại học lực: {xep_loai}")
    
    # --- 4. VÍ DỤ THỰC HÀNH ---
    
    print("\n--- VÍ DỤ 1: Tính tổng hai số ---")
    a = 10
    b = 25
    tong = a + b
    print(f"{a} + {b} = {tong}")
    
    print("\n--- VÍ DỤ 2: Chào mừng người dùng ---")
    ten_vi_du = "Minh"
    print("Xin chào, " + ten_vi_du + "! Chúc bạn học Python vui vẻ!")
    
    print("\n--- VÍ DỤ 3: Kiểm tra số chẵn/lẻ ---")
    so = 7
    if so % 2 == 0:
        print(f"{so} là số chẵn")
    else:
        print(f"{so} là số lẻ")
    
    # --- 5. BÀI TẬP NHỎ ---
    """
    Bài tập: Viết chương trình tính diện tích hình chữ nhật
    - Nhập chiều dài và chiều rộng từ người dùng
    - Tính diện tích = chiều dài × chiều rộng
    - In kết quả ra màn hình
    """
    print("\n=== BÀI TẬP NHỎ: TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT ===")
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    dien_tich = chieu_dai * chieu_rong
    print(f"Diện tích hình chữ nhật: {dien_tich} (đơn vị vuông)")
    
    print("\nChúc mừng bạn đã hoàn thành Bài 1!")
    print("Hãy luyện tập thêm bằng cách thay đổi các giá trị và thử các phép tính khác.")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```