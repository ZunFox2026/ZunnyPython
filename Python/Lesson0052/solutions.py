#################
# LỜI GIẢI BÀI TẬP
#################

class EmailDescriptor:
    """
    Descriptor kiểm tra định dạng email đơn giản.
    Yêu cầu: phải chứa '@' và kết thúc bằng '.com', '.org', hoặc '.edu'
    """
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Kiểm tra định dạng email đơn giản
        if '@' not in value:
            raise ValueError(f"{self.name} phải chứa '@'")
        if not value.endswith(('.com', '.org', '.edu')):
            raise ValueError(f"{self.name} phải kết thúc bằng .com, .org hoặc .edu")
        instance.__dict__[self.name] = value


class ChoicesDescriptor:
    """
    Descriptor chỉ chấp nhận giá trị nằm trong danh sách choices.
    """
    def __init__(self, choices, name=None):
        self.choices = choices
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value not in self.choices:
            raise ValueError(f"{self.name} phải là một trong: {self.choices}")
        instance.__dict__[self.name] = value


class EncryptedDescriptor:
    """
    Descriptor tự động mã hóa/giải mã giá trị.
    Sử dụng mã hóa XOR đơn giản với một key cố định.
    """
    def __init__(self, key=42, name=None):
        self.key = key
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        encrypted = instance.__dict__.get(self.name)
        if encrypted is None:
            return None
        # Giải mã bằng XOR
        decrypted = ''.join(chr(b ^ self.key) for b in encrypted)
        return decrypted

    def __set__(self, instance, value):
        # Mã hóa giá trị thành chuỗi byte đã XOR
        encrypted = bytes(ord(c) ^ self.key for c in value)
        instance.__dict__[self.name] = encrypted

class User:
    # Áp dụng các descriptor đã triển khai
    email = EmailDescriptor()
    status = ChoicesDescriptor(['active', 'inactive', 'pending'])
    password = EncryptedDescriptor()

    def __init__(self, email, status, password):
        self.email = email
        self.status = status
        self.password = password

# --- Kiểm thử lời giải ---
if __name__ == "__main__":
    print("\n=== Kiểm thử lời giải bài tập ===")
    
    user = User("alice@company.com", "active", "mật_khẩu_bí_mật")
    print(f"Email: {user.email}")
    print(f"Trạng thái: {user.status}")
    print(f"Mật khẩu (giải mã): {user.password}")
    
    # Kiểm tra lỗi
    try:
        user.email = "sai_email"
    except ValueError as e:
        print(f"Lỗi email: {e}")
    
    try:
        user.status = "unknown"
    except ValueError as e:
        print(f"Lỗi trạng thái: {e}")