import time
import functools

# --- Bài 1: Ghi log khi gọi hàm ---
@functools.lru_cache  # Dùng để cache kết quả của hàm hashable

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # In ra thông tin khi gọi hàm
        print(f"[LOG] Gọi hàm: {func.__name__}")
        print(f"[LOG] Tham số: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Kết quả: {result}\n")
        return result
    return wrapper

# --- Bài 2: Thử lại hàm nếu gặp lỗi tối đa 3 lần ---
def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_retries = 3
        for i in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Lỗi lần {i+1}: {e}")
                if i == max_retries - 1:
                    print("Đã thử 3 lần, không thành công.")
                    raise  # Ném lại lỗi cuối cùng
                time.sleep(0.1)  # Chờ 0.1 giây trước khi thử lại
    return wrapper

# --- Bài 3: Cache kết quả hàm theo tham số ---
def cache(func):
    saved_results = {}  # Lưu kết quả dưới dạng (args, kwargs) -> kết quả

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo khóa từ args và kwargs (chỉ dùng khi có thể hash)
        key = str(args) + str(sorted(kwargs.items()))
        if key in saved_results:
            print(f"[CACHE] Trả về kết quả đã lưu cho {func.__name__}")
            return saved_results[key]
        
        result = func(*args, **kwargs)
        saved_results[key] = result
        print(f"[CACHE] Lưu kết quả mới cho {func.__name__}")
        return result
    return wrapper

# --- Bài 4: Đo thời gian, chỉ in nếu > 1 giây ---
def timing_smart(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        if elapsed > 1:
            print(f"[TIME] Hàm '{func.__name__}' thực thi lâu: {elapsed:.4f} giây")
        return result
    return wrapper

# --- Bài 5: Đảm bảo tất cả tham số là số dương ---
def ensure_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Kiểm tra tham số trong args
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Tham số {arg} không phải số dương")
        
        # Kiểm tra tham số trong kwargs
        for k, v in kwargs.items():
            if isinstance(v, (int, float)) and v <= 0:
                raise ValueError(f"Tham số {k}={v} không phải số dương")
        
        return func(*args, **kwargs)
    return wrapper

# === Ví dụ sử dụng các decorator ===
@log_calls
def nhan(a, b):
    return a * b

@retry
def chia_ngau_nhien():
    import random
    x = random.randint(0, 3)
    if x == 0:
        raise RuntimeError("Lỗi mạng")
    return "Thành công"

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@timing_smart
def chay_cham():
    time.sleep(1.5)
    return "Xong"

@ensure_positive
def tinh_dien_tich(h, w):
    return h * w

# --- Chạy thử nghiệm ---
if __name__ == "__main__":
    print("=== Bài 1: log_calls ===")
    nhan(5, 7)
    
    print("\n=== Bài 2: retry ===")
    try:
        print(chia_ngau_nhien())
    except:
        print("Thất bại sau 3 lần thử\n")
    
    print("\n=== Bài 3: cache ===")
    print(fibonacci(5))
    print(fibonacci(5))  # Sẽ dùng kết quả đã lưu
    
    print("\n=== Bài 4: timing_smart ===")
    chay_cham()
    
    print("\n=== Bài 5: ensure_positive ===")
    print(tinh_dien_tich(3, 4))
    try:
        tinh_dien_tich(-1, 5)
    except ValueError as e:
        print(f"Lỗi: {e}")