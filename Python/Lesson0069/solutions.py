from contextlib import contextmanager
import os
import time

# Bài tập 1: Viết Context Manager để đếm thời gian thực thi
class ExecutionTimer:
    def __enter__(self):
        self.start = time.time()
        print("Bắt đầu thực thi...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        duration = time.time() - self.start
        print(f"Kết thúc thực thi. Thời gian: {duration:.4f} giây")
        return False  # Không xử lý lỗi


# Bài tập 2: Tạo Context Manager quản lý tệp tạm thời
class TemporaryFileManager:
    def __enter__(self):
        # Tạo tệp tạm và trả về đường dẫn
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
        self.path = self.temp_file.name
        print(f"Tạo tệp tạm: {self.path}")
        self.temp_file.close()  # Đóng để nơi khác có thể mở
        return self.path

    def __exit__(self, exc_type, exc_value, traceback):
        # Xóa tệp tạm khi thoát
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f"Đã xóa tệp tạm: {self.path}")


# Bài tập 3: Viết Context Manager để bắt và ghi log lỗi vào file
class ErrorLogger:
    def __init__(self, log_file="error.log"):
        self.log_file = log_file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"Lỗi: {exc_type.__name__}: {exc_value}\n")
            print(f"Lỗi đã được ghi vào {self.log_file}")
        return False  # Không xử lý lỗi, để ném ra ngoài nếu cần


# Bài tập 4: Tạo Context Manager để tạm thời thay đổi biến môi trường
class EnvVarManager:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.old_value = None

    def __enter__(self):
        # Lưu giá trị cũ nếu tồn tại
        self.old_value = os.environ.get(self.key)
        os.environ[self.key] = self.value
        print(f"Đặt biến môi trường: {self.key}={self.value}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Khôi phục giá trị cũ
        if self.old_value is None:
            os.environ.pop(self.key, None)
        else:
            os.environ[self.key] = self.old_value
        print(f"Khôi phục biến môi trường: {self.key}")


# Bài tập 5: Viết Context Manager in thông báo và đếm số lần sử dụng
class CountedContext:
    count = 0

    def __enter__(self):
        CountedContext.count += 1
        print(f"Bắt đầu Context lần thứ {CountedContext.count}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Kết thúc Context. Tổng số lần sử dụng: {CountedContext.count}")