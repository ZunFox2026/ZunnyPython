import inspect
import time
from functools import wraps

# -----------------------------
# Ví dụ 1: Ghi log tự động tên hàm và tham số
# -----------------------------

def debug_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin về tham số của hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[DEBUG] Gọi hàm: {func.__name__}")
        print(f"[DEBUG] Tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        print(f"[DEBUG] Kết quả: {result}\n")
        return result
    return wrapper

@debug_calls
def tinh_tong(a: int, b: int = 5):
    return a + b

@debug_calls
def chao_ho(name, age=25, city="Hà Nội"):
    return f"Xin chào {name}, {age} tuổi, ở {city}"

# -----------------------------
# Ví dụ 2: Kiểm tra và hiển thị thông tin về một lớp
# -----------------------------

class NhanVien:
    def __init__(self, ten, tuoi, luong):
        self.ten = ten
        self.tuoi = tuoi
        self.luong = luong
    
    def gioi_thieu(self):
        return f"Tôi là {self.ten}, {self.tuoi} tuổi, lương {self.luong}"
    
    def tang_luong(self, phan_tram):
        self.luong *= (1 + phan_tram)
        return self.luong
    
    def _phuong_thuc_nhap(self):
        pass  # nội bộ


def in_thong_tin_lop(cls):
    print(f"Thông tin về lớp: {cls.__name__}\n")
    
    # Lấy tất cả thành viên
    for name, obj in inspect.getmembers(cls):
        if inspect.isfunction(obj):
            if not name.startswith("_"):
                print(f"- Phương thức công khai: {name}")
            else:
                print(f"- Phương thức nội bộ: {name}")
        elif not name.startswith("__"):
            print(f"- Thuộc tính: {name}")

# -----------------------------
# Ví dụ 3: Decorator kiểm tra kiểu tham số
# -----------------------------

def kieu_tham_so_bat_buoc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            # Kiểm tra nếu có annotation kiểu
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    print(f"Cảnh báo: Tham số '{param_name}' của hàm '{func.__name__}' \
                          nên là {expected_type}, nhưng nhận {type(value)}")
        
        return func(*args, **kwargs)
    return wrapper

@kieu_tham_so_bat_buoc
def tinh_dien_tich(chieu_dai: float, chieu_rong: float):
    return chieu_dai * chieu_rong

# -----------------------------
# Chạy ví dụ
# -----------------------------
if __name__ == "__main__":
    print("=== Ví dụ 1: Debug calls ===")
    tinh_tong(10, 7)
    chao_ho("Minh", age=30)
    
    print("=== Ví dụ 2: Thông tin lớp ===")
    in_thong_tin_lop(NhanVien)
    
    print("\n=== Ví dụ 3: Kiểm tra kiểu ===")
    tinh_dien_tich(5.0, 3.0)  # OK
    tinh_dien_tich(5, 3)       # Cảnh báo: int thay vì float
