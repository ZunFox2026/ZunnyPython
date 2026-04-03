import inspect
import time
import functools

# --- Ví dụ 1: Decorator ghi log tham số đầu vào ---
def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số:")
        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value} (kiểu: {type(value).__name__})")
        
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_arguments
def greet(name: str, age: int = 18):
    return f"Xin chào {name}, bạn {age} tuổi."

# --- Ví dụ 2: Kiểm tra kiểu tham số tại runtime ---
def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Lấy type hints
type_hints = func.__annotations__
        
        for param_name, value in bound_args.arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Tham số '{param_name}' của hàm '{func.__name__}' "
                        f"phải là {expected_type}, nhận được {type(value)}"
                    )
        
        return func(*args, **kwargs)
    return wrapper

@validate_types
def create_user(username: str, age: int, active: bool = True):
    return {"username": username, "age": age, "active": active}

# --- Ví dụ 3: Liệt kê phương thức và thuộc tính của lớp ---

class Calculator:
    def __init__(self):
        self.version = "1.0"
    
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def _private_method(self):
        pass

    @staticmethod
    def pi():
        return 3.14159

    @classmethod
    def info(cls):
        return "Máy tính v1.0"

def list_class_members(cls):
    print(f"Phân tích lớp: {cls.__name__}")
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    for name, func in methods:
        print(f"- Phương thức: {name}")
        
    attrs = [attr for attr in dir(cls) if not attr.startswith('_') and not callable(getattr(cls, attr))]
    for attr in attrs:
        print(f"- Thuộc tính: {attr} = {getattr(cls, attr)}")

# Chạy ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Ghi log tham số ===")
    greet("An", 25)
    
    print("\n=== Ví dụ 2: Kiểm tra kiểu dữ liệu ===")
    try:
        user = create_user("Binh", 30, True)
        print("Tạo user thành công:", user)
        # create_user("Lan", "không phải số")  # Sẽ lỗi
    except TypeError as e:
        print("Lỗi kiểm tra kiểu:", e)
    
    print("\n=== Ví dụ 3: Liệt kê thành viên lớp ===")
    list_class_members(Calculator)