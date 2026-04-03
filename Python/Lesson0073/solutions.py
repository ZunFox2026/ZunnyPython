import inspect
from functools import wraps

def print_class_info(cls):
    """Bài 1: In ra tất cả phương thức và thuộc tính của một lớp"""
    print(f"Thông tin về lớp {cls.__name__}:")
    
    # Lấy các thuộc tính (không phải hàm)
    print("\nThuộc tính:")
    for name, value in inspect.getmembers(cls):
        if not (inspect.isfunction(value) or inspect.ismethod(value)) and not name.startswith("__"):
            print(f" - {name} = {value}")
    
    # Lấy các phương thức
    print("\nPhương thức:")
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        sig = inspect.signature(method)
        print(f" - {name}{sig}")

def log_call(func):
    """Bài 2: Viết decorator @log_call ghi lại tên hàm, tham số và giá trị trả về"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm: {func.__name__}")
        print(f"[LOG] Tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        
        print(f"[LOG] Trả về: {result}")
        return result
    return wrapper

def find_functions_in_file(module, line_threshold):
    """Bài 3: Tìm các hàm có số dòng mã nguồn > line_threshold"""
    large_functions = []
    for name, func in inspect.getmembers(module, inspect.isfunction):
        try:
            source_lines = inspect.getsourcelines(func)[0]
            if len(source_lines) > line_threshold:
                large_functions.append((name, len(source_lines)))
        except OSError:
            continue  # Không lấy được source
    return large_functions

def who_called_me():
    """Bài 4: In ra tên hàm đã gọi hàm hiện tại"""
    stack = inspect.stack()
    if len(stack) >= 2:
        caller_frame = stack[1]
        print(f"Hàm hiện tại được gọi bởi: {caller_frame.function}")
    else:
        print("Không xác định được ai gọi hàm này.")

def validate_types(func):
    """Bài 5: Kiểm tra kiểu tham số theo annotation. Trả về wrapper kiểm tra kiểu"""
    sig = inspect.signature(func)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Gán tham số vào tên
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Kiểm tra từng tham số
        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            # Kiểm tra annotation có tồn tại và là kiểu dữ liệu
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Tham số '{param_name}' cần là {expected_type.__name__}, "
                        f"nhận được {type(value).__name__}"
                    )
        
        return func(*args, **kwargs)
    
    return wrapper