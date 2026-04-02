# Làm quen với thư viện Tkinter
## Giới thiệu
Thư viện Tkinter là một trong những thư viện đồ họa người dùng (GUI) phổ biến nhất trong Python. Nó cho phép bạn tạo ra các ứng dụng GUI đơn giản và trực quan. Với Tkinter, bạn có thể tạo ra các cửa sổ, nút bấm, trường nhập liệu, menu và nhiều thành phần khác. Đây là một công cụ lý tưởng cho những người mới bắt đầu học lập trình Python và muốn tạo ra các ứng dụng GUI.

## Lý thuyết
Tkinter cung cấp một số lượng lớn các thành phần GUI khác nhau, bao gồm:
- `Tk`: Lớp cơ bản để tạo ra một cửa sổ chính.
- `Label`: Thành phần hiển thị văn bản hoặc hình ảnh.
- `Button`: Thành phần tạo ra một nút bấm.
- `Entry`: Thành phần tạo ra một trường nhập liệu.
- `Text`: Thành phần tạo ra một vùng nhập liệu đa dòng.
- `Frame`: Thành phần tạo ra một khung chứa các thành phần khác.

Mỗi thành phần này có thể được tùy chỉnh bằng cách sử dụng các phương thức và thuộc tính khác nhau. Ví dụ, bạn có thể thay đổi màu sắc, phông chữ, kích thước của văn bản trong một `Label`.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách tạo ra một cửa sổ với một nút bấm và một trường nhập liệu:
```python
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Làm quen với Tkinter")

# Tạo một nút bấm
button = tk.Button(root, text="Click me!", command=lambda: print("Nút bấm được click!"))
button.pack()

# Tạo một trường nhập liệu
entry = tk.Entry(root)
entry.pack()

# Chạy ứng dụng
root.mainloop()
```
Trong ví dụ này, chúng ta tạo ra một cửa sổ với tiêu đề "Làm quen với Tkinter", một nút bấm với văn bản "Click me!" và một trường nhập liệu. Khi nút bấm được click, nó sẽ in ra thông báo "Nút bấm được click!".

## Bài tập
Bài tập cho bạn:
- Tạo một cửa sổ với hai nút bấm, một nút bấm có văn bản "Click me!" và một nút bấm có văn bản "Thoát".
- Khi nút bấm "Click me!" được click, nó sẽ in ra thông báo "Nút bấm được click!".
- Khi nút bấm "Thoát" được click, nó sẽ đóng cửa sổ lại.
- Thêm một trường nhập liệu vào cửa sổ và khi người dùng nhập liệu vào trường này, nó sẽ được in ra khi nút bấm "Click me!" được click.