######################
# Bài tập 1
# Tạo context manager đếm số dòng trong file
class LineCounter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None
        self.line_count = 0

    def __enter__(self):
        # TODO: Mở file và chuẩn bị đếm
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # TODO: Đóng file và xử lý lỗi nếu cần
        pass

    def count_lines(self):
        # TODO: Đếm số dòng
        pass


######################
# Bài tập 2
# Context manager tạm thời đổi thư mục
class TemporaryDirectory:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.old_dir = None

    def __enter__(self):
        # TODO: Lưu thư mục hiện tại, chuyển đến new_dir
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # TODO: Quay lại thư mục cũ
        pass


######################
# Bài tập 3
# Context manager ghi log hành động
class ActionLogger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        # TODO: Ghi thời gian bắt đầu vào log
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # TODO: Ghi thời gian kết thúc, thông báo lỗi nếu có
        pass


######################
# Bài tập 4
# Sử dụng contextlib để tạo Timer
def timer_function():
    # TODO: Dùng @contextmanager để tạo generator-based Timer
    pass


######################
# Bài tập 5
# Context manager quản lý trạng thái LOGGING_ENABLED
LOGGING_ENABLED = True
class SilentMode:
    def __enter__(self):
        # TODO: Lưu trạng thái cũ, tắt logging
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # TODO: Khôi phục trạng thái cũ
        pass
