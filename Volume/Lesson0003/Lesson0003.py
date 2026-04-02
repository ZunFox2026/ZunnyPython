def kiem_tra_so_nguyen_to(n):
    # Nếu n nhỏ hơn 2 thì không phải là số nguyên tố
    if n < 2:
        return False
    # Duyệt từ 2 đến căn bậc 2 của n
    for i in range(2, int(n**0.5) + 1):
        # Nếu n chia hết cho bất kỳ số nào trong khoảng này thì không phải là số nguyên tố
        if n % i == 0:
            return False
    # Nếu không chia hết cho bất kỳ số nào trong khoảng này thì là số nguyên tố
    return True

def tim_so_nguyen_to():
    # Nhập số từ người dùng
    n = int(input("Nhập số: "))
    # Kiểm tra số nguyên tố
    if kiem_tra_so_nguyen_to(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không là số nguyên tố")

# Chạy chương trình
tim_so_nguyen_to()