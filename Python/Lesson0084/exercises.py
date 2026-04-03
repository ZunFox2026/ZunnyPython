# Bài tập 1:
# Viết hàm analyze_class(cls) nhận vào một lớp và in ra:
# - Tên tất cả các phương thức
# - Chữ ký của từng phương thức
# - Ghi chú tài liệu (docstring) của lớp và từng phương thức

def analyze_class(cls):
    # Gợi ý: dùng inspect.getmembers, inspect.signature, và thuộc tính __doc__
    pass

# Bài tập 2:
# Viết hàm log_caller() in ra tên hàm đang gọi nó và tên hàm gọi hàm đó (stack)
# Sử dụng inspect.stack()

def log_caller():
    # Gợi ý: inspect.stack()[1] là hàm gọi hàm hiện tại
    pass

def test_log():
    log_caller()

# Bài tập 3:
# Viết hàm get_function_info(func) trả về một từ điển chứa:
# - Tên hàm
# - Docstring
# - Số lượng tham số
# - Có tham số *args hay không
# - Có tham số **kwargs hay không

def get_function_info(func):
    # Gợi ý: dùng inspect.signature và duyệt các tham số
    pass