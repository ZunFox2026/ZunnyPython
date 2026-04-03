import inspect

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profile = Profile("an@gmail.com", "HN")

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def __str__(self):
        return f"User({self.name}, {self.age})"

class Profile:
    def __init__(self, email, city):
        self.email = email
        self.city = city

def debug_obj(obj):
    """
    In ra tất cả các thành viên của một đối tượng (thuộc tính và phương thức)
    """
    print(f"=== Kiểm tra đối tượng: {type(obj).__name__} ===")
    members = inspect.getmembers(obj)
    for name, value in members:
        if not name.startswith('_'):  # Bỏ qua các thành viên nội bộ
            print(f"{name}: {value}")

# Ví dụ 1: Dùng debug_obj
user = User("An", 25)
debug_obj(user)

# Ví dụ 2: Cấu hình động từ dictionary
def apply_config(obj, config):
    """
    Gán các thuộc tính cho đối tượng từ dictionary
    """
    for key, value in config.items():
        if hasattr(obj, key):
            setattr(obj, key, value)
            print(f"Đã cập nhật {key} = {value}")
        else:
            print(f"Cảnh báo: {key} không tồn tại trong đối tượng")

config = {"age": 26, "name": "Bình"}
apply_config(user, config)
print("Sau khi cập nhật:", user)

# Ví dụ 3: Kiểm tra tham số hàm với inspect
from functools import wraps
def validate_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            # Kiểm tra annotation kiểu
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    raise TypeError(f"Tham số '{param_name}' phải là {expected_type.__name__}")
        return func(*args, **kwargs)
    return wrapper

@validate_types
def create_user(name: str, age: int) -> User:
    return User(name, age)

# Test validate_types
try:
    u = create_user("Nam", 20)
    print("Tạo user thành công:", u)
    # create_user(123, "20")  # Sẽ lỗi
except TypeError as e:
    print("Lỗi kiểm tra kiểu:", e)

# Dùng inspect để xem stack
def outer():
    inner()

def inner():
    frame = inspect.currentframe()
    caller = frame.f_back
    print(f"Hàm hiện tại: {caller.f_code.co_name} gọi tới {frame.f_code.co_name}")

print("--- Kiểm tra stack gọi hàm ---")
outer()