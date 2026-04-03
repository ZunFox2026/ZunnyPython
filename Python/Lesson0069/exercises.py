from contextlib import contextmanager
import os
import tempfile

# Bài tập 1: Viết Context Manager để đếm thời gian thực thi
class ExecutionTimer:
    # TODO: Triển khai __enter__ và __exit__ để đo thời gian
    pass

# Bài tập 2: Tạo Context Manager quản lý tệp tạm thời
class TemporaryFileManager:
    # TODO: Triển khai để tạo tệp tạm, trả về đường dẫn, và xóa khi thoát
    pass

# Bài tập 3: Viết Context Manager để bắt và ghi log lỗi vào file
class ErrorLogger:
    def __init__(self, log_file="error.log"):
        self.log_file = log_file
    # TODO: Ghi lỗi vào file nếu có

# Bài tập 4: Tạo Context Manager để tạm thời thay đổi biến môi trường
class EnvVarManager:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.old_value = None
    # TODO: Lưu giá trị cũ, thiết lập mới, khôi phục khi thoát

# Bài tập 5: Viết Context Manager in thông báo và đếm số lần sử dụng
class CountedContext:
    count = 0
    # TODO: Tăng biến count mỗi lần dùng, in số lần
    pass