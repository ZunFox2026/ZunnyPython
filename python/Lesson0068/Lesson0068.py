# Bài 68: Lập Trình Cơ Bản - Bài tập về hàm

# Định nghĩa một hàm cơ bản
def chao_mung(ten):
    # In ra lời chào
    print(f"Xin chào, {ten}!")

# Định nghĩa một hàm tính tổng
def tinh_tong(a, b):
    # Trả về tổng của a và b
    return a + b

# Định nghĩa một hàm kiểm tra số chẵn
def kiem_tra_so_chan(n):
    # Trả về True nếu n là số chẵn, False nếu n là số lẻ
    return n % 2 == 0

# Ví dụ sử dụng hàm
print("Ví dụ sử dụng hàm:")
chao_mung("Nguyễn Văn A")
ket_qua = tinh_tong(5, 7)
print(f"Tổng của 5 và 7 là: {ket_qua}")

# Ví dụ sử dụng hàm kiểm tra số chẵn
so = 10
if kiem_tra_so_chan(so):
    print(f"{so} là số chẵn")
else:
    print(f"{so} là số lẻ")