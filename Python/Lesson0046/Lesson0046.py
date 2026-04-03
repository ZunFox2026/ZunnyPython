"""
Bài học Python 46 cấp Cơ bản - Làm Chủ Ngôn Ngữ Lập Trình từ A đến Z
Tài liệu: Tổng hợp các khái niệm cơ bản trong Python (biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm, danh sách)
"""

# 1. Biến và Kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị
ten = "Nguyen Van A"        # Chuỗi (string)
tuoi = 20                   # Số nguyên (int)
chieu_cao = 1.75            # Số thực (float)
la_sinh_vien = True         # Boolean (True/False)

# In thông tin ra màn hình
print("Thông tin cá nhân:")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Cấu trúc điều kiện (if-elif-else)
print("\n--- Kiểm tra độ tuổi ---")
if tuoi < 18:
    print("Bạn chưa đủ tuổi trưởng thành.")
elif 18 <= tuoi < 60:
    print("Bạn là người trưởng thành.")
else:
    print("Bạn là người cao tuổi.")

# Ví dụ 2: Kiểm tra số chẵn/lẻ
so = 7
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# 3. Vòng lặp for và while
print("\n--- In các số từ 1 đến 5 ---")
for i in range(1, 6):
    print(i)

print("\n--- In số chẵn từ 0 đến 10 bằng while ---")
n = 0
while n <= 10:
    if n % 2 == 0:
        print(n)
    n += 1

# 4. Danh sách (list) và các thao tác cơ bản
danh_sach_mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
print(f"\nDanh sách môn học: {danh_sach_mon_hoc}")

# Thêm phần tử vào danh sách
danh_sach_mon_hoc.append("Văn")
print(f"Sau khi thêm 'Văn': {danh_sach_mon_hoc}")

# Truy cập phần tử theo chỉ số
print(f"Môn học đầu tiên: {danh_sach_mon_hoc[0]}")

# Duyệt danh sách bằng vòng lặp
print("Các môn học:")
for mon in danh_sach_mon_hoc:
    print(f" - {mon}")

# 5. Hàm trong Python
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    :param a: số thứ nhất
    :param b: số thứ hai
    :return: tổng của a và b
    """
    return a + b

def chao_ten(ten):
    """
    Hàm in lời chào
    :param ten: tên người dùng
    """
    print(f"Xin chào, {ten}!")

# Gọi hàm
print("\n--- Sử dụng hàm ---")
ket_qua = tinh_tong(5, 3)
print(f"Tổng của 5 và 3 là: {ket_qua}")

chao_ten("Minh")

# Ví dụ 3: Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"11 có phải số nguyên tố? {la_so_nguyen_to(11)}")

# Bài tập nhỏ: Viết chương trình tính giai thừa của một số
def tinh_giai_thua(n):
    """
    Hàm tính giai thừa của n (n!)
    """
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua

# Kiểm thử bài tập
print("\n--- Bài tập: Tính giai thừa ---")
so_can_tinh = 5
print(f"Giai thừa của {so_can_tinh} là: {tinh_giai_thua(so_can_tinh)}")

# Gợi ý bài tập thêm cho người học:
# 1. Viết hàm tìm số lớn nhất trong danh sách
# 2. Viết chương trình in bảng cửu chương từ 1 đến 10
# 3. Kiểm tra một chuỗi có phải là palindrome không

def main():
    print("Chương trình học Python từ A đến Z đã hoàn thành!")
    print("Hãy thực hành thêm để nắm vững kiến thức.")

if __name__ == "__main__":
    main()
```