### Ví dụ 1: Đăng ký tự động các lớp con
class PluginMeta(type):
    plugins = []  # Danh sách lưu các lớp plugin

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        # Chỉ đăng ký nếu không phải lớp cơ sở trừu tượng (giả sử không có thuộc tính abstract)
        if not attrs.get('abstract', False):
            cls.plugins.append(new_class)
        return new_class

class PluginBase(metaclass=PluginMeta):
    abstract = True  # Đánh dấu lớp cơ sở là trừu tượng

    def run(self):
        raise NotImplementedError

class EmailPlugin(PluginBase):
    def run(self):
        print("Gửi email...")

class SMSPlugin(PluginBase):
    def run(self):
        print("Gửi tin nhắn SMS...")

# Kiểm tra danh sách plugin đã được đăng ký
print("Các plugin đã đăng ký:")
for plugin in PluginMeta.plugins:
    print(f"- {plugin.__name__}")


### Ví dụ 2: Kiểm tra bắt buộc phương thức
class ProcessRequiredMeta(type):
    def __new__(cls, name, bases, attrs):
        # Bỏ qua kiểm tra cho lớp cơ sở trừu tượng
        if 'abstract' in attrs and attrs['abstract']:
            return super().__new__(cls, name, bases, attrs)
        
        # Kiểm tra xem có phương thức 'process' không
        if 'process' not in attrs:
            raise TypeError(f"Lớp {name} phải định nghĩa phương thức 'process()'!")
        
        # Kiểm tra process có phải là hàm không
        if not callable(attrs['process']):
            raise TypeError(f"'process' trong lớp {name} phải là một phương thức!")
            
        return super().__new__(cls, name, bases, attrs)

class TaskBase(metaclass=ProcessRequiredMeta):
    abstract = True

class DownloadTask(TaskBase):
    def process(self):
        print("Đang tải file...")

class ConvertTask(TaskBase):
    def process(self):
        print("Đang chuyển đổi định dạng...")

# Sẽ chạy OK
download = DownloadTask()
download.process()


### Ví dụ 3: Tự động thêm phương thức to_dict
class AutoToDictMeta(type):
    def __new__(cls, name, bases, attrs):
        # Thêm phương thức to_dict nếu chưa có
        if 'to_dict' not in attrs:
            def to_dict(self):
                return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            attrs['to_dict'] = to_dict

        return super().__new__(cls, name, bases, attrs)

class Person(metaclass=AutoToDictMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print("Thông tin người dùng:", p.to_dict())  # {'name': 'Alice', 'age': 30}
