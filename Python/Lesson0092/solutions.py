from functools import wraps
import time

# --- BÀI 1: Decorator @repeat(n) ---
def repeat(n):
    """
    Gọi hàm lặp lại n lần và trả về danh sách kết quả.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Xin chào!")
    return "OK"


# --- BÀI 2: Class decorator @TimeIt ---
class TimeIt:
    """
    In ra thời gian thực thi mỗi lần gọi hàm.
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        duration = time.time() - start
        print(f"[TimeIt] {self.func.__name__} mất {duration:.4f}s")
        return result

@TimeIt
def tinh_toan(n):
    return sum(i * i for i in range(n))


# --- BÀI 3: Decorator @only_allow_types ---
def only_allow_types(*allowed_types):
    """
    Kiểm tra kiểu dữ liệu của các đối số.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Kiểm tra các đối số vị trí
            for i, (arg, expected_type) in enumerate(zip(args, allowed_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Đối số {i+1}: mong là {expected_type}, nhận {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@only_allow_types(int, int)
def cong(a, b):
    return a + b


# --- BÀI 4: Decorator @cache_method ---
def cache_method(func):
    """
    Cache kết quả của phương thức dựa trên tham số đầu vào.
    """
    cache_name = f"_cache_{func.__name__}"

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Tạo khóa từ tham số
        cache_key = str(args) + str(sorted(kwargs.items()))

        # Tạo cache nếu chưa có
        if not hasattr(self, cache_name):
            setattr(self, cache_name, {})
        cache = getattr(self, cache_name)

        if cache_key not in cache:
            cache[cache_key] = func(self, *args, **kwargs)
        return cache[cache_key]

    return wrapper


class MayTinh:
    @cache_method
    def fibonacci(self, n):
        if n < 2:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


# --- BÀI 5: Decorator @ensure_result ---
def ensure_result(condition):
    """
    Kiểm tra kết quả trả về có thỏa điều kiện.
    condition: hàm nhận kết quả và trả về True/False
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not condition(result):
                raise ValueError(f"Kết quả {result} không thỏa điều kiện")
            return result
        return wrapper
    return decorator

@ensure_result(lambda x: x > 0)
def nghich_dao(a):
    return 1 / a if a != 0 else 0


# --- CHẠY CÁC BÀI TẬP ĐỂ KIỂM TRA ---
if __name__ == "__main__":
    print("=== Bài 1: repeat ===")
    print(hello())

    print("\n=== Bài 2: TimeIt ===")
    print(tinh_toan(10000))

    print("\n=== Bài 3: only_allow_types ===")
    print(cong(5, 3))
    try:
        cong(5, "3")
    except TypeError as e:
        print("Lỗi kiểu:", e)

    print("\n=== Bài 4: cache_method ===")
    mt = MayTinh()
    print(mt.fibonacci(10))
    print(mt.fibonacci(10))  # Gọi lại, phải nhanh hơn

    print("\n=== Bài 5: ensure_result ===")
    print(nghich_dao(2))
    try:
        nghich_dao(-1)
    except ValueError as e:
        print("Lỗi kết quả:", e)