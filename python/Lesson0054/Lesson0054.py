def kiem_tra_so_nguyen_to(n):
    # Kiểm tra số nguyên tố
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        # Nếu có số chia hết thì không phải số nguyên tố
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to(n):
    # Tìm số nguyên tố trong khoảng từ 1 đến n
    so_nguyen_to = []
    for i in range(1, n + 1):
        if kiem_tra_so_nguyen_to(i):
            so_nguyen_to.append(i)
    return so_nguyen_to

# Ví dụ sử dụng
n = 30
so_nguyen_to = tim_so_nguyen_to(n)
print("Số nguyên tố trong khoảng từ 1 đến", n, "là:", so_nguyen_to)