"""
Bài học: Python 23 Cấp Cơ Bản
Mô tả: Hướng dẫn các khái niệm cơ bản trong Python qua 23 cấp độ đơn giản.
Tác giả: AI Tutor
Ngày: 2025
"""

# Cấp 1: In ra màn hình
print("Chào mừng bạn đến với Python 23 Cấp Cơ Bản!")

# Cấp 2: Biến và kiểu dữ liệu
ten = "An"           # chuỗi
tuoi = 15            # số nguyên
chieu_cao = 1.65     # số thực
la_hoc_sinh = True   # boolean

# Cấp 3: In biến
print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

# Cấp 4: Nhập liệu từ người dùng
ho_ten = input("Nhập họ tên của bạn: ")
print(f"Xin chào, {ho_ten}!")

# Cấp 5: Toán tử cơ bản
a = 10
b = 3
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
print(f"Thương: {a / b:.2f}")  # làm tròn 2 chữ số

# Cấp 6: Toán tử so sánh
print(f"a > b: {a > b}")
print(f"a == b: {a == b}")

# Cấp 7: Câu lệnh điều kiện if
if tuoi >= 18:
    print("Bạn đã đủ tuổi trưởng thành.")
else:
    print("Bạn chưa đủ tuổi trưởng thành.")

# Cấp 8: Câu lệnh if-elif-else
diem = 85
if diem >= 90:
    print("Xếp loại: Xuất sắc")
elif diem >= 80:
    print("Xếp loại: Giỏi")
elif diem >= 70:
    print("Xếp loại: Khá")
else:
    print("Xếp loại: Trung bình")

# Cấp 9: Vòng lặp for
print("In các số từ 1 đến 5:")
for i in range(1, 6):
    print(i, end=" ")
print()  # xuống dòng

# Cấp 10: Vòng lặp while
dem = 1
print("Đếm ngược từ 5:")
while dem <= 5:
    print(6 - dem, end=" ")
    dem += 1
print()

# Cấp 11: Danh sách (list)
danh_sach_mon_hoc = ["Toán", "Văn", "Anh"]
print("Các môn học:", danh_sach_mon_hoc)

# Cấp 12: Thêm phần tử vào danh sách
danh_sach_mon_hoc.append("Lý")
print("Sau khi thêm Lý:", danh_sach_mon_hoc)

# Cấp 13: Truy cập phần tử danh sách
print("Môn đầu tiên:", danh_sach_mon_hoc[0])
print("Môn cuối:", danh_sach_mon_hoc[-1])

# Cấp 14: Duyệt danh sách bằng for
print("In từng môn học:")
for mon in danh_sach_mon_hoc:
    print(f"- {mon}")

# Cấp 15: Hàm đơn giản
def xin_chao(ten):
    """Hàm in lời chào"""
    print(f"Xin chào, {ten}!")

# Cấp 16: Gọi hàm
xin_chao("Bình")

# Cấp 17: Hàm có trả về giá trị
def tinh_tong(x, y):
    return x + y

ket_qua = tinh_tong(7, 8)
print(f"Tổng của 7 và 8 là: {ket_qua}")

# Cấp 18: Xử lý lỗi với try-except
try:
    so = int(input("Nhập một số nguyên: "))
    print(f"Bạn đã nhập: {so}")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng số nguyên!")

# Cấp 19: Tạo và sử dụng từ điển (dictionary)
thong_tin_hoc_sinh = {
    "ten": "Mai",
    "tuoi": 16,
    "lop": "10A2"
}
print("Thông tin học sinh:", thong_tin_hoc_sinh)

# Cấp 20: Truy cập giá trị từ điển
print(f"Học sinh tên: {thong_tin_hoc_sinh['ten']}")

# Cấp 21: Thêm cặp key-value vào từ điển
thong_tin_hoc_sinh["diem_tb"] = 8.7
print("Sau khi thêm điểm:", thong_tin_hoc_sinh)

# Cấp 22: Vòng lặp với từ điển
print("Thông tin chi tiết:")
for khoa, gia_tri in thong_tin_hoc_sinh.items():
    print(f"{khoa}: {gia_tri}")

# Cấp 23: Kết thúc chương trình
print("Chúc mừng bạn đã hoàn thành 23 cấp cơ bản của Python!")

# --- VÍ DỤ THỰC HÀNH ---
# Ví dụ 1: Tính trung bình cộng 3 số
def tinh_trung_binh(a, b, c):
    return (a + b + c) / 3

print(f"Trung bình của 4, 5, 6: {tinh_trung_binh(4, 5, 6)}")

# Ví dụ 2: Kiểm tra số chẵn/lẻ
so_nhap = 12
if so_nhap % 2 == 0:
    print(f"{so_nhap} là số chẵn.")
else:
    print(f"{so_nhap} là số lẻ.")

# Ví dụ 3: Tìm phần tử lớn nhất trong danh sách
danh_sach = [3, 7, 2, 9, 1]
max_val = danh_sach[0]
for num in danh_sach:
    if num > max_val:
        max_val = num
print(f"Giá trị lớn nhất: {max_val}")

# --- BÀI TẬP NHỎ ---
"""
Bài tập: Viết chương trình nhập vào danh sách điểm của học sinh (5 điểm),
sau đó tính và in ra điểm trung bình, điểm cao nhất và thấp nhất.
Gợi ý: Dùng vòng lặp, danh sách và hàm max(), min().
"""

def bai_tap_nho():
    print("\n--- BÀI TẬP NHỎ: TÍNH ĐIỂM TRUNG BÌNH ---")
    diem_list = []
    for i in range(5):
        while True:
            try:
                diem = float(input(f"Nhập điểm môn {i+1} (0-10): "))
                if 0 <= diem <= 10:
                    diem_list.append(diem)
                    break
                else:
                    print("Điểm phải từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
    
    trung_binh = sum(diem_list) / len(diem_list)
    print(f"\nĐiểm trung bình: {trung_binh:.2f}")
    print(f"Điểm cao nhất: {max(diem_list)}")
    print(f"Điểm thấp nhất: {min(diem_list)}")

# Gọi bài tập nhỏ
bai_tap_nho()

if __name__ == "__main__":
    print("\nChương trình kết thúc. Cảm ơn bạn đã học cùng Python 23 Cấp Cơ Bản!")
```