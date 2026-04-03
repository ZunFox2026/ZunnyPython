import inspect
import functools

def kiem_tra_tham_so_bat_buoc(func):
    """Trả về danh sách các tham số bắt buộc của hàm"""
    sig = inspect.signature(func)
    required_params = []
    for name, param in sig.parameters.items():
        # Tham số bắt buộc là tham số không có giá trị mặc định
        if param.default == inspect.Parameter.empty:
            required_params.append(name)
    return required_params

def bai_tap_1():
    def ham_mau(x, y, z=10):
        return x + y + z
    
    ket_qua = kiem_tra_tham_so_bat_buoc(ham_mau)
    print(f"[Bài 1] Tham số bắt buộc: {ket_qua}")  # Dự kiến: ['x', 'y']


def kiem_tra_kieu(func):
    """Decorator kiểm tra kiểu tham số dựa trên type hints"""
    sig = inspect.signature(func)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Gắn tham số vào chữ ký
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Kiểm tra từng tham số
        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            expected_type = param.annotation
            
            # Nếu có ghi chú kiểu và kiểu không khớp
            if expected_type != inspect.Parameter.empty and not isinstance(value, expected_type):
                print(f"[CẢNH BÁO] Tham số '{name}' của hàm '{func.__name__}' nên là {expected_type}, nhận {type(value)}")
        
        return func(*args, **kwargs)
    return wrapper

def bai_tap_2():
    @kiem_tra_kieu
    def ham_thu(x: int, y: str):
        return x * len(y)
    
    print("[Bài 2] Kiểm tra kiểu:")
    ham_thu(5, "abc")      # OK
    ham_thu("abc", 123)     # Cảnh báo


def liet_ke_lop_con(base_class, module):
    """Liệt kê các lớp con kế thừa từ base_class trong module"""
    subclasses = []
    # Duyệt qua tất cả các đối tượng trong module
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Kiểm tra lớp có kế thừa từ base_class và không phải chính base_class
        if issubclass(obj, base_class) and obj != base_class:
            subclasses.append(name)
    return subclasses

def bai_tap_3():
    # Tạo lớp mẫu để kiểm thử
    class DongVat:
        pass
    
    class Cho(DongVat):
        pass
    
    class Meo(DongVat):
        pass
    
    class Chim:
        pass  # Không kế thừa
    
    import sys
    ket_qua = liet_ke_lop_con(DongVat, sys.modules[__name__])
    print(f"[Bài 3] Các lớp con của DongVat: {ket_qua}")  # Dự kiến: ['Cho', 'Meo']


def ham_duoc_goi_truoc():
    """Trả về tên hàm đã gọi hàm hiện tại"""
    frame = inspect.currentframe()
    # Lấy frame của hàm gọi (f_back)
    caller_frame = frame.f_back.f_back  # f_back đầu tiên là của hàm gọi hàm này, f_back thứ hai là của hàm gọi hàm gọi
    
    if caller_frame is None:
        return "trực tiếp"
    
    return caller_frame.f_code.co_name

def ham_goi():
    return ham_duoc_goi_truoc()

def bai_tap_4():
    print(f"[Bài 4] Hàm được gọi trước: {ham_goi()}")  # Dự kiến: "ham_goi"
    print(f"[Bài 4] Gọi trực tiếp: {ham_duoc_goi_truoc()}")  # Dự kiến: "trực tiếp"

if __name__ == "__main__":
    bai_tap_1()
    bai_tap_2()
    bai_tap_3()
    bai_tap_4()