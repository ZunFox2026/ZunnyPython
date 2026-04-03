import inspect

# Bài 1: In thông tin các phương thức public của lớp
def print_class_info(cls):
    """In tên và docstring của các phương thức public trong lớp."""
    # Lấy tất cả thành viên là hàm và không bắt đầu bằng _
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    for name, method in methods:
        if not name.startswith("_"):  # Chỉ lấy phương thức public
            doc = inspect.getdoc(method) or "Không có mô tả"
            print(f"{name}: {doc}")

# Bài 2: Phân tích chi tiết tham số hàm
def analyze_function_params(func):
    """In chi tiết từng tham số: tên, annotation, giá trị mặc định."""
    sig = inspect.signature(func)
    print(f"Phân tích hàm: {func.__name__}")
    for name, param in sig.parameters.items():
        # Xử lý annotation
        type_hint = param.annotation
        if type_hint == inspect.Parameter.empty:
            type_hint = "Không có"
        
        # Xử lý giá trị mặc định
        default = param.default
        if default == inspect.Parameter.empty:
            default = "Không có"
        
        print(f"- {name}: kiểu={type_hint}, mặc định={default}")

# Bài 3: Tạo decorator log_call
def log_call(func):
    """Decorator: in tên hàm, tham số, và dòng gọi khi thực thi."""
    def wrapper(*args, **kwargs):
        # Lấy thông tin về nơi gọi hàm
        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        lineno = frame.f_lineno
        
        # Lấy danh sách tham số
        sig = inspect.signature(func)
        try:
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            args_str = ", ".join(f"{k}={v}" for k, v in bound_args.arguments.items())
        except TypeError as e:
            args_str = "(lỗi khi bind tham số)"
        
        print(f"[LOG] Gọi {func.__name__}({args_str}) tại {filename}:{lineno}")
        return func(*args, **kwargs)
    return wrapper

# Bài 4: Tìm hàm trong module có ít nhất min_params tham số
def find_functions_in_module(module, min_params=2):
    """Trả về danh sách tên các hàm trong module có >= min_params tham số."""
    functions = []
    # Lấy tất cả thành viên là hàm
    for name, obj in inspect.getmembers(module, predicate=inspect.isfunction):
        try:
            sig = inspect.signature(obj)
            if len(sig.parameters) >= min_params:
                functions.append(name)
        except (ValueError, TypeError):
            # Một số hàm built-in không lấy được signature
            continue
    return functions

# Bài 5: Kiểm tra phương thức được gọi từ phương thức khác trong lớp
def is_called_from_class_method():
    """Trả về True nếu gọi từ phương thức khác trong cùng lớp."""
    stack = inspect.stack()
    # Gọi hiện tại là [0], hàm gọi nó là [1], v.v.
    if len(stack) < 3:
        return False
    
    # Lấy frame của hàm gọi (gọi từ đâu)
    caller_frame = stack[1]
    caller_self = caller_frame.frame.f_locals.get('self')
    
    if not caller_self:
        return False
    
    # Lấy frame của hàm gọi trước đó (gọi từ đâu đến caller)
    caller_of_caller_frame = stack[2]
    caller_of_caller_self = caller_of_caller_frame.frame.f_locals.get('self')
    
    # Nếu cả hai đều có 'self' và cùng đối tượng -> gọi từ phương thức khác trong lớp
    return caller_self is not None and caller_of_caller_self is caller_self