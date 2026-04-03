import time
import functools

# Ví dụ 1: Decorator ghi log thời gian thực thi
def time_logger(func):
    @functools.wraps(func)  # Giữ nguyên tên và docstring của hàm gốc
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

# Áp dụng decorator
@time_logger
def calculate_sum(n):
    """Tính tổng từ 1 đến n"""
    return sum(range(1, n + 1))

# Ví dụ 2: Decorator kiểm tra kiểu dữ liệu đầu vào
def type_check(expected_types):
    """
    Kiểm tra kiểu dữ liệu của các tham số đầu vào.
    expected_types: tuple hoặc list chứa các kiểu mong đợi cho từng tham số.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Kiểm tra positional arguments
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Đối số thứ {i+1} phải là {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check((int, str))
def greet_user(age, name):
    print(f"Xin chào {name}, bạn {age} tuổi.")

# Ví dụ 3: Decorator đếm số lần gọi hàm
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Hàm '{func.__name__}' đã được gọi {wrapper.call_count} lần")
        return func(*args, **kwargs)
    wrapper.call_count = 0  # Biến đếm nằm trong hàm wrapper
    return wrapper

@count_calls
def say_hello():
    print("Xin chào!")

# Chạy các ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Đo thời gian thực thi ===")
    total = calculate_sum(100000)
    print(f"Tổng: {total}\n")

    print("=== Ví dụ 2: Kiểm tra kiểu dữ liệu ===")
    greet_user(25, "Minh")  # Hợp lệ
    # greet_user("25", "Minh")  # Sẽ báo lỗi
    print()

    print("=== Ví dụ 3: Đếm số lần gọi hàm ===")
    say_hello()
    say_hello()
    say_hello()
    print(f"Tổng cộng gọi {say_hello.call_count} lần\n")