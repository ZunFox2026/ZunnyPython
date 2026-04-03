# Python 40 Cấp Cơ Bản: Hành Trình Từ Con Số 0 Đến Tự Tin Lập Trình

## Giới thiệu

Chào mừng bạn đến với bài học thứ 40 trong chuỗi "Python 40 Cấp Cơ Bản" – một hành trình được thiết kế dành riêng cho người mới bắt đầu, giúp bạn từng bước làm chủ ngôn ngữ lập trình Python. Ở bài cuối cùng này, chúng ta sẽ tổng kết lại toàn bộ kiến thức đã học và áp dụng vào một ví dụ thực tế, từ đó củng cố sự tự tin khi lập trình. Dù bạn xuất phát từ con số 0, giờ đây bạn đã có thể viết mã, xử lý dữ liệu, sử dụng hàm, và làm việc với các cấu trúc điều khiển. Bài học này là bước đệm hoàn hảo để bạn tiếp tục hành trình phát triển với Python ở cấp độ nâng cao.

## Lý thuyết

Trong suốt 40 bài học, bạn đã được học các khái niệm cốt lõi của Python: biến, kiểu dữ liệu, cấu trúc rẽ nhánh (`if-else`), vòng lặp (`for`, `while`), hàm (`def`), danh sách (`list`), từ điển (`dict`), và xử lý lỗi (`try-except`). Bài học cuối cùng này không giới thiệu kiến thức mới, mà tập trung vào việc **tổng hợp và vận dụng** những kiến thức đó để giải quyết một bài toán thực tế: quản lý danh sách học sinh.

## Ví dụ

Dưới đây là một chương trình đơn giản quản lý danh sách học sinh bằng cách sử dụng từ điển và hàm:

```python
students = {}

def add_student(name, age):
    students[name] = age
    print(f"Đã thêm học sinh: {name}, tuổi: {age}")

def show_students():
    if students:
        print("Danh sách học sinh:")
        for name, age in students.items():
            print(f" - {name}: {age} tuổi")
    else:
        print("Chưa có học sinh nào.")

add_student("An", 15)
add_student("Bình", 16)
show_students()
```

## Bài tập

1. Sửa hàm `add_student` để kiểm tra nếu tên học sinh đã tồn tại thì không thêm mới.
2. Viết hàm `remove_student(name)` để xóa học sinh khỏi danh sách.
3. Viết hàm `find_student(name)` để kiểm tra và in tuổi của học sinh nếu tồn tại.

Chúc mừng bạn đã hoàn thành hành trình 40 bài học! Hãy tiếp tục luyện tập và khám phá thế giới rộng lớn của lập trình!