import time
import sqlite3
import threading
import os

# Ví dụ 1: Đo thời gian thực thi

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        print(f'Thời gian thực thi: {self.end - self.start:.4f} giây')
        # Không xử lý lỗi, để lỗi lan ra nếu có
        return False

print("=== Ví dụ 1: Đo thời gian ===")
with Timer():
    time.sleep(1)


# Ví dụ 2: Quản lý kết nối cơ sở dữ liệu
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f'Kết nối đến cơ sở dữ liệu: {self.db_name}')
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.connection:
            self.connection.close()
            print(f'Đã đóng kết nối: {self.db_name}')
        
        if exc_type is not None:
            print(f'Lỗi xảy ra trong khối with: {exc_value}')
        # Không chặn ngoại lệ
        return False

print("\n=== Ví dụ 2: Quản lý kết nối CSDL ===")
try:
    with DatabaseConnection(':memory:') as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE test (id INTEGER)')
        cursor.execute('INSERT INTO test VALUES (1)')
        conn.commit()
except Exception as e:
    print(f'Lỗi: {e}')


# Ví dụ 3: Quản lý khóa trong môi trường đa luồng
class ManagedLock:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        print('Đang chờ khóa...')
        self.lock.acquire()
        print('Đã có khóa')
        return self.lock

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Đang giải phóng khóa')
        self.lock.release()
        return False

print("\n=== Ví dụ 3: Quản lý khóa ===")
lock = ManagedLock()
with lock:
    print('Đang xử lý trong khu vực an toàn...')
print('Ra khỏi khu vực an toàn')
