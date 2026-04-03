import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1
        return f"{self.name} vừa tròn {self.age} tuổi!"

    def _private_method(self):
        return "Phương thức riêng tư"

# Ví dụ 1: Tự động gọi phương thức qua tên chuỗi
def call_method_by_name(obj, method_name):
    """
    Gọi phương thức của đối tượng dựa trên tên chuỗi.
    Nếu không tồn tại, trả về thông báo.
    """
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method()
        else:
            return f"{method_name} không phải là phương thức, giá trị: {method}"
    else:
        return f"Đối tượng không có phương thức {method_name}"

print("=== Ví dụ 1: Gọi phương thức động ===")
person = Person("An", 20)
print(call_method_by_name(person, "greet"))
print(call_method_by_name(person, "have_birthday"))
print(call_method_by_name(person, "unknown_method"))

# Ví dụ 2: Tạo báo cáo chi tiết về lớp bằng inspect
def describe_class(cls):
    """
    In ra thông tin chi tiết về một lớp: tên, các phương thức, thuộc tính.
    """
    print(f"\n=== Mô tả lớp {cls.__name__} ===")
    methods = [name for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction)]
    attributes = [name for name, obj in inspect.getmembers(cls) if not callable(obj) and not name.startswith("__")]
    
    print(f"Các phương thức: {methods}")
    print(f"Các thuộc tính: {attributes}")
    
    # In signature của từng phương thức
    for name in methods:
        method = getattr(cls, name)
        sig = inspect.signature(method)
        print(f"  {name}{sig}")

describe_class(Person)

# Ví dụ 3: Ghi log tự động tên hàm và tham số sử dụng inspect
def debug_call():
    """
    Ghi log thông tin về hàm gọi nó: tên hàm, tham số, file, dòng.
    """
    frame = inspect.currentframe().f_back  # Lấy frame trước đó (hàm gọi)
    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_number = frame.f_lineno
    
    # Lấy tham số của hàm gọi
    args_info = inspect.getargvalues(frame)
    args_dict = {}
    for arg in args_info.args:
        args_dict[arg] = args_info.locals[arg]
    
    print(f"[DEBUG] Hàm '{func_name}' được gọi tại {filename}:{line_number}")
    print(f"[DEBUG] Tham số: {args_dict}")


def calculate_salary(base, bonus=0, tax_rate=0.1):
    debug_call()
    salary = (base + bonus) * (1 - tax_rate)
    return salary

print("\n=== Ví dụ 3: Ghi log tự động ===")
salary = calculate_salary(1000, bonus=200, tax_rate=0.15)
print(f"Lương thực nhận: {salary}")