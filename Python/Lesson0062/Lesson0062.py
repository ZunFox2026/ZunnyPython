"""
Bài Python 62: Xử Lý Danh Sách và Vòng Lặp Cơ Bản

Mục tiêu:
- Hiểu cách tạo, truy cập và thao tác với danh sách (list) trong Python.
- Sử dụng vòng lặp for và while để duyệt danh sách.
- Thực hành các thao tác cơ bản: thêm, xóa, tìm kiếm, duyệt phần tử.

Tác giả: [Tên bạn]
Ngày: 2023
"""

def main():
    # -------------------------------
    # 1. Tạo và in danh sách cơ bản
    # -------------------------------
    # Danh sách (list) là cấu trúc dữ liệu lưu trữ nhiều giá trị trong một biến
    danh_sach_ten = ["An", "Bình", "Chi", "Dũng", "Em"]
    print("Danh sách tên ban đầu:")
    print(danh_sach_ten)

    # Truy cập phần tử theo chỉ số (index)
    print(f"\nPhần tử đầu tiên: {danh_sach_ten[0]}")
    print(f"Phần tử cuối cùng: {danh_sach_ten[-1]}")

    # -------------------------------
    # 2. Duyệt danh sách bằng vòng lặp for
    # -------------------------------
    print("\nDuyệt danh sách bằng vòng lặp for:")
    for ten in danh_sach_ten:
        print(f"Xin chào, {ten}!")

    # Dùng enumerate để lấy cả chỉ số và giá trị
    print("\nDuyệt với chỉ số:")
    for i, ten in enumerate(danh_sach_ten):
        print(f"Vị trí {i}: {ten}")

    # -------------------------------
    # 3. Duyệt danh sách bằng vòng lặp while
    # -------------------------------
    print("\nDuyệt bằng vòng lặp while:")
    i = 0
    while i < len(danh_sach_ten):
        print(f"Tên thứ {i + 1}: {danh_sach_ten[i]}")
        i += 1

    # -------------------------------
    # 4. Thêm và xóa phần tử
    # -------------------------------
    # Thêm phần tử vào cuối danh sách
    danh_sach_ten.append("Fong")
    print(f"\nSau khi thêm 'Fong': {danh_sach_ten}")

    # Thêm phần tử vào vị trí cụ thể
    danh_sach_ten.insert(2, "Giang")  # Chèn vào vị trí thứ 2
    print(f"Sau khi chèn 'Giang' vào vị trí 2: {danh_sach_ten}")

    # Xóa phần tử theo giá trị
    danh_sach_ten.remove("Dũng")
    print(f"Sau khi xóa 'Dũng': {danh_sach_ten}")

    # Xóa phần tử theo chỉ số
    phan_tu_xoa = danh_sach_ten.pop(0)  # Xóa phần tử đầu
    print(f"Đã xóa: {phan_tu_xoa}, danh sách còn lại: {danh_sach_ten}")

    # -------------------------------
    # 5. Tìm kiếm trong danh sách
    # -------------------------------
    tim_kiem = "Chi"
    if tim_kiem in danh_sach_ten:
        vi_tri = danh_sach_ten.index(tim_kiem)
        print(f"\n'{tim_kiem}' được tìm thấy tại vị trí {vi_tri}")
    else:
        print(f"\n'{tim_kiem}' không có trong danh sách")

    # -------------------------------
    # 6. Sắp xếp danh sách
    # -------------------------------
    danh_sach_ten.sort()  # Sắp xếp theo thứ tự bảng chữ cái
    print(f"\nDanh sách sau khi sắp xếp: {danh_sach_ten}")

    # -------------------------------
    # 7. Danh sách số và tính toán
    # -------------------------------
    danh_sach_diem = [8, 6, 9, 7, 10, 5]
    print(f"\nDanh sách điểm: {danh_sach_diem}")
    print(f"Điểm cao nhất: {max(danh_sach_diem)}")
    print(f"Điểm thấp nhất: {min(danh_sach_diem)}")
    print(f"Điểm trung bình: {sum(danh_sach_diem) / len(danh_sach_diem):.2f}")

    # -------------------------------
    # Ví dụ thực hành
    # -------------------------------
    print("\n" + "="*40)
    print("VÍ DỤ THỰC HÀNH")
    print("="*40)

    # Ví dụ 1: Tạo danh sách bình phương các số từ 1 đến 5
    binh_phuong = []
    for i in range(1, 6):
        binh_phuong.append(i ** 2)
    print("Bình phương các số từ 1 đến 5:", binh_phuong)

    # Ví dụ 2: Lọc các số chẵn trong danh sách
    so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    so_chan = []
    for so in so_nguyen:
        if so % 2 == 0:
            so_chan.append(so)
    print("Các số chẵn:", so_chan)

    # -------------------------------
    # Bài tập nhỏ: Đếm số lượng phần tử lớn hơn giá trị trung bình
    # -------------------------------
    print("\n" + "-"*30)
    print("BÀI TẬP NHỎ")
    print("-"*30)
    print("Đếm số phần tử lớn hơn giá trị trung bình trong danh sách điểm.")

    trung_binh = sum(danh_sach_diem) / len(danh_sach_diem)
    dem = 0
    for diem in danh_sach_diem:
        if diem > trung_binh:
            dem += 1

    print(f"Giá trị trung bình: {trung_binh:.2f}")
    print(f"Số phần tử lớn hơn trung bình: {dem}")

    # Hoàn thành chương trình
    print("\nChương trình kết thúc.")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

**Hướng dẫn sử dụng:**

1. Lưu mã trên vào file `bai_62_danh_sach_vong_lap.py`
2. Chạy bằng lệnh: `python bai_62_danh_sach_vong_lap.py`
3. Quan sát kết quả in ra màn hình

**Nội dung học được:**
- Tạo, truy cập, duyệt danh sách.
- Sử dụng `for` và `while` để xử lý danh sách.
- Các thao tác thêm, xóa, tìm kiếm, sắp xếp.
- Áp dụng vào bài toán thực tế và giải bài tập nhỏ.