### Bài tập 1: Tạo context manager SuppressErrors
# Viết một context manager có thể bỏ qua các loại exception được chỉ định.
# Ví dụ: với ValueError, TypeError

class SuppressErrors:
    # Hoàn thành lớp này
    pass


### Bài tập 2: Timer ghi log vào file
# Viết context manager TimerLog ghi thời gian thực thi vào một file log.

class TimerLog:
    def __init__(self, log_file):
        # Khởi tạo với tên file log
        pass

    def __enter__(self):
        # Ghi thời gian bắt đầu và mở file
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # Tính thời gian, ghi vào file, đóng file
        pass


### Bài tập 3: ReadOnlyFile
# Tạo context manager mở file ở chế độ chỉ đọc, đảm bảo không bị ghi nhầm.

class ReadOnlyFile:
    def __init__(self, filename):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


### Bài tập 4: ChangeDir an toàn
# Viết context manager ChangeDir (dùng class) để thay đổi thư mục làm việc.
# Đảm bảo luôn quay lại thư mục ban đầu dù có lỗi.

class ChangeDir:
    def __init__(self, path):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


### Bài tập 5: In thông báo với @contextmanager
# Dùng @contextmanager để tạo context manager in ra:
# "Bắt đầu..." khi vào, "Kết thúc." khi ra.

# from contextlib import contextmanager

# @contextmanager
# def log_block(name):
#     pass