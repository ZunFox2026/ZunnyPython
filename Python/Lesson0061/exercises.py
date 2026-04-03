import inspect

# Bài tập 1: Liệt kê các hàm trong một module
def list_functions(module):
    """In ra danh sách các hàm trong module cùng với docstring.
    
    Args:
        module: Module Python (ví dụ: math, os, hoặc module tự định nghĩa)
    """
    pass

# Bài tập 2: Phân tích một lớp
def analyze_class(cls):
    """In ra thông tin chi tiết về một lớp: tên, các phương thức, thuộc tính, docstring.
    
    Args:
        cls: Lớp Python (class object)
    """
    pass

# Bài tập 3: Decorator ghi log vào file
from functools import wraps
def trace_call(func):
    """Decorator ghi lại tên hàm, tham số và kết quả vào file log.txt."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Ghi log vào file log.txt
        pass
    return wrapper

# Bài tập 4: Tìm hàm có từ khóa trong docstring
def find_functions_with_keyword(module, keyword):
    """Tìm các hàm trong module có chứa keyword trong docstring.
    
    Returns:
        Danh sách tên hàm (str) thỏa mãn.
    """
    pass

# Bài tập 5: In call stack
def print_call_stack():
    """In ra toàn bộ call stack hiện tại."""
    pass

def outer():
    middle()

def middle():
    inner()

def inner():
    print_call_stack()