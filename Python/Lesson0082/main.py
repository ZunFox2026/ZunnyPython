from contextlib import contextmanager
import time
import tempfile
import os

# ====================
# Ví dụ 1: Context Manager tự tạo để đo thời gian thực thi
# ====================
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Bắt đầu đo thời gian...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed = end_time - self.start_time
        print(f"Kết thúc. Thời gian thực thi: {elapsed:.4f} giây")
        # Không xử lý lỗi, để ngoại lệ lan ra ngoài nếu có
        return False

# Sử dụng Timer
print("=== Ví dụ 1: Đo thời gian ===")
with Timer():
    time.sleep(1)  # Giả lập công việc
    print("Đang xử lý...")


# ====================
# Ví dụ 2: Quản lý file tạm thời với lớp
# ====================
class TempFileManager:
    def __enter__(self):
        # Tạo file tạm
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        print(f"Tạo file tạm: {self.temp_file.name}")
        return self.temp_file

    def __exit__(self, exc_type, exc_value, traceback):
        self.temp_file.close()
        os.unlink(self.temp_file.name)  # Xóa file
        print(f"Đã xóa file tạm: {self.temp_file.name}")
        return False

print("\n=== Ví dụ 2: Quản lý file tạm ===")
with TempFileManager() as temp:
    temp.write("Dữ liệu tạm thời\n")
    temp.seek(0)
    print("Nội dung file tạm:", temp.read())
# File đã bị xóa sau khi ra khỏi khối with


# ====================
# Ví dụ 3: Dùng @contextmanager để quản lý kết nối cơ sở dữ liệu giả lập
# ====================
@contextmanager
def database_connection():
    print("Đang kết nối đến cơ sở dữ liệu...")
    conn = {"connected": True, "data": []}
    try:
        yield conn  # Trả về kết nối để sử dụng
    finally:
        print("Đóng kết nối cơ sở dữ liệu...")
        conn["connected"] = False

print("\n=== Ví dụ 3: Quản lý kết nối CSDL ===")
with database_connection() as db:
    print("Trạng thái kết nối:", db["connected"])
    db["data"].append("Dữ liệu 1")
    db["data"].append("Dữ liệu 2")
    print("Dữ liệu đã lưu:", db["data"])
# Kết nối được đóng tự động dù có lỗi hay không