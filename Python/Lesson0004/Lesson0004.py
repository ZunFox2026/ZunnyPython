# Bài 4: Python Cơ bản
# Chương trình minh hoạ các khái niệm cơ bản: biến, kiểu dữ liệu, input/output,
# câu điều kiện, vòng lặp, hàm, list, dict.

def tinh_nam_sinh(tuoi, nam_hien_tai=2025):
    """Tính năm sinh từ tuổi và năm hiện tại."""
    return nam_hien_tai - tuoi

def la_so_nguyen_to(n):
    """Kiểm tra xem n có phải là số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bang_cuu_chuong(n):
    """In bảng cửu chương của n từ 1 đến 10."""
    print(f"\nBảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def main():
    print("=== Chương trình Python Cơ bản ===")
    
    # Nhập thông tin từ người dùng
    ten = input("Nhập tên của bạn: ")
    try:
        tuoi = int(input("Nhập tuổi của bạn: "))
    except ValueError:
        print("Tuổi phải là số nguyên. Đặt tuổi mặc định là 0.")
        tuoi = 0
    
    # Tính và hiển thị năm sinh
    nam_sinh = tinh_nam_sinh(tuoi)
    print(f"Xin chào {ten}! Bạn sinh năm {nam_sinh}.")
    
    # Kiểm tra thành년
    if tuoi >= 18:
        print("Bạn đã thành년.")
    else:
        print("Bạn còn nhỏ tuổi.")
    
    # Kiểm tra số nguyên tố
    if la_so_nguyen_to(tuoi):
        print(f"Tuổi {tuoi} là số nguyên tố.")
    else:
        print(f"Tuổi {tuoi} không phải là số nguyên tố.")
    
    # Nhập một số để in bảng cửu chương
    try:
        so = int(input("\nNhập một số để xem bảng cửu chương (mặc định 7): "))
    except ValueError:
        so = 7
        print("Giá trị không hợp lệ, sử dụng mặc định 7.")
    bang_cuu_chuong(so)
    
    # Minh hoạ list
    mon_hoc = ["Toán", "Lý", "Hóa", "Văn", "Anh"]
    print(f"\nDanh sách môn học: {mon_hoc}")
    mon_hoc.append("Sử")
    print(f"Sau khi thêm 'Sử': {mon_hoc}")
    mon_hoc.remove("Lý")
    print(f"Sau khi xóa 'Lý': {mon_hoc}")
    
    # Minh hoạ dict
    sinh_vien = {
        "ten": ten,
        "tuoi": tuoi,
        "lop": "12A1",
        "diem": {"Toan": 8.5: