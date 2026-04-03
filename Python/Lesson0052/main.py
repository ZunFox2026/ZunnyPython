class PositiveNumber:
    """Descriptor đảm bảo giá trị là số và lớn hơn 0"""
    def __init__(self, name):
        self.name = name  # tên thuộc tính (dùng để lưu trong instance)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} phải là số")
        if value <= 0:
            raise ValueError(f"{self.name} phải lớn hơn 0")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]


class Person:
    age = PositiveNumber('age')
    height = PositiveNumber('height')  # chiều cao tính bằng mét

    def __init__(self, age, height):
        self.age = age
        self.height = height

# --- Ví dụ 1: Kiểm tra số dương ---
print("=== Ví dụ 1: PositiveNumber Descriptor ===")
person1 = Person(25, 1.75)
print(f"Tuổi: {person1.age}, Chiều cao: {person1.height}")

# Thử gán giá trị không hợp lệ
try:
    person1.age = -5
except ValueError as e:
    print(f"Lỗi: {e}")


# --- Ví dụ 2: Kiểm tra kiểu dữ liệu ---
class Typed:
    """Descriptor yêu cầu giá trị phải có kiểu cụ thể"""
    def __init__(self, expected_type, name=None):
        self.expected_type = expected_type
        self.name = name

    def __set_name__(self, owner, name):
        # Được gọi tự động nếu Python >= 3.6, giúp tự động đặt tên
        if self.name is None:
            self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} phải là {self.expected_type.__name__}")
        instance.__dict__[self.name] = value


class Product:
    name = Typed(str)
    price = Typed(float)
    in_stock = Typed(bool)

    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock

print("\n=== Ví dụ 2: Typed Descriptor ===")
product = Product("Laptop", 1200.0, True)
print(f"Sản phẩm: {product.name}, Giá: {product.price}, Còn hàng: {product.in_stock}")

try:
    product.price = "không hợp lệ"
except TypeError as e:
    print(f"Lỗi: {e}")


# --- Ví dụ 3: Descriptor với ghi log truy cập ---
import logging
logging.basicConfig(level=logging.INFO)

class LoggedAccess:
    """Ghi log mỗi khi truy cập hoặc thay đổi giá trị"""
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.name)
        logging.info(f"Đọc {self.name} = {value}")
        return value

    def __set__(self, instance, value):
        logging.info(f"Gán {self.name} = {value}")
        instance.__dict__[self.name] = value


class BankAccount:
    balance = LoggedAccess()

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Số dư không đủ")
        self.balance -= amount

print("\n=== Ví dụ 3: LoggedAccess Descriptor ===")
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
