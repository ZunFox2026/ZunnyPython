import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Xin chào, tôi là {self.name}")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} vừa tròn {self.age} tuổi!")

# --- Ví dụ 1: In tất cả thuộc tính của đối tượng ---
def print_object_attributes(obj):
    """In tất cả thuộc tính dữ liệu của đối tượng"""
    print(f"Thuộc tính của {obj.__class__.__name__}:")
    for attr_name in dir(obj):
        # Bỏ qua các phương thức và thuộc tính nội bộ
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)
            if not callable(attr_value):  # Không phải hàm
                print(f"  {attr_name}: {attr_value}")

# Tạo đối tượng và in thông tin
person = Person("Minh", 20)
print_object_attributes(person)

print("\n---\n")

# --- Ví dụ 2: Gọi phương thức từ tên chuỗi ---
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def power(self, base, exp):
        return base ** exp

# Giả lập người dùng nhập tên phương thức và tham số
def run_calculator_method(calc, method_name, *args):
    if hasattr(calc, method_name):
        method = getattr(calc, method_name)
        if callable(method):
            result = method(*args)
            print(f"Kết quả của {method_name}{args} = {result}")
            return result
        else:
            print("Đây không phải là phương thức.")
    else:
        print("Phương thức không tồn tại.")

# Sử dụng
calc = Calculator()
run_calculator_method(calc, "add", 5, 3)
run_calculator_method(calc, "power", 2, 10)

print("\n---\n")

# --- Ví dụ 3: Debug tự động in thông tin hàm đang gọi ---
def debug_call():
    """In ra thông tin về hàm gọi hiện tại"""
    # Lấy thông tin stack: [0] là hàm hiện tại, [1] là hàm gọi nó
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno
    print(f"[DEBUG] Hàm '{func_name}' được gọi tại {filename}:{line_no}")

    # In các biến cục bộ tại điểm gọi
    local_vars = frame.f_locals
    if local_vars:
        print("  Biến cục bộ:", local_vars)

    # Giải phóng bộ nhớ
    del frame

def problematic_function(x, y):
    debug_call()
    return x / y if y != 0 else 0

# Gọi thử
problematic_function(10, 2)

# In chữ ký của một hàm
print("\n--- Chữ ký hàm problematic_function ---")
sig = inspect.signature(problematic_function)
for param_name, param in sig.parameters.items():
    print(f"Tham số: {param_name}, Mặc định: {param.default}")