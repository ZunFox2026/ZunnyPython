import inspect
import functools

# Bài tập 1: Viết hàm kiểm tra tham số bắt buộc
def get_required_params(func):
    sig = inspect.signature(func)
    required = []
    for param_name, param in sig.parameters.items():
        # Tham số bắt buộc là tham số không có giá trị mặc định
        if param.default == param.empty and param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            required.append(param_name)
    return required

# Bài tập 2: Viết decorator kiểm tra kiểu tham số
def type_check(func):
    sig = inspect.signature(func)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Gắn tham số vào chữ ký
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Kiểm tra từng tham số
        for param_name, param_value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            # Nếu có annotation kiểu
            if param.annotation != param.empty:
                expected_type = param.annotation
                # Kiểm tra kiểu dữ liệu
                if not isinstance(param_value, expected_type):
                    raise TypeError(
                        f"Tham số '{param_name}' cần kiểu {expected_type.__name__}, "
                        f"nhưng nhận được {type(param_value).__name__}"
                    )
        
        return func(*args, **kwargs)
    
    return wrapper

# Bài tập 3: In tên hàm gọi nó
def who_called_me():
    # Lấy stack hiện tại
    stack = inspect.stack()
    # Frame [1] là hàm gọi hàm hiện tại
    if len(stack) > 1:
        caller_frame = stack[1]
        print(f"Hàm {caller_frame.function} đã gọi tôi")
    else:
        print("Không xác định được ai gọi")

# Hàm để kiểm thử - không chỉnh sửa
def test_function_a():
    test_function_b()

def test_function_b():
    who_called_me()  # Dự kiến in ra: Hàm test_function_b đã gọi tôi

# Kiểm thử lời giải (bỏ comment để chạy)
# print(get_required_params(lambda x, y, z=10: None))  # ['x', 'y']
# 
# @type_check
def example_func(name: str, age: int):
    return f"{name}, {age} tuổi"

# print(example_func("An", 20))  # OK
# print(example_func("An", "hai mươi"))  # Lỗi TypeError

# test_function_a()