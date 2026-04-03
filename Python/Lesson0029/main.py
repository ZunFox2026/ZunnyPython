import time
import functools

# --- Ví dụ 1: Đo thời gian thực thi ---

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

@time_it
def tinh_tong(n):
    """Tính tổng từ 1 đến n"""
    return sum(range(1, n + 1))

# --- Ví dụ 2: Xác thực người dùng ---

def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            print(f"Truy cập bị từ chối: Người dùng '{user['name']}' không phải admin.")
            return None
        print(f"Xác thực thành công cho '{user['name']}'")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def xoa_nguoi_dung(user, user_id):
    """Xóa người dùng (giả lập)"""
    print(f"Đã xóa người dùng có ID: {user_id}")
    return True

# --- Ví dụ 3: Ghi log mỗi lần gọi hàm ---

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Đang gọi hàm: {func.__name__} với tham số: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm {func.__name__} đã hoàn thành.")
        return result
    return wrapper

@log_calls
def tinh_giai_thua(n):
    """Tính giai thừa của n"""
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

# --- Chạy các ví dụ ---
if __name__ == "__main__":
    print("=== Ví dụ 1: Đo thời gian ===")
    ket_qua_tong = tinh_tong(100000)
    print(f"Tổng: {ket_qua_tong}\n")

    print("=== Ví dụ 2: Xác thực người dùng ===")
    user_admin = {'name': 'An', 'role': 'admin'}
    user_normal = {'name': 'Binh', 'role': 'user'}

    xoa_nguoi_dung(user_admin, 123)
    xoa_nguoi_dung(user_normal, 456)
    print()

    print("=== Ví dụ 3: Ghi log ===")
    ket_qua_gt = tinh_giai_thua(5)
    print(f"Giai thừa(5) = {ket_qua_gt}")
