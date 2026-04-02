# Nhập thư viện Tkinter
from tkinter import *

# Tạo cửa sổ chính
root = Tk()
# Đặt tiêu đề cho cửa sổ
root.title("Làm quen với Tkinter")

# Tạo label và hiển thị văn bản
label = Label(root, text="Xin chào, tôi là Tkinter!")
# Thêm label vào cửa sổ
label.pack()

# Tạo nút bấm
def xin_chao():
    # Hiển thị thông báo khi bấm nút
    print("Xin chào!")

nút_bấm = Button(root, text="Bấm vào đây", command=xin_chao)
# Thêm nút bấm vào cửa sổ
nút_bấm.pack()

# Tạo trường nhập văn bản
trường_nhập = Entry(root)
# Thêm trường nhập vào cửa sổ
trường_nhập.pack()

# Tạo nút bấm để hiển thị nội dung trường nhập
def hiển_thị():
    # Lấy nội dung trường nhập và hiển thị
    nội_dung = trường_nhập.get()
    print(nội_dung)

nút_hiển_thị = Button(root, text="Hiển thị nội dung", command=hiển_thị)
# Thêm nút bấm vào cửa sổ
nút_hiển_thị.pack()

# Khởi động cửa sổ
root.mainloop()