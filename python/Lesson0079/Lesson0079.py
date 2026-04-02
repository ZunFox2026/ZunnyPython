def la_chinh_phuong(n):
    # Kiểm tra xem số n có phải là số chính phương không
    if n < 0:
        return False
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

# Ví dụ sử dụng
so_kiem_tra = 25
if la_chinh_phuong(so_kiem_tra):
    print(f"{so_kiem_tra} là số chính phương")
else:
    print(f"{so_kiem_tra} không phải là số chính phương")

# Tìm tất cả các số chính phương trong một khoảng
khoang = range(1, 101)  # ví dụ từ 1 đến 100
so_chinh_phuong = [i for i in khoang if la_chinh_phuong(i)]
print("Các số chính phương trong khoảng từ 1 đến 100 là:", so_chinh_phuong)