from functools import lru_cache

# Bài tập 1: Viết hàm tính số Lucas thứ n
# Lucas(0) = 2, Lucas(1) = 1, Lucas(n) = Lucas(n-1) + Lucas(n-2)
# Yêu cầu: dùng @lru_cache để tối ưu
@lru_cache(maxsize=None)
def lucas(n):
    pass  # TODO: Viết mã

# Bài tập 2: Tính tổng dãy Fibonacci từ 1 đến n
# sum_fibonacci(n) = fibonacci(1) + fibonacci(2) + ... + fibonacci(n)
# Yêu cầu: tối ưu bằng @lru_cache
@lru_cache(maxsize=None)
def sum_fibonacci(n):
    pass  # TODO: Viết mã

# Bài tập 3: Kiểm tra số nguyên tố
# is_prime(n) trả về True nếu n là số nguyên tố
# Yêu cầu: dùng @lru_cache
@lru_cache(maxsize=None)
def is_prime(n):
    pass  # TODO: Viết mã

# Bài tập 4: Đếm số từ trong câu
# word_count(sentence)
# Gợi ý: chuỗi là hashable nên có thể dùng lru_cache
# Nhưng hãy cân nhắc: có thực sự cần thiết không?
@lru_cache(maxsize=128)
def word_count(sentence):
    pass  # TODO: Viết mã