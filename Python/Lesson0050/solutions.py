import inspect
import sys
from typing import get_type_hints

# Bài 1: In thông tin hàm gọi
def print_caller_info():
    # Lấy thông tin ngăn xếp
    stack = inspect.stack()
    # [0] là hàm hiện tại, [1] là hàm gọi nó
    caller_frame = stack[1]
    print(f"Hàm hiện tại: {caller_frame.function}")
    if len(stack) > 2:
        parent_frame = stack[2]
        print(f"Được gọi từ: {parent_frame.function}")
    else:
        print("Được gọi trực tiếp từ toàn cục")

def test_caller():
    print_caller_info()

test_caller()

# Bài 2: Decorator log_calls
def log_calls(func):
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm
        sig = inspect.signature(func)
        try:
            # Ghép tham số thực tế vào tham số hình thức
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()  # Áp dụng giá trị mặc định
            
            print(f"[LOG] Gọi hàm '{func.__name__}' với:")
            for param_name, value in bound_args.arguments.items():
                print(f"  {param_name} = {value} (kiểu: {type(value).__name__})")
        except Exception as e:
            print(f"[LOG] Không thể ghi log tham số: {e}")
        
        # Gọi hàm gốc
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name, greeting="Xin chào"):
    print(f"{greeting}, {name}!")

greet("Mai", "Chào bạn")
greet("Lan")

# Bài 3: Khám phá module
def explore_module(module):
    print(f"Khám phá module: {module.__name__}")
    
    # Lấy các hàm
    functions = inspect.getmembers(module, inspect.isfunction)
    print("\n--- Các hàm ---")
    for name, func in functions:
        doc = func.__doc__ or "Không có mô tả"
        print(f"{name}: {doc}")
    
    # Lấy các lớp
    classes = inspect.getmembers(module, inspect.isclass)
    print("\n--- Các lớp ---")
    for name, cls in classes:
        doc = cls.__doc__ or "Không có mô tả"
        print(f"{name}: {doc}")

explore_module(sys.modules[__name__])

# Bài 4: Kiểm tra kiểu tham số
def validate_types(func, *args, **kwargs):
    try:
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Lấy type hints
        type_hints = get_type_hints(func)
        
        for param_name, value in bound_args.arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                # Xử lý Union, Optional, v.v. đơn giản
                if hasattr(expected_type, '__origin__') and expected_type.__origin__ is not None:
                    # Kiểm tra kiểu phức tạp (ví dụ: Union[int, str])
                    if not isinstance(value, expected_type.__args__):
                        return False
                else:
                    if not isinstance(value, expected_type):
                        return False
        return True
    except:
        return False

def sample_function(x: int, y: str):
    pass

print(validate_types(sample_function, 10, "abc"))  # True
print(validate_types(sample_function, "xyz", 123))  # False

# Bài 5: Tìm các hàm có docstring
def find_functions_with_docstring(module):
    functions = inspect.getmembers(module, inspect.isfunction)
    result = []
    for name, func in functions:
        if func.__doc__:  # Nếu có docstring và không rỗng
            result.append(name)
    return result

functions_with_docs = find_functions_with_docstring(sys.modules[__name__])
print("\nCác hàm có docstring:", functions_with_docs)
