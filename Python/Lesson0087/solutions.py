import inspect

def exercise1():
    """
    Bài tập 1: In ra các phương thức công khai và docstring của chúng.
    """
    # Lấy tất cả các thành viên là hàm trong global
    functions = inspect.getmembers(globals(), predicate=inspect.isfunction)
    print("Các hàm công khai trong module:")
    for name, func in functions:
        if not name.startswith("_"):  # Bỏ qua hàm private
            doc = func.__doc__ or "Không có mô tả"
            print(f"- {name}: {doc}")


class MathUtils:
    """Công cụ toán học đơn giản"""
    
    def square(self, x):
        """Trả về bình phương của x"""
        return x ** 2
    
    def _private_helper(self):
        """Hàm helper không công khai"""
        return "private"
    
    def cube(self, x):
        """Trả về lập phương của x"""
        return x ** 3


def exercise2(obj):
    """
    Bài tập 2: Kiểm tra phương thức 'square' có tham số 'x' không.
    """
    if hasattr(obj, 'square'):
        method = getattr(obj, 'square')
        sig = inspect.signature(method)
        if 'x' in sig.parameters:
            print("Phương thức 'square' có tham số 'x'")
        else:
            print("Phương thức 'square' KHÔNG có tham số 'x'")
    else:
        print("Đối tượng không có phương thức 'square'")


def exercise3(frame_depth=1):
    """
    Bài tập 3: In ra call stack từ hiện tại trở lên.
    """
    stack = inspect.stack()
    print("Call stack:")
    # Bắt đầu từ frame_depth để bỏ qua các frame không cần thiết
    for frame_info in stack[frame_depth:]:
        filename = frame_info.filename.split("/")[-1]  # Lấy tên file ngắn
        lineno = frame_info.lineno
        function_name = frame_info.function
        print(f"  File \"{filename}\", line {lineno}, in {function_name}")


def outer():
    middle()

def middle():
    inner()

def inner():
    exercise3(frame_depth=3)

# Kiểm tra lời giải
# exercise1()
# calc = MathUtils()
# exercise2(calc)
# inner()