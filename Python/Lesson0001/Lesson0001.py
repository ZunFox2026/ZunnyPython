# -*- coding: utf-8 -*-
"""
Bài 1: Python Cơ bản
Mục tiêu: Giới thiệu các cú pháp nền tảng nhất của ngôn ngữ Python.
Bao gồm: Biến, kiểu dữ liệu cơ bản, phép toán, câu lệnh điều kiện, vòng lặp.
"""

def in_loi_chao():
    """Hàm in ra lời chào cơ bản."""
    print("Chào mừng bạn đến với Bài 1: Python Cơ bản!")

def minh_hoa_kieu_du_lieu():
    """Minh họa các kiểu dữ liệu phổ biến trong Python."""
    so_nguyen = 10              # int: Số nguyên
    so_thuc = 2.5               # float: Số thực
    ho_ten = "Lập trình viên"   # str: Chuỗi ký tự
    da_hoc_chua = True          # bool: Đúng/Sai
    
    print(f"Biến số nguyên: {so_nguyen} (kiểu: {type(so_nguyen).__name__})")
    print(f"Biến số thực: {so_thuc} (kiểu: {type(so_thuc).__name__})")
    print(f"Biến chuỗi: {ho_ten} (kiểu: {type(ho_ten).__name__})")
    print(f"Biến logic: {da_hoc_chua} (kiểu: {type(da_hoc_chua).__name__})")

def thuc_hien_phep_toan():
    """Minh họa các phép toán số học cơ bản."""
    a, b = 15, 4
    print(f"\nPhép toán với a={a}, b={b}:")
    print(f"- Cộng: a + b = {a + b}")
    print(f"- Trừ: a - b = {a - b}")
    print(f"- Nhân: a * b = {a * b}")
    print(f"- Chia thường: a / b = {a / b}")
    print(f"- Chia lấy nguyên: a // b = {a // b}")
    print(f"- Chia lấy dư: a % b = {a % b}")
    print(f"- Lũy thừa: a ** b = {a ** b}")

def su_dung_cau_lenh_dieu_kien():
    """Minh họa cấu trúc rẽ nhánh if/elif/else."""
    diem_so = 82
    print(f"\nXếp loại cho điểm số: {diem_so}")
    
    if diem_so >= 90:
        print("=> Kết quả: Xuất sắc")
    elif diem_so >= 75:
        print("=> Kết quả: Khá")
    elif diem_so >= 50:
        print("=> Kết quả: Trung bình")
    else:
        print("=> Kết quả: Cần cố gắng lại")

def su_dung_vong_lap():
    """Minh họa vòng lặp for và while."""
    print("\n1. Vòng lặp for (in các số từ 1 đến 5):")
    for i in range(1, 6):
        print(f"  Bước {i}", end=" ")
    print()
    
    print("2. Vòng lặp while (đếm ngược từ 3 về 0):")
    dem = 3
    while dem >= 0:
        print(f"  Số: {dem}")
        dem -= 1

def main():
    """Hàm chính điều phối chạy các phần minh họa."""
    print("=" * 40)
    in_loi_chao()
    print("=" * 40)
    
    minh_hoa_kieu_du_lieu()
    thuc_hien_phep_toan()
    su_dung_cau_lenh_dieu_kien()
    su_dung_vong_lap()
    
    print("\n" + "=" * 40)
    print("Hoàn thành Bài 1: Python Cơ bản!")
    print("=" * 40)

# Khối điều kiện để file có thể chạy trực tiếp hoặc import làm module
if __name__ == "__main__":
    main()