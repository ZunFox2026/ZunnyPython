####################
# exercises.py
# Bài tập lập trình phản xạ
####################

def call_method(obj, method_name, *args):
    """
    Gọi phương thức method_name trên đối tượng obj với các tham số *args.
    Nếu phương thức không tồn tại hoặc không thể gọi, trả về None.
    """
    pass

def find_classes_in_module(module, base_class):
    """
    Tìm tất cả các lớp trong module kế thừa từ base_class (trừ chính base_class).
    Trả về danh sách các class.
    """
    pass

def safe_get(obj, attr_path, default=None):
    """
    Lấy giá trị từ thuộc tính lồng nhau theo đường dẫn chuỗi.
    Ví dụ: safe_get(user, 'profile.theme', 'dark')
    """
    pass

def log_calls(func):
    """
    Decorator: in ra tên hàm đã gọi hàm được trang trí.
    Sử dụng inspect.stack() để lấy thông tin.
    """
    pass

class Plugin:
    """Base class cho plugin"""
    def execute(self):
        raise NotImplementedError

class DataPlugin(Plugin):
    def execute(self):
        return "Xử lý dữ liệu"

class ReportPlugin(Plugin):
    def execute(self):
        return "Tạo báo cáo"

def load_plugins():
    """
    Tự động tìm tất cả các lớp kế thừa từ Plugin trong module hiện tại
    và trả về danh sách các instance.
    """
    pass