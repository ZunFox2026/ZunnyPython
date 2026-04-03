import inspect

def print_class_info(cls):
    """
    Bài tập 1: In ra tất cả phương thức và thuộc tính của một lớp.
    Gợi ý: Dùng inspect.getmembers và phân loại bằng inspect.isfunction, inspect.isroutine...
    """
    pass

def log_call(func):
    """
    Bài tập 2: Viết decorator @log_call ghi lại:
    - Tên hàm
    - Tham số đầu vào
    - Nơi gọi (file, dòng)
    """
    pass

def find_functions_by_doc_keyword(module, keyword):
    """
    Bài tập 3: Tìm các hàm trong module có từ khóa trong docstring.
    Gợi ý: Dùng inspect.getmembers để lấy hàm, sau đó kiểm tra docstring.
    """
    pass

def validate_types(func):
    """
    Bài tập 4: Viết decorator kiểm tra kiểu tham số dựa trên type hints.
    Nếu kiểu không khớp, in cảnh báo (hoặc raise exception).
    Gợi ý: Dùng inspect.signature và type checking.
    """
    pass

def get_caller_info():
    """
    Bài tập 5: Trả về tên hàm và dòng mã của nơi gọi.
    Trả về dạng tuple: (function_name, line_number, filename)
    """
    pass