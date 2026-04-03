### Bài tập 1: Tạo decorator retry
# Viết một decorator @retry(max_attempts=3) để thử lại hàm nếu xảy ra ngoại lệ.
# Nếu vượt quá số lần thử, mới raise lỗi.

def retry(max_attempts=3):
    # Gợi ý: Tạo wrapper, dùng vòng lặp và try-except
    pass

### Bài tập 2: Tạo decorator only_admin
# Viết decorator @only_admin, kiểm tra tham số đầu tiên là user dict và role phải là 'admin'.
# Nếu không, in thông báo và không thực thi hàm.

def only_admin(func):
    # Gợi ý: Kiểm tra user['role']
    pass

### Bài tập 3: Tạo decorator cache_result
# Viết decorator @cache_result để lưu kết quả hàm theo tham số đầu vào.
# Nếu hàm được gọi lại với cùng tham số, trả về kết quả đã lưu.
# Gợi ý: Dùng dictionary để lưu (args, kwargs) -> result

def cache_result(func):
    # Gợi ý: Dùng tuple(args) và frozenset(kwargs.items()) làm key
    pass
