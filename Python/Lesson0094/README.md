# Bài học Python nâng cao số 94: Sử dụng Metaclass để Tùy chỉnh Hành vi Lớp

Trong bài học này, chúng ta sẽ tìm hiểu về **metaclass** – một khái niệm nâng cao trong Python cho phép bạn kiểm soát cách các lớp được tạo ra. Metaclass là một công cụ mạnh mẽ, thường được dùng trong các framework như Django, SQLAlchemy để tự động hóa cấu hình lớp.

## Mục tiêu bài học
- Hiểu được metaclass là gì và tại sao cần dùng nó.
- Biết cách tạo và sử dụng metaclass để tùy chỉnh hành vi khi định nghĩa lớp.
- Áp dụng metaclass vào các tình huống thực tế như đăng ký tự động lớp, kiểm tra ràng buộc trong thiết kế lớp.
- Rèn luyện kỹ năng lập trình nâng cao thông qua bài tập thực hành.

## Lý thuyết chi tiết

### Metaclass là gì?
Trong Python, mọi thứ đều là đối tượng, kể cả **class**. Khi bạn viết:

```python
class MyClass:
    pass
```

Python tạo ra một **đối tượng kiểu class**. Đối tượng này không phải được tạo bởi `type()` của một instance, mà được tạo bởi **metaclass**.

`type` chính là metaclass mặc định. Bạn có thể kiểm tra bằng:
```python
print(type(MyClass))  # <class 'type'>
```

`type` không chỉ là hàm kiểm tra kiểu dữ liệu, mà còn là một metaclass – nó là thứ tạo ra các class.

### Tạo class bằng type

Bạn có thể tạo class động bằng `type(name, bases, attrs)`:

```python
MyClass = type('MyClass', (), {'x': 5})
```

Tương đương với:

```python
class MyClass:
    x = 5
```

### Tạo metaclass

Metaclass là một lớp kế thừa từ `type`, và ghi đè phương thức `__new__` hoặc `__init__` để can thiệp vào quá trình tạo lớp.

Ví dụ đơn giản:

```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Đang tạo lớp {name}")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass
```

Khi chạy, sẽ in ra: `Đang tạo lớp MyClass`.

### Ứng dụng thực tế của metaclass
- Đăng ký tự động các lớp con (plugin system).
- Kiểm tra ràng buộc khi định nghĩa lớp (ví dụ: bắt buộc có phương thức nào đó).
- Tạo các lớp với hành vi đặc biệt (như singleton, abstract class nâng cao).

## Ví dụ minh họa

### Ví dụ 1: Đăng ký tự động các lớp con

Giả sử bạn đang xây dựng hệ thống plugin, và muốn mọi lớp plugin được tự động đăng ký vào một danh sách.

### Ví dụ 2: Kiểm tra bắt buộc phương thức

Bạn muốn mọi lớp sử dụng metaclass phải định nghĩa phương thức `process()`.

### Ví dụ 3: Tạo lớp với thuộc tính đọc - ghi tùy chỉnh

Sử dụng metaclass để thêm hành vi tự động như in log khi truy cập thuộc tính.

## Bài tập thực hành

1. Viết một metaclass để đảm bảo rằng mọi lớp sử dụng nó đều có thuộc tính `version` kiểu int.
2. Tạo metaclass để đăng ký tất cả các lớp con vào một bộ nhớ (registry) dưới dạng từ điển.
3. Viết metaclass để kiểm tra rằng tên lớp phải bắt đầu bằng chữ in hoa.
4. Tạo metaclass để tự động thêm phương thức `to_dict()` cho mọi lớp.
5. (Nâng cao) Viết metaclass để tạo lớp singleton (chỉ cho phép một instance).

## Tổng kết

Metaclass là một công cụ mạnh mẽ nhưng cũng dễ gây rối nếu dùng không cẩn thận. Nó cho phép bạn kiểm soát toàn bộ quá trình tạo lớp – từ tên, thuộc tính đến hành vi.

Bạn nên sử dụng metaclass khi:
- Cần thay đổi hành vi của lớp tại thời điểm định nghĩa.
- Xây dựng framework hoặc thư viện.
- Cần tự động hóa cấu hình lớp.

Tuy nhiên, hãy nhớ nguyên tắc: "Nếu có thể dùng decorator, inheritance, hay descriptor thì đừng dùng metaclass".

Metaclass là công cụ của bậc thầy – hãy dùng nó một cách có trách nhiệm!