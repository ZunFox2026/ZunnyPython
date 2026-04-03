# Bài học Python 5 cấp Cơ bản - Bắt đầu với Python
# Mục tiêu: Học các khái niệm cơ bản: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm

def main():
    # 1. Biến và kiểu dữ liệu cơ bản
    # Biến là tên để lưu trữ dữ liệu
    ten = "An"              # Chuỗi (string)
    tuoi = 12               # Số nguyên (int)
    chieu_cao = 1.55        # Số thực (float)
    hoc_gioi = True         # Boolean (True/False)

    print(f"Xin chào, mình tên là {ten}, {tuoi} tuổi, cao {chieu_cao}m.")
    print(f"Học giỏi: {hoc_gioi}")

    # 2. Câu lệnh điều kiện (if-elif-else)
    # Dùng để ra quyết định trong chương trình
    if tuoi < 10:
        print("Bạn là học sinh tiểu học.")
    elif tuoi < 16:
        print("Bạn là học sinh trung học cơ sở.")
    else:
        print("Bạn là học sinh trung học phổ thông.")

    # Ví dụ 2: Kiểm tra điểm số
    diem = 8.5
    if diem >= 9:
        print("Xếp loại: Xuất sắc")
    elif diem >= 7:
        print("Xếp loại: Khá")
    elif diem >= 5:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")

    # 3. Vòng lặp for
    # Dùng để lặp qua một dãy số hoặc danh sách
    print("\nIn các số từ 1 đến 5:")
    for i in range(1, 6):
        print(i)

    # Ví dụ: In lời chúc cho các bạn
    ban_be = ["Bình", "Hoa", "Cường"]
    print("\nLời chúc gửi các bạn:")
    for ban in ban_be:
        print(f"Chúc bạn {ban} học giỏi và vui vẻ!")

    # 4. Hàm (function)
    # Hàm giúp tái sử dụng đoạn mã
    def tinh_tong(a, b):
        """Hàm này tính tổng của hai số"""
        return a + b

    def chao_ten(ten):
        """Hàm chào hỏi theo tên"""
        print(f"Xin chào {ten}! Rất vui được gặp bạn.")

    # Gọi hàm
    ket_qua = tinh_tong(5, 7)
    print(f"Tổng của 5 và 7 là: {ket_qua}")

    chao_ten("Lan")

    # 5. Bài tập nhỏ: Viết chương trình kiểm tra số chẵn/lẻ
    # Yêu cầu người dùng nhập một số và kiểm tra
    print("\n--- Bài tập nhỏ ---")
    try:
        so = int(input("Nhập một số nguyên: "))
        if so % 2 == 0:
            print(f"Số {so} là số chẵn.")
        else:
            print(f"Số {so} là số lẻ.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

    # Gợi ý mở rộng: Viết hàm kiểm tra chẵn lẻ
    def kiem_tra_chan_le(n):
        return "chẵn" if n % 2 == 0 else "lẻ"

    # Test hàm
    print(f"10 là số {kiem_tra_chan_le(10)}")
    print(f"7 là số {kiem_tra_chan_le(7)}")


# Chạy chương trình
if __name__ == "__main__":
    main()


"""
Tóm tắt bài học:
- Biến: lưu trữ dữ liệu (int, float, str, bool)
- Câu điều kiện: if, elif, else
- Vòng lặp: for ... in range()
- Hàm: def để tạo hàm, return để trả kết quả
- Bài tập: kiểm tra số chẵn lẻ

Gợi ý luyện tập thêm:
1. Viết chương trình tính diện tích hình chữ nhật
2. In bảng cửu chương từ 1 đến 5
3. Tạo danh sách các món ăn yêu thích và in ra
"""
```