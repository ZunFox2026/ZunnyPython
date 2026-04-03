import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def _private_method(self):
        return "Phương thức riêng tư"

###############
# Bài tập 1 #
###############
def safe_getattr(obj, attr, default=None, allow_private=False):
    """
    Viết hàm an toàn để lấy thuộc tính từ đối tượng.
    - Nếu thuộc tính không tồn tại, trả về default.
    - Nếu allow_private=False, không cho phép truy cập thuộc tính bắt đầu bằng _.
    """
    # Kiểm tra nếu tên thuộc tính là private
    if not allow_private and attr.startswith('_'):
        return default
    
    # Sử dụng getattr với default
    return getattr(obj, attr, default)

###############
# Bài tập 2 #
###############
def list_methods(obj):
    """
    Trả về danh sách tên các phương thức công khai (không bắt đầu bằng _) của đối tượng.
    """
    methods = []
    for name in dir(obj):
        # Bỏ qua tên bắt đầu bằng _
        if name.startswith('_'):
            continue
        attr = getattr(obj, name)
        if callable(attr):
            methods.append(name)
    return methods

###############
# Bài tập 3 #
###############
class PluginManager:
    """
    Quản lý các plugin (lớp xử lý) được đăng ký theo tên.
    Yêu cầu:
    - register_plugin(name, plugin_class): đăng ký lớp plugin
    - create_and_run(name, *args, **kwargs): tạo đối tượng và gọi run()
    """
    def __init__(self):
        self.plugins = {}
    
    def register_plugin(self, name, plugin_class):
        """Đăng ký plugin theo tên"""
        self.plugins[name] = plugin_class
    
    def create_and_run(self, name, *args, **kwargs):
        """Tạo đối tượng plugin và gọi phương thức run"""
        if name not in self.plugins:
            raise ValueError(f"Không tìm thấy plugin: {name}")
        
        plugin_class = self.plugins[name]
        instance = plugin_class(*args, **kwargs)
        
        # Kiểm tra và gọi run() nếu tồn tại
        if hasattr(instance, 'run') and callable(getattr(instance, 'run')):
            return instance.run()
        else:
            raise AttributeError(f"Plugin {name} không có phương thức run()")

# Ví dụ sử dụng PluginManager
class HelloPlugin:
    def __init__(self, message="Xin chào"):
        self.message = message
    
    def run(self):
        return self.message

class AddPlugin:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def run(self):
        return self.a + self.b

###############
# Bài tập 4 #
###############
def is_subclass(obj, base_class):
    """
    Kiểm tra xem obj (có thể là lớp hoặc đối tượng) có kế thừa từ base_class không.
    """
    # Nếu obj là đối tượng, lấy lớp của nó
    if not isinstance(obj, type):  # không phải kiểu class
        obj = obj.__class__
    
    # Kiểm tra kế thừa
    return issubclass(obj, base_class)

###############
# Bài tập 5 #
###############
def dump_object_info(obj):
    """
    In ra thông tin chi tiết về một đối tượng:
    - Loại
    - Các thuộc tính (không phải hàm, không private)
    - Các phương thức công khai
    """
    print(f"Loại đối tượng: {type(obj).__name__}")
    
    print("\nThuộc tính:")
    for name in dir(obj):
        if name.startswith('_'):
            continue
        value = getattr(obj, name)
        if not callable(value):
            print(f"  {name}: {value}")
    
    print("\nPhương thức công khai:")
    for name in dir(obj):
        if name.startswith('_'):
            continue
        value = getattr(obj, name)
        if callable(value):
            print(f"  {name}")

# --- Kiểm thử các bài tập ---
if __name__ == "__main__":
    p = Person("Alice", 30)
    
    print("Bài tập 1:", safe_getattr(p, "name"))
    print("Bài tập 1 (không tồn tại):", safe_getattr(p, "height", "Không biết"))
    
    print("\nBài tập 2:", list_methods(p))
    
    print("\nBài tập 3:")
    pm = PluginManager()
    pm.register_plugin("hello", HelloPlugin)
    pm.register_plugin("add", AddPlugin)
    print(pm.create_and_run("hello", message="Chào bạn!"))
    print(pm.create_and_run("add", 5, 3))
    
    print("\nBài tập 4:", is_subclass(p, Person))
    print("Bài tập 4 (list):", is_subclass([], list))
    
    print("\nBài tập 5:")
    dump_object_info(p)