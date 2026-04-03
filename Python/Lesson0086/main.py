import inspect

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, I'm {self.name}"

    def update_email(self, new_email):
        self.email = new_email

# Ví dụ 1: Gọi phương thức động dựa trên chuỗi
print("=== Ví dụ 1: Gọi phương thức động ===")
user = User("Bob", "bob@example.com")
method_name = "greet"

if hasattr(user, method_name):
    method = getattr(user, method_name)
    if callable(method):
        result = method()
        print(f"Kết quả gọi {method_name}(): {result}")
else:
    print(f"Không tìm thấy phương thức {method_name}")


# Ví dụ 2: Tự động đăng ký các lớp xử lý sự kiện
print("\n=== Ví dụ 2: Tự động đăng ký lớp xử lý ===")

class EventHandler:
    pass

class LoginHandler(EventHandler):
    def handle(self):
        return "Xử lý đăng nhập"

class LogoutHandler(EventHandler):
    def handle(self):
        return "Xử lý đăng xuất"

def discover_handlers(module, base_class):
    """
    Tìm tất cả các lớp trong module kế thừa từ base_class
    """
    handlers = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, base_class) and obj != base_class:
            handlers.append(obj)
    return handlers

# Giả lập lấy các lớp từ module hiện tại (__main__)
# Trong thực tế, sẽ dùng một module riêng
import sys
current_module = sys.modules[__name__]

found_handlers = discover_handlers(current_module, EventHandler)
print("Các handler tìm thấy:")
for handler_cls in found_handlers:
    instance = handler_cls()
    print(f"- {handler_cls.__name__}: {instance.handle()}")


# Ví dụ 3: Truy cập an toàn thuộc tính lồng nhau và ghi log
print("\n=== Ví dụ 3: Truy cập an toàn và ghi log ===")

class Profile:
    def __init__(self, theme="dark", language="vi"):
        self.theme = theme
        self.language = language

class UserWithProfile:
    def __init__(self, username):
        self.username = username
        # Không phải lúc nào cũng có profile

# Hàm truy cập an toàn với log
def safe_get_with_log(obj, attr_path, default=None):
    """
    Truy cập thuộc tính lồng nhau, ví dụ: user.profile.theme
    Đồng thời in log từng bước truy cập
    """
    attrs = attr_path.split('.')
    current = obj
    for attr in attrs:
        print(f"Đang truy cập: {attr}")
        if hasattr(current, attr):
            current = getattr(current, attr)
        else:
            print(f"Lỗi: Không tìm thấy thuộc tính '{attr}'")
            return default
    return current

user1 = UserWithProfile("alice")
user1.profile = Profile(theme="light")

theme = safe_get_with_log(user1, "profile.theme", "default")
print(f"Theme tìm thấy: {theme}")

theme2 = safe_get_with_log(user1, "profile.settings.layout", "compact")
print(f"Layout: {theme2}")