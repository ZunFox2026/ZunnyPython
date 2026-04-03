from typing import Any, Callable, get_type_hints
import inspect
import functools

# ------------------------
# Bài tập 1: Viết decorator @log_calls
# ------------------------

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Hàm '{func.__name__}' được gọi với:")
        for param_name, value in bound_args.arguments.items():
            print(f"  {param_name} = {value} (kiểu: {type(value).__name__})")
        return func(*args, **kwargs)
    return wrapper


# ------------------------
# Bài tập 2: In mã nguồn các hàm trong một module
# ------------------------

def print_function_sources(module):
    """In mã nguồn của tất cả các hàm trong module."""
    print(f"=== Mã nguồn các hàm trong {module.__name__} ===")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith('_'):  # Bỏ qua hàm nội bộ
            continue
        try:
            source = inspect.getsource(obj)
            print(f"\n--- Hàm: {name} ---")
            print(source.rstrip())
        except OSError:
            print(f"  Không thể lấy mã nguồn của {name}")


# ------------------------
# Bài tập 3: Phân tích tham số hàm
# ------------------------

def analyze_function_params(func):
    """In chi tiết các tham số của hàm: tên, kiểu, mặc định."""
    print(f"Phân tích tham số của hàm '{func.__name__}':")
    
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)
    
    for name, param in sig.parameters.items():
        param_type = type_hints.get(name, 'Không xác định')
        default = param.default if param.default != inspect.Parameter.empty else 'Không có'
        
        print(f"  - {name}: ")
        print(f"      Kiểu: {param_type}")
        print(f"      Mặc định: {default}")
        print(f"      Bắt buộc: {param.default == inspect.Parameter.empty}")


# ------------------------
# Bài tập 4: In ra tên hàm đã gọi hàm hiện tại
# ------------------------

def who_called_me():
    """In ra tên của hàm đã gọi hàm này."""
    stack = inspect.stack()
    if len(stack) < 2:
        print("Không tìm thấy hàm gọi.")
    else:
        caller_frame = stack[1]
        print(f"Hàm hiện tại được gọi bởi: '{caller_frame.function}'")


def caller_function():
    who_called_me()


# ------------------------
# Bài tập 5: Decorator kiểm tra kiểu tham số
# ------------------------

def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy type hints
        hints = get_type_hints(func)
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Kiểm tra từng tham số
        for param_name, value in bound_args.arguments.items():
            expected_type = hints.get(param_name)
            if expected_type and not isinstance(value, expected_type):
                print(f"[CẢNH BÁO] Tham số '{param_name}' của hàm '{func.__name__}' \
                      nên là kiểu {expected_type}, nhưng lại là {type(value)}")
        
        return func(*args, **kwargs)
    return wrapper

@validate_types
def add_numbers(a: int, b: int) -> int:
    return a + b