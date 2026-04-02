# Bài 53: Python Cơ bản
# Mô tả: Tổng hợp các kiến thức nền tảng Python thường gặp ở mức cơ bản
# (biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm, danh sách, từ điển, chuỗi)

def kiem_tra_so_nguyen_duong(so):
    """Kiểm tra xem số truyền vào có phải số nguyên dương hay không."""
    return isinstance(so, int) and so > 0


def tinh_tong_danh_sach(danh_sach):
    """Tính tổng tất cả các phần tử trong danh sách số."""
    tong = 0
    for phan_tu in danh_sach:
        tong += phan_tu
    return tong


def in_bang_cuu_chuong(so):
    """In ra bảng cửu chương của số được truyền vào."""
    print(f"\n--- Bảng cửu chương {so} ---")
    for i in range(1, 11):
        # Sử dụng f-string để căn chỉnh cột cho đẹp mắt
        print(f"{so} x {i:2} = {so * i:3}")


def main():
    print("=== BÀI 53: PYTHON CƠ BẢN ===")

    # 1. Biến và kiểu dữ liệu cơ bản
    print("\n1. Biến và kiểu dữ liệu:")
    ten_ngon_ngu = "Python"
    phien_ban = 3.11
    nam_hoc = 2024
    dang_hoc = True
    print(f"  Ngôn ngữ: {ten_ngon_ngu}")
    print(f"  Phiên bản: {phien_ban} (float)")
    print(f"  Năm học: {nam_hoc} (int)")
    print(f"  Đang học: {dang_hoc} (bool)")

    # 2. Cấu trúc điều kiện if-elif-else
    print("\n2. Cấu trúc điều kiện:")
    diem = 7.8
    if diem >= 9.0:
        xep_loai = "Xuất sắc"
    elif diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    else:
        xep_loai = "Trung bình"
    print(f"  Điểm {diem:.1f} -> Xếp loại: {xep_loai}")

    # 3. Vòng lặp for với danh sách
    print("\n3. Vòng lặp for và danh sách:")
    danh_sach_qua = ["Táo", "Cam", "Xoài", "Nho"]
    print(f"  Danh sách trái cây: {danh_sach_qua}")
    for idx, qua in enumerate(danh_sach_qua, start=1):
        print(f"  {idx}. {qua}")

    # 4. Từ điển (Dictionary)
    print("\n4. Từ điển cơ bản:")
    thong_tin = {
        "ten": "Lập trình viên Python",
        "so_nam_kinh_nghiem": 2,
        "ngon_ngu_chinh": "Python",
        "ky_nang": ["Git", "Django", "Data Analysis"]
    }
    for khoa, gia_tri in thong_tin.items():
        print(f"  {khoa}: {gia_tri}")

    # 5. Xử lý chuỗi cơ bản
    print("\n5. Xử lý chuỗi:")
    chuoi_goc = "  Hello, World!  "
    print(f"  Gốc: '{chuoi_goc}'")
    print(f"  strip(): '{chuoi_goc.strip()}'")
    print(f"  upper(): '{chuoi_goc.upper()}'")
    print(f"  split(): {chuoi_goc.strip().split(',')}")
    print(f"  Độ dài: {len(chuoi_goc)}")

    # 6. Vòng lặp while
    print("\n6. Vòng lặp while:")
    dem = 1
    while dem <= 3:
        print(f"  Đang chạy lần thứ {dem}")
        dem += 1

    # 7. Gọi hàm tự định nghĩa
    print("\n7. Gọi hàm tự viết:")
    so_kiem_tra = 5
    if kiem_tra_so_nguyen_duong(so_kiem_tra):
        print(f"  {