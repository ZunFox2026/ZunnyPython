import inspect
from functools import wraps

class User:
    def __init__(self, name=None, age=None, profile=None):
        self.name = name
        self.age = age
        self.profile = profile

class Profile:
    def __init__(self, email=None, city=None):
        self.email = email
        self.city = city

##############
# Bài tập 1 #
##############
def safe_getattr(obj, attr_path, default=None):
    """
    Truy cập thuộc tính lồng nhau qua chuỗi đường dẫn, ví dụ: 'profile.email'
    Nếu không tồn tại, trả về default.
    """
    attributes = attr_path.split('.')
    current = obj
    for attr in attributes:
        if hasattr(current, attr):
            current = getattr(current, attr)
        else:
            return default
    return current

##############
# Bài tập 2 #
##############
def list_public_methods(cls):
    """
    Trả về danh sách tên các phương thức công khai của lớp (không bắt đầu bằng '_')
    """
    methods = []
    for name, value in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not name.startswith('_'):
            methods.append(name)
    return methods

##############
# Bài tập 3 #
##############
def log_calls(func):
    """
    Decorator: in ra tên hàm gọi và tên hàm đang được gọi
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin stack
        stack = inspect.stack()
        caller_name = stack[1].function  # Hàm gọi đến
        current_name = func.__name__
        print(f"[LOG] Hàm '{caller_name}' đã gọi tới hàm '{current_name}'")
        return func(*args, **kwargs)
    return wrapper

##############
# Bài tập 4 #
##############
def create_object_from_dict(cls, data):
    """
    Tạo một đối tượng từ lớp cls, gán các thuộc tính từ dictionary data
    """
    obj = cls()
    for key, value in data.items():
        setattr(obj, key, value)
    return obj

##############
# Bài tập 5 #
##############
def find_functions_with_annotation(module, annotation):
    """
    Tìm tất cả các hàm trong module có annotation cụ thể (ví dụ: str, int)
    Trả về danh sách tên hàm.
    """
    functions = []
    # Lấy tất cả các thành viên trong module
    for name, obj in inspect.getmembers(module, predicate=inspect.isfunction):
        sig = inspect.signature(obj)
        for param in sig.parameters.values():
            if param.annotation == annotation:
                functions.append(name)
                break  # Chỉ cần 1 tham số khớp là đủ
    return functions