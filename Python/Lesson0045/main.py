import time
import json
import os
from contextlib import contextmanager

# =======================
# Ví dụ 1: Đo thời gian thực thi
# =======================

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Bắt đầu đo thời gian...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed = end_time - self.start_time
        print(f"Kết thúc đo. Thời gian thực thi: {elapsed:.4f} giây")
        # Không kìm nén ngoại lệ
        return False

# Sử dụng Timer
print("=== Ví dụ 1: Đo thời gian ===")
with Timer() as t:
    time.sleep(1)
    print("Đang thực hiện một tác vụ...")

# =======================
# Ví dụ 2: Quản lý kết nối CSDL giả lập
# =======================

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Kết nối đến cơ sở dữ liệu {self.db_name}...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connected:
            print(f"Đóng kết nối đến {self.db_name}")
            self.connected = False

        if exc_type is not None:
            print(f"Lỗi xảy ra: {exc_value}")
        return False  # Không xử lý ngoại lệ

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Chưa kết nối đến CSDL")
        print(f"Thực hiện truy vấn: {sql}")

print("\n=== Ví dụ 2: Quản lý kết nối CSDL ===")
with DatabaseConnection("myapp_db") as db:
    db.query("SELECT * FROM users")
    # Tự động đóng khi kết thúc khối

# =======================
# Ví dụ 3: Thay đổi thư mục làm việc tạm thời
# =======================

@contextmanager
def temporary_cwd(path):
    old_cwd = os.getcwd()
    try:
        os.chdir(path)
        print(f"Đã chuyển đến thư mục: {path}")
        yield  # Trả quyền điều khiển cho khối with
    finally:
        os.chdir(old_cwd)
        print(f"Đã quay lại thư mục gốc: {old_cwd}")

print("\n=== Ví dụ 3: Thay đổi thư mục tạm thời ===")
print(f"Thư mục hiện tại ban đầu: {os.getcwd()}")
try:
    with temporary_cwd("/"):
        print(f"Thư mục hiện tại trong khối: {os.getcwd()}")
except FileNotFoundError:
    print("Không tìm thấy thư mục chỉ định.")
print(f"Thư mục hiện tại sau khối: {os.getcwd()}")