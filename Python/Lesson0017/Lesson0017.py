def main():
    """
    Bài học: Làm Quen Với Biến và Kiểu Dữ Liệu trong Python
    Mục tiêu:
    - Hiểu cách khai báo biến
    - Biết các kiểu dữ liệu cơ bản: int, float, str, bool
    - Biết cách kiểm tra kiểu dữ liệu
    - Thực hành với các phép toán cơ bản
    """

    # ========================
    # 1. KHAI BÁO BIẾN
    # Biến là tên gọi để lưu trữ dữ liệu
    # Python tự động suy ra kiểu dữ liệu khi gán giá trị

    tuoi = 20           # số nguyên (int)
    chieu_cao = 1.75    # số thực (float)
    ten = "Nguyễn Văn A"  # chuỗi (str)
    da_tot_nghiep = True  # giá trị logic (bool): True hoặc False

    # In giá trị các biến
    print("=== KHAI BÁO BIẾN ===")
    print("Tên:", ten)
    print("Tuổi:", tuoi)
    print("Chiều cao:", chieu_cao, "m")
    print("Đã tốt nghiệp:", da_tot_nghiep)


    # ========================
    # 2. KIỂM TRA KIỂU DỮ LIỆU
    # Dùng hàm type() để kiểm tra kiểu dữ liệu của biến

    print("\n=== KIỂM TRA KIỂU DỮ LIỆU ===")
    print("Kiểu dữ liệu của 'tuoi':", type(tuoi))
    print("Kiểu dữ liệu của 'chieu_cao':", type(chieu_cao))
    print("Kiểu dữ liệu của 'ten':", type(ten))
    print("Kiểu dữ liệu của 'da_tot_nghiep':", type(da_tot_nghiep))


    # ========================
    # 3. CÁC KIỂU DỮ LIỆU CƠ BẢN - VÍ DỤ

    print("\n=== CÁC VÍ DỤ VỀ KIỂU DỮ LIỆU ===")

    # Ví dụ 1: Số nguyên và số thực
    a = 10
    b = 3.5
    tong = a + b
    print(f"{a} + {b} = {tong} → Kiểu: {type(tong)}")

    # Ví dụ 2: Chuỗi ký tự
    ho = "Trần"
    ten_dem = "Thị"
    ten = "B"
    ho_ten = ho + " " + ten_dem + " " + ten  # Nối chuỗi
    print("Họ tên đầy đủ:", ho_ten)

    # Ví dụ 3: Biến boolean trong biểu thức điều kiện
    diem = 8.5
    dat_yeu_cau = diem >= 5.0
    print(f"Điểm {diem} có đạt yêu cầu? {dat_yeu_cau}")


    # ========================
    # 4. ÉP KIỂU DỮ LIỆU
    # Chuyển đổi giữa các kiểu dữ liệu

    print("\n=== ÉP KIỂU DỮ LIỆU ===")
    so_str = "100"           # chuỗi
    so_int = int(so_str)     # chuyển thành số nguyên
    so_float = float(so_str) # chuyển thành số thực
    print(f"Chuỗi '{so_str}' → int: {so_int}, float: {so_float}")

    # Chuyển số thành chuỗi
    gia_tri_so = 42
    chuoi_so = str(gia_tri_so)
    print(f"Số {gia_tri_so} → chuỗi: '{chuoi_so}'")


    # ========================
    # 5. BÀI TẬP NHỎ
    # Yêu cầu người dùng nhập thông tin và xử lý đơn giản

    print("\n=== BÀI TẬP NHỎ ===")
    print("Hãy nhập thông tin của bạn:")

    # Nhập dữ liệu từ người dùng (luôn trả về str)
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    tuoi_nguoi_dung = int(input("Nhập tuổi của bạn: "))  # ép kiểu sang int
    chieu_cao_nguoi_dung = float(input("Nhập chiều cao (m): "))

    # Xử lý và in kết quả
    print(f"\nThông tin bạn vừa nhập:")
    print(f"- Tên: {ten_nguoi_dung} (kiểu: {type(ten_nguoi_dung)})")
    print(f"- Tuổi: {tuoi_nguoi_dung} (kiểu: {type(tuoi_nguoi_dung)})")
    print(f"- Chiều cao: {chieu_cao_nguoi_dung} m (kiểu: {type(chieu_cao_nguoi_dung)})")

    # Kiểm tra tuổi
    if tuoi_nguoi_dung >= 18:
        print(f"{ten_nguoi_dung}, bạn đã đủ tuổi trưởng thành.")
    else:
        print(f"{ten_nguoi_dung}, bạn chưa đủ tuổi trưởng thành.")


    # ========================
    # 6. GHI NHỚ
    """
    ✅ Ghi nhớ:
    - Biến được tạo khi gán giá trị: ten_bien = gia_tri
    - Các kiểu dữ liệu phổ biến: int, float, str, bool
    - Dùng type() để kiểm tra kiểu dữ liệu
    - Dùng int(), float(), str() để ép kiểu
    - input() luôn trả về chuỗi → cần ép kiểu nếu cần số
    """

    print("\nChúc mừng bạn đã hoàn thành bài học về Biến và Kiểu Dữ Liệu!")


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```