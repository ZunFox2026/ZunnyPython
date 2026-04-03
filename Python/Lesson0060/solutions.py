import inspect
from functools import wraps

def hello(name, age=20):
    """Chào một người."""
    return f"Xin chào {name}, {age} tuổi."

def greet_all(*names):
    """Chào tất cả mọi người."""
    return " và ".join([f"Xin chào {n}" for n in names])

class User:
    def __init__(self, username, email=""):
        self.username = username
        self.email = email

    def info(self):
        return f"User: {self.username}, Email: {self.email}"

    def change_email(self, new_email):
        self.email = new_email

# Bài tập 1: Liệt kê các hàm trong một module cùng docstring
def list_functions(module):
    """In ra danh sách các hàm trong module cùng với docstring."""
    print("=== Danh sách các hàm ===\n")
    # Lấy tất cả thành viên là hàm
    functions = inspect.getmembers(module, inspect.isfunction)
    
    for name, func in functions:
        doc = inspect.getdoc(func) or "Không có mô tả."
        print(f"- {name}: {doc}")

# Bài tập 2: Viết decorator @log_call ghi log khi gọi hàm
def log_call(func):
    """Decorator ghi log tên hàm và tham số khi gọi."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm
        sig = inspect.signature(func)
        try:
            # Ghép tham số thực tế vào chữ ký
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            args_str = ", ".join([f"{k}={v}" for k, v in bound_args.arguments.items()])
        except Exception as e:
            args_str = "(không thể xác định)"
            
        print(f"[LOG] Gọi hàm: {func.__name__}({args_str})")
        return func(*args, **kwargs)
    return wrapper

# Bài tập 3: Phân tích một lớp, in ra các phương thức và thuộc tính
def analyze_class(cls):
    """In ra tất cả phương thức và thuộc tính của một lớp."""
    print(f"=== Phân tích lớp {cls.__name__} ===\n")
    
    # Lấy các phương thức (hàm trong lớp)
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    print("Phương thức:")
    for name, method in methods:
        sig = inspect.signature(method)
        print(f"  - {name}{sig}")
    
    # Lấy các thuộc tính (nếu có thể xác định từ __init__)
    print("\nThuộc tính (từ __init__):")
    if hasattr(cls, "__init__"):
        init_sig = inspect.signature(cls.__init__)
        for param in list(init_sig.parameters.values())[1:]:  # bỏ qua 'self'
            print(f"  - {param.name} (mặc định: {param.default})")
    else:
        print("  Không tìm thấy __init__")

# Bài tập 4: Tìm các hàm có tham số mặc định
def find_functions_with_defaults(module):
    """Trả về danh sách tên các hàm trong module có tham số có giá trị mặc định."""
    functions = inspect.getmembers(module, inspect.isfunction)
    result = []
    
    for name, func in functions:
        sig = inspect.signature(func)
        for param in sig.parameters.values():
            # Kiểm tra nếu tham số có giá trị mặc định
            if param.default != inspect.Parameter.empty:
                result.append(name)
                break  # Chỉ cần một tham số có mặc định
    
    return result

# Bài tập 5: In thông tin về hàm gọi nó
def print_caller_info():
    """In ra tên hàm gọi nó, tên file và số dòng."""
    # inspect.stack()[1] là frame gọi hàm hiện tại
    caller_frame = inspect.stack()[1]
    func_name = caller_frame.function
    filename = caller_frame.filename
    line_no = caller_frame.lineno
    
    print(f"Hàm '{func_name}' gọi print_caller_info() tại {filename}:{line_no}")

def test_caller():
    print_caller_info()

test_caller()