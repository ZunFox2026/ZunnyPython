import inspect

# Bài 1: Viết hàm in thông tin chi tiết về một hàm
def print_function_info(func):
    """In ra tên, docstring, các tham số, kiểu dữ liệu, giá trị mặc định của hàm."""
    # TODO: Hoàn thành hàm này
    pass

# Bài 2: Viết decorator kiểm tra kiểu dữ liệu
def validate_types(func):
    """Decorator kiểm tra kiểu dữ liệu tham số dựa trên type hints."""
    # TODO: Hoàn thành decorator này
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Bài 3: Tìm các hàm test trong một module
def find_test_functions(module):
    """Tìm tất cả các hàm trong module có tên bắt đầu bằng 'test_' và trả về danh sách tên."""
    # TODO: Hoàn thành hàm này
    pass

# Bài 4: Liệt kê phương thức công khai của lớp
def list_public_methods(cls):
    """Trả về danh sách tên các phương thức công khai của lớp (không bắt đầu bằng '_')."""
    # TODO: Hoàn thành hàm này
    pass

# Bài 5: Decorator ghi log vào file
def log_call(func):
    """Decorator ghi tên hàm, tham số, và kết quả vào file 'function_calls.log'."""
    # TODO: Hoàn thành decorator này
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper