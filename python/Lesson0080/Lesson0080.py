# Đây là chương trình mẫu cho bài "Lập Trình Cơ Bản"
# Chương trình này sẽ thực hiện các phép toán cơ bản

# Hàm chính của chương trình
def main():
    # Khai báo biến số nguyên
    so_nguyen = 10
    
    # Khai báo biến số thực
    so_thuc = 20.5
    
    # Khai báo biến chuỗi
    chuoi = "Xin chào, thế giới!"
    
    # In ra màn hình giá trị của biến số nguyên
    print("Giá trị của biến số nguyên:", so_nguyen)
    
    # In ra màn hình giá trị của biến số thực
    print("Giá trị của biến số thực:", so_thuc)
    
    # In ra màn hình giá trị của biến chuỗi
    print("Giá trị của biến chuỗi:", chuoi)
    
    # Thực hiện phép toán cộng
    ket_qua_cong = so_nguyen + int(so_thuc)
    print("Kết quả của phép toán cộng:", ket_qua_cong)
    
    # Thực hiện phép toán trừ
    ket_qua_tru = so_nguyen - int(so_thuc)
    print("Kết quả của phép toán trừ:", ket_qua_tru)
    
    # Thực hiện phép toán nhân
    ket_qua_nhan = so_nguyen * int(so_thuc)
    print("Kết quả của phép toán nhân:", ket_qua_nhan)
    
    # Thực hiện phép toán chia
    if so_thuc != 0:
        ket_qua_chia = so_nguyen / so_thuc
        print("Kết quả của phép toán chia:", ket_qua_chia)
    else:
        print("Không thể chia cho 0!")

# Gọi hàm chính
if __name__ == "__main__":
    main()