def chao_hoi(ten):
    # Hàm chào hỏi
    print(f'Xin chào {ten}!')

# Gọi hàm chào hỏi
chao_hoi('Nguyễn Văn A')

# Bài tập về nhà: Viết một hàm tính tổng các số từ 1 đến n

def tinh_tong(n):
    # Khởi tạo biến tổng
    tong = 0
    # Dùng vòng lặp để tính tổng
    for i in range(1, n + 1):
        # Cộng dồn vào biến tổng
        tong += i
    # Trả về biến tổng
    return tong

# Gọi hàm tính tổng
ket_qua = tinh_tong(10)
print(f'Tổng từ 1 đến 10 là {ket_qua}')