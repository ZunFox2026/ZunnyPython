import time
import functools

# ================== VÍ DỤ 1: Đo thời gian thực thi ==================

def do_thoi_gian(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = func(*args, **kwargs)
        ket_thuc = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {ket_thuc - bat_dau:.4f} giây")
        return ket_qua
    return wrapper

@do_thoi_gian
def tinh_tong(n):
    """Tính tổng từ 1 đến n"""
    return sum(range(1, n + 1))

# ================== VÍ DỤ 2: Kiểm tra đầu vào ==================

def kiem_tra_duong(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Kiểm tra tất cả tham số vị trí
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Tất cả tham số phải là số dương. Phát hiện: {arg}")
        return func(*args, **kwargs)
    return wrapper

@kiem_tra_duong
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    """Tính diện tích hình chữ nhật"""
    return chieu_dai * chieu_rong

# ================== VÍ DỤ 3: Ghi log hoạt động ==================

def log_thao_tac(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Đang thực hiện hàm: {func.__name__}")
        if args or kwargs:
            print(f"[LOG] Tham số: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm {func.__name__} hoàn thành. Kết quả: {result}")
        return result
    return wrapper

@log_thao_tac
def chao_nguoi_dung(ten, loi_chao="Xin chào"):
    """Chào người dùng với lời chào tùy chọn"""
    return f"{loi_chao}, {ten}!"

# ================== Chạy ví dụ ==================
if __name__ == "__main__":
    print("=== Ví dụ 1: Đo thời gian ===")
    ket_qua_1 = tinh_tong(100000)
    print(f"Kết quả: {ket_qua_1}\n")

    print("=== Ví dụ 2: Kiểm tra đầu vào ===")
    try:
        ket_qua_2 = tinh_dien_tich_hinh_chu_nhat(5, 3)
        print(f"Diện tích: {ket_qua_2}\n")
        
        # Sẽ gây lỗi
        tinh_dien_tich_hinh_chu_nhat(-2, 4)
    except ValueError as e:
        print(f"Lỗi: {e}\n")

    print("=== Ví dụ 3: Ghi log ===")
    ket_qua_3 = chao_nguoi_dung("An", loi_chao="Chào mừng")