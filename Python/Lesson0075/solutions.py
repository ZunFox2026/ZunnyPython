import os
import time

################################################################################
# Bài tập 1: Viết Context Manager để tạm thời thay đổi thư mục làm việc

class TemporaryDirectory:
    def __init__(self, path):
        self.path = path
        self.original_dir = None

    def __enter__(self):
        self.original_dir = os.getcwd()  # Lưu thư mục hiện tại
        os.chdir(self.path)  # Chuyển đến thư mục mới
        print(f"Đã chuyển đến thư mục: {self.path}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)  # Quay lại thư mục ban đầu
        print(f"Đã quay lại thư mục: {self.original_dir}")


################################################################################
# Bài tập 2: Viết Context Manager để đếm số lượng dòng khi đọc file

class LineCountContext:
    def __init__(self, filename):
        self.filename = filename
        self.line_count = 0
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        # Đọc và đếm tất cả dòng
        lines = self.file.readlines()
        self.line_count = len(lines)
        # Quay lại đầu file để người dùng đọc tiếp
        self.file.seek(0)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(f"Đã đọc file '{self.filename}' với {self.line_count} dòng.")


################################################################################
# Bài tập 3: Viết Context Manager bắt lỗi và ghi log, không ngắt chương trình

class SafeExecution:
    def __init__(self, log_file="error.log"):
        self.log_file = log_file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Lỗi: {exc_type.__name__}: {exc_value}\n")
            print(f"Lỗi đã được ghi vào {self.log_file}")
            return True  # Ngăn không cho lỗi ném ra ngoài
        return False


################################################################################
# Bài tập 4: Viết Context Manager quản lý bộ nhớ đệm (cache) trong khối lệnh

class TemporaryCache:
    def __init__(self, cache_dict):
        self.cache_dict = cache_dict
        self.backup = None

    def __enter__(self):
        self.backup = dict(self.cache_dict)  # Sao lưu cache hiện tại
        return self.cache_dict

    def __exit__(self, exc_type, exc_value, traceback):
        # Khôi phục cache về trạng thái ban đầu
        self.cache_dict.clear()
        self.cache_dict.update(self.backup)
        print("Cache đã được khôi phục về trạng thái ban đầu.")


################################################################################
# Bài tập 5: In thông báo khi có ngoại lệ, nhưng cho phép chương trình tiếp tục

class NotifyOnError:
    def __enter__(self):
        print("Bắt đầu khối lệnh...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"⚠️ Cảnh báo: Có lỗi xảy ra: {exc_value}")
            print("Khối lệnh kết thúc với lỗi, nhưng chương trình vẫn tiếp tục.")
        else:
            print("✅ Khối lệnh kết thúc thành công.")
        return False  # Không bắt lỗi, để lỗi ném ra ngoài nếu cần