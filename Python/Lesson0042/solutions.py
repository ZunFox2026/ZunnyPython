import inspect

def print_object_info(obj):
    """In thông tin chi tiết về đối tượng"""
    print(f"Đối tượng: {obj.__class__.__name__}")
    print("Thuộc tính:")
    for attr_name in dir(obj):
        # Bỏ qua thuộc tính nội bộ và phương thức
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)
            if not callable(attr_value):
                print(f"  {attr_name}: {attr_value}")


class CommandRunner:
    def __init__(self):
        self.state = "stopped"

    def start(self):
        if self.state == "stopped":
            self.state = "running"
            print("Đã khởi động.")
        else:
            print("Đã đang chạy.")

    def stop(self):
        if self.state == "running":
            self.state = "stopped"
            print("Đã dừng.")
        else:
            print("Đã dừng rồi.")

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        print(f"Trạng thái: {self.state}")

    def run(self, command_name):
        """Gọi phương thức từ tên chuỗi"""
        if hasattr(self, command_name):
            method = getattr(self, command_name)
            if callable(method):
                method()  # Gọi phương thức không có tham số
            else:
                print(f"{command_name} không phải là phương thức.")
        else:
            print(f"Lệnh '{command_name}' không tồn tại.")


def log_call():
    """In ra tên hàm và tham số của hàm đang gọi"""
    # Lấy thông tin từ stack: [1] là hàm gọi log_call
    caller_frame = inspect.stack()[1]
    func_name = caller_frame.function
    filename = caller_frame.filename
    line_no = caller_frame.lineno
    
    # Lấy thông tin tham số
    code = caller_frame.frame.f_code
    arg_count = code.co_argcount
    arg_names = code.co_varnames[:arg_count]
    local_vars = caller_frame.frame.f_locals
    
    args_str = ", ".join([f"{name}={local_vars[name]}" for name in arg_names])
    
    print(f"[LOG] Gọi {func_name}({args_str}) tại {filename}:{line_no}")


def serialize_object(obj):
    """Chuyển đổi object thành dict chỉ chứa thuộc tính dữ liệu"""
    result = {}
    for attr_name in dir(obj):
        if not attr_name.startswith('_'):
            attr_value = getattr(obj, attr_name)
            if not callable(attr_value):
                result[attr_name] = attr_value
    return result


def check_required_params(func):
    """Trả về danh sách các tham số bắt buộc của hàm"""
    sig = inspect.signature(func)
    required_params = []
    for name, param in sig.parameters.items():
        if param.default == inspect.Parameter.empty:
            required_params.append(name)
    return required_params