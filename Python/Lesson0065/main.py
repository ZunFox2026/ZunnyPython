import inspect

def ham_mau(a: int, b: str = "hello", c: float = 3.14) -> bool:
    """Hàm mẫu để minh họa"""
    return len(b) > a and c > 0

class LopMau:
    def __init__(self, ten: str):
        self.ten = ten

    def xin_chao(self, loi_chao: str = "Xin chào"):
        return f"{loi_chao}, tôi là {self.ten}"

# --- Ví dụ 1: Kiểm tra chữ ký hàm ---
def vi_du_1():
    print("=== Ví dụ 1: Kiểm tra chữ ký hàm ===")
    sig = inspect.signature(ham_mau)
    print(f"Chữ ký của hàm 'ham_mau': {sig}")

    for name, param in sig.parameters.items():
        print(f"Tham số: {name}")
        print(f"  - Kiểu: {param.annotation if param.annotation != inspect._empty else 'Không xác định'}")
        print(f"  - Mặc định: {param.default if param.default != inspect._empty else 'Không có'}")
        print(f"  - Kiểu tham số: {param.kind}")

# --- Ví dụ 2: Lấy mã nguồn của hàm ---
def vi_du_2():
    print("\n=== Ví dụ 2: Lấy mã nguồn của hàm ===")
    try:
        source = inspect.getsource(ham_mau)
        print("Mã nguồn của hàm 'ham_mau':")
        print(source)
    except OSError:
        print("Không thể lấy mã nguồn (hàm có thể là built-in hoặc từ C)")

# --- Ví dụ 3: Ghi log tự động tên hàm và tham số gọi ---
def ham_goi():
    goi_ham_con()

def goi_ham_con():
    frame = inspect.currentframe()
    info = inspect.getframeinfo(frame)
    caller = inspect.stack()[1]
    print(f"Hàm '{info.function}' được gọi từ '{caller.function}'")
    print(f"File: {info.filename}, Dòng: {info.lineno}")

def vi_du_3():
    print("\n=== Ví dụ 3: Ghi log gọi hàm ===")
    ham_goi()

if __name__ == "__main__":
    vi_du_1()
    vi_du_2()
    vi_du_3()