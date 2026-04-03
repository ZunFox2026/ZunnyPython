# Bài học Python số 35: Làm việc với Decorators (Trang trí viên)

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của **decorator** trong Python.
- Biết cách viết và sử dụng decorator đơn giản và có tham số.
- Áp dụng decorator vào các tình huống thực tế như đo thời gian thực thi, kiểm tra quyền truy cập, ghi log.
- Nâng cao kỹ năng lập trình hàm bậc cao và xử lý hàm như một đối tượng.

## Lý thuyết chi tiết

### 1. Hàm là đối tượng đầu lớp một (First-class object)
Trong Python, **hàm** là đối tượng đầu lớp một, có nghĩa là:
- Có thể gán hàm cho biến.
- Có thể truyền hàm làm tham số cho hàm khác.
- Có thể trả về hàm từ một hàm.

Ví dụ:
```python
def xin_chao(ten):
    return f"Xin chào, {ten}!"

ham = xin_chao
print(ham("An"))  # Xin chào, An!
```

### 2. Hàm lồng nhau (Nested function)
Hàm có thể được định nghĩa bên trong một hàm khác.

```python
def chao_hoi(loai):
    def tieng_viet():
        return "Xin chào!"
    def tieng_anh():
        return "Hello!"
    
    if loai == "vi":
        return tieng_viet
    else:
        return tieng_anh

ham = chao_hoi("vi")
print(ham())  # Xin chào!
```

### 3. Closure
Closure là hàm con truy cập biến từ hàm cha, ngay cả khi hàm cha đã kết thúc.

```python
def tao_ham_chao(ten):
    def chao():
        return f"Xin chào {ten}!"
    return chao

chao_an = tao_ham_chao("An")
print(chao_an())  # Xin chào An!
```

### 4. Decorator là gì?
**Decorator** là một hàm nhận vào một hàm khác, thêm hành vi cho hàm đó và trả về một hàm mới.

Cú pháp: dùng `@tên_decorator` trên hàm cần trang trí.

#### Cấu trúc cơ bản
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Làm gì đó trước khi gọi hàm
        ket_qua = func(*args, **kwargs)
        # Làm gì đó sau khi gọi hàm
        return ket_qua
    return wrapper
```

#### Ví dụ: In ra thông báo trước và sau khi gọi hàm
```python
def log_thuc_thi(func):
    def wrapper(*args, **kwargs):
        print(f"Đang thực thi hàm {func.__name__}")
        ket_qua = func(*args, **kwargs)
        print(f"Hoàn tất thực thi hàm {func.__name__}")
        return ket_qua
    return wrapper

@log_thuc_thi
def tinh_tong(a, b):
    return a + b

print(tinh_tong(3, 5))
# Output:
# Đang thực thi hàm tinh_tong
# Hoàn tất thực thi hàm tinh_tong
# 8
```

### 5. Decorator có tham số
Để tạo decorator có tham số, ta cần thêm một lớp hàm bao ngoài.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                ket_qua = func(*args, **kwargs)
            return ket_qua
        return wrapper
    return decorator

@repeat(3)
def chao():
    print("Xin chào!")

chao()  # In ra 3 lần "Xin chào!"
```

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi hàm
Sử dụng decorator để đo thời gian một hàm thực thi.

### Ví dụ 2: Kiểm tra quyền truy cập
Trang trí một hàm yêu cầu người dùng phải đăng nhập.

### Ví dụ 3: Tạo cache đơn giản với decorator
Lưu kết quả của hàm để tránh tính toán lại.

## Bài tập thực hành
1. Viết decorator `in_hoa` chuyển kết quả trả về của hàm (chuỗi) thành chữ in hoa.
2. Viết decorator `kiem_tra_so_duong` chỉ cho phép hàm được gọi nếu tất cả tham số là số dương.
3. Viết decorator `ghi_log` ghi lại thời gian gọi hàm và tham số vào file log.txt.
4. Viết decorator `gioi_han_toc_do` giới hạn tần suất gọi hàm (chỉ cho phép gọi mỗi 2 giây một lần).
5. Viết decorator `thu_hoach_ngoai_le` bắt mọi ngoại lệ và in ra thông báo, trả về None nếu có lỗi.

## Tổng kết
- Decorator là công cụ mạnh mẽ để mở rộng hành vi của hàm mà không làm thay đổi mã nguồn gốc.
- Có thể dùng để ghi log, đo hiệu năng, kiểm tra quyền, cache, giới hạn tần suất, xử lý lỗi, v.v.
- Hiểu rõ closure và hàm bậc cao là nền tảng để viết decorator hiệu quả.
- Decorator có thể không có tham số hoặc có tham số (cần thêm 1 lớp hàm bao ngoài).

Hãy luyện tập thường xuyên để thành thạo kỹ năng này!
