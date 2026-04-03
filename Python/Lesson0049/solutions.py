import inspect
from functools import wraps
from typing import Any, Callable, List, Union, get_origin, get_args

# Bài 1: Viết hàm list_public_methods(cls)
def list_public_methods(cls):
    """In ra tất cả các phương thức public (không bắt đầu bằng '_') của một lớp"""
    # Lấy tất cả thành viên là phương thức
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    print(f"Các phương thức public của lớp {cls.__name__}:")
    for name, method in methods:
        if not name.startswith('_'):
            print(f"  - {name}")

# Bài 2: Viết decorator @log_calls
def log_calls(func):
    """Ghi log mỗi khi hàm được gọi, bao gồm tên hàm và tham số"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo chuỗi biểu diễn tham số
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"[LOG] Gọi hàm: {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"[LOG] Kết quả: {func.__name__} = {result!r}")
        return result
    return wrapper

# Bài 3: Viết hàm analyze_function(func)
def analyze_function(func):
    """In ra chi tiết về một hàm: tên, tham số, kiểu, giá trị mặc định"""
    print(f"Phân tích hàm: {func.__name__}")
    sig = inspect.signature(func)
    for name, param in sig.parameters.items():
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else "Không xác định"
        default = param.default if param.default != inspect.Parameter.empty else "Không có"
        print(f"  Tham số: {name}")
        print(f"    Kiểu: {param_type}")
        print(f"    Mặc định: {default}")

# Bài 4: Viết hàm find_classes_in_module(module)
def find_classes_in_module(module):
    """Trả về danh sách các lớp trong một module"""
    classes = []
    # Duyệt tất cả thành viên trong module
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module.__name__:
            classes.append(obj)
    return classes

# Bài 5: Viết hàm validate_call(func, **kwargs)
def validate_call(func, **kwargs):
    """Kiểm tra xem kwargs có phù hợp với chữ ký của func không"""
    sig = inspect.signature(func)
    try:
        # Cố gắng bind các tham số
        sig.bind(**kwargs)
        # Kiểm tra kiểu nếu có annotation
        for name, value in kwargs.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    expected_type = param.annotation
                    # Xử lý Union type
                    origin = get_origin(expected_type)
                    if origin is Union:
                        args = get_args(expected_type)
                        if not any(isinstance(value, t) for t in args):
                            return False
                    elif not isinstance(value, expected_type):
                        return False
        return True
    except Exception:
        return False