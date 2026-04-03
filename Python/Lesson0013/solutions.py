import functools
import time

# Lời giải Bài tập 1: time_logger (đã làm trong ví dụ, nhưng đảm bảo đúng yêu cầu)
# Xem trong file main.py

# Lời giải Bài tập 2: Kiểm tra tham số là số dương
def ensure_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Kiểm tra các tham số trong args
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Giá trị {arg} không phải là số dương")
        # Kiểm tra các tham số trong kwargs
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(f"Tham số {key} = {value} không phải là số dương")
        return func(*args, **kwargs)
    return wrapper

@ensure_positive
def calculate_area(length, width):
    return length * width

# Lời giải Bài tập 3: Memoize - lưu kết quả để tránh tính lại
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo khóa từ args và kwargs (phải bất biến)
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Lời giải Bài tập 4: admin_required
def admin_required(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            raise PermissionError(f"Người dùng {user['name']} không có quyền truy cập")
        return func(user, *args, **kwargs)
    return wrapper

@admin_required
def delete_user(user, target_user_id):
    print(f"Người dùng {user['name']} đã xóa user có ID {target_user_id}")

# Lời giải Bài tập 5: retry
def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Lỗi lần {attempt}: {e}")
                    if attempt < max_attempts:
                        time.sleep(0.5)  # Chờ 0.5 giây trước khi thử lại
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Kết nối thất bại")
    print("Thành công!")

# Kiểm thử lời giải (bỏ comment để chạy)
if __name__ == "__main__":
    # Bài 2
    print("=== Bài 2: ensure_positive ===")
    print(calculate_area(5, 4))  # Hợp lệ
    # print(calculate_area(-5, 4))  # Sẽ lỗi
    print()

    # Bài 3
    print("=== Bài 3: memoize (fibonacci) ===")
    print(fibonacci(10))
    print(fibonacci(10))  # Lấy từ cache
    print()

    # Bài 4
    print("=== Bài 4: admin_required ===")
    admin_user = {'name': 'An', 'role': 'admin'}
    normal_user = {'name': 'Bình', 'role': 'user'}
    delete_user(admin_user, 123)  # Thành công
    # delete_user(normal_user, 456)  # Lỗi quyền
    print()

    # Bài 5
    print("=== Bài 5: retry ===")
    unreliable_function()