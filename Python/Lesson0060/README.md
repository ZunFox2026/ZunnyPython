# Python 60 Cấp Độ Cơ Bản - Hành Trình Từ Con Số 0 Đến Lập Trình Viên

## Giới thiệu

Chào mừng bạn đến với bài học thứ 60 trong chuỗi hành trình "Python 60 Cấp Độ Cơ Bản"! Đây là bài học cuối cùng trong cấp độ **Cơ bản**, đánh dấu bước chuyển quan trọng từ người mới bắt đầu đến việc nắm vững các khái niệm nền tảng của lập trình Python. Trong bài này, chúng ta sẽ tổng hợp và củng cố những kiến thức đã học qua các chủ đề như biến, vòng lặp, rẽ nhánh, hàm và cấu trúc dữ liệu đơn giản. Mục tiêu là giúp bạn tự tin viết những chương trình nhỏ hoàn chỉnh và sẵn sàng bước sang cấp độ **Trung cấp**.

## Lý thuyết

Python là ngôn ngữ lập trình linh hoạt và dễ học, lý tưởng cho người mới. Trong 60 bài đầu, bạn đã làm quen với:
- Biến và kiểu dữ liệu (int, float, str, bool)
- Câu điều kiện `if-elif-else`
- Vòng lặp `for` và `while`
- Hàm với `def` và giá trị trả về
- Danh sách (`list`), chuỗi (`string`) và từ điển (`dict`)

Tất cả những kiến thức này đều là nền tảng thiết yếu để phát triển các ứng dụng thực tế.

## Ví dụ

Dưới đây là một chương trình nhỏ tổng hợp các kiến thức đã học: một chương trình quản lý danh sách việc cần làm (to-do list):

```python
def hien_thi_danh_sach(danh_sach):
    print("\nDanh sách việc cần làm:")
    for i, viec in enumerate(danh_sach, 1):
        print(f"{i}. {viec}")

def them_viec(danh_sach):
    viec_moi = input("Nhập việc cần làm: ")
    danh_sach.append(viec_moi)
    print("Đã thêm việc!")

# Chương trình chính
if __name__ == "__main__":
    to_do_list = []
    while True:
        hien_thi_danh_sach(to_do_list)
        lua_chon = input("\nChọn: (1) Thêm việc, (2) Thoát: ")
        if lua_chon == "1":
            them_viec(to_do_list)
        elif lua_chon == "2":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
```

## Bài tập

1. Sửa chương trình trên để cho phép người dùng xóa một việc theo số thứ tự.
2. Thêm chức năng đánh dấu việc đã hoàn thành.
3. Lưu danh sách vào file văn bản khi thoát và đọc lại khi khởi động.

Chúc mừng bạn đã hoàn thành cấp độ Cơ bản! Hãy tiếp tục đồng hành cùng chúng tôi ở cấp độ Trung cấp để khám phá nhiều điều thú vị hơn với Python!