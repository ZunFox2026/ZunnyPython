import inspect

class Calculator:
    """Một lớp máy tính đơn giản."""
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result


def greet(name, title="Thưa ông/bà"):
    """Hàm chào hỏi."""
    print(f"{title} {name}, chào bạn!")


def goodbye(name, time="tối"): 
    """Hàm chia tay."""
    print(f"Tạm biệt {name}, chúc bạn một buổi {time} tốt lành!")

# Bài tập 1: Viết hàm log_call để in ra tên hàm và tham số

def log_call():
    # Lấy thông tin khung gọi gần nhất (hàm gọi log_call)
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    args = frame.f_locals
    print(f"[LOG] Hàm '{func_name}' được gọi với tham số: {args}")

# Bài tập 2: Viết hàm in thông tin về một lớp

def print_class_info(cls):
    """In ra tất cả phương thức và thuộc tính của lớp."""
    print(f"Thông tin về lớp: {cls.__name__}")
    print("Các phương thức:")
    for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction):
        print(f"  - {name}{inspect.signature(obj)}")
    
    print("Các thuộc tính (không phải hàm):")
    for name, obj in inspect.getmembers(cls):
        if not inspect.isfunction(obj) and not name.startswith("__"):
            print(f"  - {name} (kiểu: {type(obj).__name__})")

# Bài tập 3: Viết hàm tìm tất cả hàm trong một module

def find_functions_in_module(module):
    """
    Trả về danh sách tên các hàm trong một module.
    """
    functions = []
    # Duyệt qua tất cả các thành viên của module
    for name, obj in inspect.getmembers(module):
        # Kiểm tra nếu là hàm và không phải là hàm nội bộ (bắt đầu bằng __)
        if inspect.isfunction(obj) and not name.startswith("__"):
            functions.append(name)
    return functions

# Bài tập 4: Viết decorator @debug_calls sử dụng inspect

def debug_calls(func):
    """Decorator in ra thông tin khi hàm được gọi."""
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm để hiển thị thông tin rõ hơn
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[DEBUG] Gọi hàm '{func.__name__}' với tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        
        print(f"[DEBUG] Hàm '{func.__name__}' trả về: {result}")
        return result
    return wrapper

# --- Kiểm thử các bài tập ---
if __name__ == "__main__":
    # Test bài 1
    def test_log():
        x = 5
        y = 10
        log_call()  # In ra tên hàm test_log và tham số
    
    print("=== Bài tập 1: log_call ===")
    test_log()
    
    # Test bài 2
    print("\n=== Bài tập 2: print_class_info ===")
    print_class_info(Calculator)
    
    # Test bài 3
    print("\n=== Bài tập 3: find_functions_in_module ===")
    funcs = find_functions_in_module(__name__)  # Dùng module hiện tại
    print("Các hàm trong module:", funcs)
    
    # Test bài 4
    print("\n=== Bài tập 4: @debug_calls ===")
    
    @debug_calls
    def power(base, exp=2):
        return base ** exp
    
    result = power(3, exp=4)