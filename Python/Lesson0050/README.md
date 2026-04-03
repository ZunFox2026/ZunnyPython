# Python 50 Cấp Cơ Bản – Bài 50

## Giới thiệu

Chào mừng bạn đến với bài học cuối cùng trong chuỗi **"Python 50 Cấp Cơ Bản"**! Bài học này sẽ tổng kết những kiến thức cơ bản bạn đã học qua bằng cách thực hành một chương trình nhỏ hoàn chỉnh. Chúng ta sẽ xây dựng một **chương trình quản lý danh sách công việc đơn giản (To-Do List)** bằng Python. Đây là ứng dụng thực tế giúp củng cố các kỹ năng như: xử lý chuỗi, vòng lặp, cấu trúc điều kiện, và thao tác với danh sách.

## Lý thuyết

Trong bài này, chúng ta sẽ sử dụng:
- **Danh sách (list)** để lưu trữ các công việc.
- **Vòng lặp `while`** để chương trình chạy liên tục cho đến khi người dùng thoát.
- **Câu lệnh điều kiện `if-elif-else`** để xử lý các lựa chọn của người dùng.
- **Các thao tác cơ bản**: thêm, xóa, hiển thị công việc.

## Ví dụ

Dưới đây là chương trình To-Do List đơn giản:

```python
# Danh sách công việc
danh_sach = []

print("=== Quản lý To-Do List ===")
print("1. Thêm công việc")
print("2. Hiển thị công việc")
print("3. Xóa công việc")
print("4. Thoát")

while True:
    lua_chon = input("\nChọn chức năng (1-4): ")

    if lua_chon == "1":
        cong_viec = input("Nhập công việc mới: ")
        danh_sach.append(cong_viec)
        print(f"Đã thêm: {cong_viec}")
    elif lua_chon == "2":
        if danh_sach:
            print("Danh sách công việc:")
            for i, cv in enumerate(danh_sach, 1):
                print(f"{i}. {cv}")
        else:
            print("Danh sách trống.")
    elif lua_chon == "3":
        if danh_sach:
            stt = int(input("Nhập số thứ tự công việc cần xóa: ")) - 1
            if 0 <= stt < len(danh_sach):
                xoa = danh_sach.pop(stt)
                print(f"Đã xóa: {xoa}")
            else:
                print("Số thứ tự không hợp lệ.")
        else:
            print("Danh sách trống, không có gì để xóa.")
    elif lua_chon == "4":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
```

## Bài tập

Hãy cải tiến chương trình trên bằng cách:
1. Thêm chức năng đánh dấu công việc đã hoàn thành.
2. Lưu danh sách vào file `todo.txt` khi thoát và đọc lại khi khởi động.
3. Kiểm tra trùng lặp công việc trước khi thêm.

Chúc mừng bạn đã hoàn thành 50 bài học cơ bản! Hãy tiếp tục học hỏi và phát triển với Python! 🐍