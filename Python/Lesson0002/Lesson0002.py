"""
Bài 2: Cấu Trúc Điều Khiển và Hàm Đơn Giản trong Python
Mục tiêu:
- Hiểu cách sử dụng các cấu trúc điều khiển: if, elif, else, for, while
- Viết và sử dụng hàm đơn giản
- Áp dụng kiến thức vào giải quyết bài toán thực tế
"""

# ----------------------------- VÍ DỤ 1: Cấu trúc if-elif-else -----------------------------
def kiem_tra_so():
    """
    Ví dụ 1: Kiểm tra tính chất của một số nguyên (dương, âm, bằng 0)
    """
    print("=== Ví dụ 1: Kiểm tra số dương, âm hoặc bằng 0 ===")
    try:
        so = int(input("Nhập một số nguyên: "))
        
        if so > 0:
            print(f"{so} là số dương.")
        elif so < 0:
            print(f"{so} là số âm.")
        else:
            print("Đây là số 0.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


# ----------------------------- VÍ DỤ 2: Vòng lặp for và while -----------------------------
def in_cac_so():
    """
    Ví dụ 2: In các số từ 1 đến n bằng vòng lặp for và while
    """
    print("\n=== Ví dụ 2: In dãy số bằng vòng lặp ===")
    try:
        n = int(input("Nhập n (n > 0): "))
        
        if n <= 0:
            print("n phải lớn hơn 0.")
            return
        
        print("In bằng vòng lặp for:")
        for i in range(1, n + 1):
            print(i, end=" ")
        print()  # Xuống dòng
        
        print("In bằng vòng lặp while:")
        i = 1
        while i <= n:
            print(i, end=" ")
            i += 1
        print()
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


# ----------------------------- VÍ DỤ 3: Hàm đơn giản với tham số và trả về giá trị -----------------------------
def tinh_giai_thua(n):
    """
    Hàm tính giai thừa của một số nguyên không âm
    """
    if n < 0:
        return None
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

def tinh_tong_binh_phuong(n):
    """
    Hàm tính tổng bình phương các số từ 1 đến n
    """
    tong = 0
    for i in range(1, n + 1):
        tong += i ** 2
    return tong

def vi_du_ham():
    """
    Ví dụ 3: Sử dụng hàm để tính toán
    """
    print("\n=== Ví dụ 3: Sử dụng hàm tính toán ===")
    try:
        n = int(input("Nhập một số nguyên không âm: "))
        
        gt = tinh_giai_thua(n)
        if gt is not None:
            print(f"Giai thừa của {n} là: {gt}")
        else:
            print("Không thể tính giai thừa của số âm.")
        
        tong_bp = tinh_tong_binh_phuong(n)
        print(f"Tổng bình phương từ 1 đến {n} là: {tong_bp}")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


# ----------------------------- BÀI TẬP NHỎ: Kiểm tra số nguyên tố -----------------------------
def la_so_nguyen_to(n):
    """
    Hàm kiểm tra một số có phải là số nguyên tố không
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def bai_tap_nho():
    """
    Bài tập nhỏ: Kiểm tra số nguyên tố
    Yêu cầu người dùng nhập một số và kiểm tra xem nó có phải số nguyên tố không.
    """
    print("\n=== Bài tập nhỏ: Kiểm tra số nguyên tố ===")
    try:
        n = int(input("Nhập một số nguyên: "))
        if la_so_nguyen_to(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


# ----------------------------- Hàm main -----------------------------
def main():
    """
    Hàm chính để chạy chương trình
    """
    print("CHÀO MỪNG ĐẾN VỚI BÀI 2: CẤU TRÚC ĐIỀU KHIỂN VÀ HÀM ĐƠN GIẢN")
    print("=" * 60)
    
    # Chạy các ví dụ
    kiem_tra_so()
    in_cac_so()
    vi_du_ham()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    print("\nCẢM ƠN BẠN ĐÃ SỬ DỤNG CHƯƠNG TRÌNH!")


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```