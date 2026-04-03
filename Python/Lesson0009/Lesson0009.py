# Python 9 Cấp Cơ Bản - Bài học tổng hợp cơ bản
# Tác giả: Học viên Python
# Mục tiêu: Giới thiệu 9 cấp độ cơ bản trong Python qua ví dụ và bài tập

def main():
    """
    Hàm chính thực hiện các ví dụ và bài tập cơ bản
    """

    # ===== CẤP 1: In ra màn hình =====
    print("=== Cấp 1: In ra màn hình ===")
    print("Chào mừng bạn đến với Python!")

    # ===== CẤP 2: Biến và kiểu dữ liệu =====
    print("\n=== Cấp 2: Biến và kiểu dữ liệu ===")
    ten = "An"           # chuỗi
    tuoi = 15            # số nguyên
    chieu_cao = 1.65     # số thực
    la_hoc_sinh = True   # boolean

    print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

    # ===== CẤP 3: Nhập dữ liệu từ người dùng =====
    print("\n=== Cấp 3: Nhập dữ liệu ===")
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    print(f"Xin chào, {ten_nguoi_dung}!")

    # ===== CẤP 4: Câu điều kiện (if-else) =====
    print("\n=== Cấp 4: Câu điều kiện ===")
    diem = 7.5
    if diem >= 8.0:
        print("Bạn đạt loại Giỏi!")
    elif diem >= 6.5:
        print("Bạn đạt loại Khá!")
    else:
        print("Bạn cần cố gắng hơn!")

    # ===== CẤP 5: Vòng lặp for =====
    print("\n=== Cấp 5: Vòng lặp for ===")
    print("In các số từ 1 đến 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()  # xuống dòng

    # ===== CẤP 6: Vòng lặp while =====
    print("\n=== Cấp 6: Vòng lặp while ===")
    dem = 3
    while dem > 0:
        print(f"Còn {dem} giây...")
        dem -= 1
    print("Hết giờ!")

    # ===== CẤP 7: Hàm (function) =====
    print("\n=== Cấp 7: Hàm ===")

    def tinh_tong(a, b):
        """Hàm tính tổng hai số"""
        return a + b

    ket_qua = tinh_tong(10, 20)
    print(f"Tổng của 10 và 20 là: {ket_qua}")

    # ===== CẤP 8: Danh sách (list) =====
    print("\n=== Cấp 8: Danh sách ===")
    mon_an = ["phở", "bún", "cơm", "xôi"]
    print("Các món ăn yêu thích:", mon_an)
    mon_an.append("bánh mì")  # thêm phần tử
    print("Sau khi thêm bánh mì:", mon_an)

    # ===== CẤP 9: Xử lý lỗi (try-except) =====
    print("\n=== Cấp 9: Xử lý lỗi ===")
    try:
        so = int(input("Nhập một số nguyên: "))
        print(f"Bạn đã nhập: {so}")
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên!")

    # ===== VÍ DỤ THỰC HÀNH =====
    print("\n=== Ví dụ 1: Kiểm tra số chẵn/lẻ ===")
    so_nhap = 8
    if so_nhap % 2 == 0:
        print(f"{so_nhap} là số chẵn")
    else:
        print(f"{so_nhap} là số lẻ")

    print("\n=== Ví dụ 2: In bảng cửu chương 2 ===")
    for i in range(1, 11):
        print(f"2 x {i} = {2 * i}")

    # ===== BÀI TẬP NHỎ =====
    print("\n=== Bài tập nhỏ ===")
    print("Bài tập: Viết chương trình tính tổng các số từ 1 đến n")
    try:
        n = int(input("Nhập số n: "))
        tong = sum(range(1, n + 1))
        print(f"Tổng các số từ 1 đến {n} là: {tong}")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

    print("\nChúc mừng bạn đã hoàn thành 9 cấp cơ bản!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn:**

- **9 cấp cơ bản** bao gồm: in dữ liệu, biến, nhập liệu, điều kiện, vòng lặp (for/while), hàm, danh sách, xử lý lỗi.
- **2 ví dụ**: kiểm tra số chẵn/lẻ và in bảng cửu chương.
- **Bài tập nhỏ**: tính tổng dãy số từ 1 đến n.
- Dòng lệnh: khoảng 95 dòng, rõ ràng, dễ hiểu cho người mới bắt đầu.

Chạy file `.py` này bằng Python để thực hành!