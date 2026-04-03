"""
Python 43: Xử Lý Danh Sách và Vòng Lặp
Mục tiêu: Hiểu cách tạo, thao tác và lặp qua danh sách (list) trong Python.
Bao gồm: vòng lặp for, while, thêm/xóa phần tử, duyệt ngược, và các hàm tiện ích.
"""

def main():
    # === 1. Tạo danh sách ===
    # Danh sách (list) là cấu trúc dữ liệu lưu trữ nhiều phần tử, có thể thay đổi (mutable)
    fruits = ["táo", "chuối", "cam", "xoài"]
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True]

    print("1. Danh sách ban đầu:")
    print("Trái cây:", fruits)
    print("Số:", numbers)
    print("Hỗn hợp:", mixed_list)

    # === 2. Duyệt danh sách bằng vòng lặp for ===
    print("\n2. Duyệt danh sách bằng vòng lặp for:")
    for fruit in fruits:
        print(f"- {fruit}")

    # === 3. Duyệt với chỉ số (index) sử dụng enumerate ===
    print("\n3. Duyệt danh sách với chỉ số:")
    for index, fruit in enumerate(fruits):
        print(f"  [{index}] {fruit}")

    # === 4. Duyệt ngược danh sách ===
    print("\n4. Duyệt ngược danh sách:")
    for fruit in reversed(fruits):
        print(f"- {fruit}")

    # === 5. Duyệt bằng vòng lặp while ===
    print("\n5. Duyệt bằng vòng lặp while:")
    i = 0
    while i < len(fruits):
        print(f"  {i + 1}. {fruits[i]}")
        i += 1

    # === 6. Thêm phần tử vào danh sách ===
    print("\n6. Thêm phần tử:")
    fruits.append("dưa hấu")  # Thêm vào cuối
    fruits.insert(1, "sầu riêng")  # Chèn vào vị trí 1
    print("Sau khi thêm:", fruits)

    # === 7. Xóa phần tử khỏi danh sách ===
    print("\n7. Xóa phần tử:")
    fruits.remove("cam")  # Xóa theo giá trị
    del fruits[0]  # Xóa theo chỉ số
    print("Sau khi xóa:", fruits)

    # === 8. Cập nhật phần tử ===
    print("\n8. Cập nhật phần tử:")
    fruits[1] = "nho"
    print("Sau khi cập nhật:", fruits)

    # === 9. Tìm kiếm phần tử ===
    print("\n9. Tìm kiếm phần tử:")
    if "xoài" in fruits:
        print("Tìm thấy xoài trong danh sách!")
    else:
        print("Không tìm thấy xoài.")

    # === 10. Sắp xếp danh sách ===
    print("\n10. Sắp xếp danh sách:")
    fruits.sort()  # Sắp xếp tăng dần
    print("Sau sắp xếp:", fruits)

    # === 11. Danh sách số: Tính tổng, giá trị lớn/nhỏ ===
    print("\n11. Xử lý danh sách số:")
    print("Tổng các số:", sum(numbers))
    print("Số lớn nhất:", max(numbers))
    print("Số nhỏ nhất:", min(numbers))

    # === 12. Tạo danh sách mới từ danh sách cũ (list comprehension) ===
    print("\n12. Tạo danh sách bình phương bằng list comprehension:")
    squares = [x ** 2 for x in numbers]
    print("Bình phương các số:", squares)

    # === 13. Ví dụ thực tế: Tính điểm trung bình học sinh ===
    print("\n=== Ví dụ 1: Tính điểm trung bình ===")
    diem_toan = [8, 9, 7, 10, 6, 8, 9]
    diem_tb = sum(diem_toan) / len(diem_toan)
    print("Điểm môn Toán:", diem_toan)
    print(f"Điểm trung bình: {diem_tb:.2f}")

    # === 14. Ví dụ: Đếm số lượng phần tử thỏa điều kiện ===
    print("\n=== Ví dụ 2: Đếm số điểm >= 8 ===")
    so_luong_gioi = sum(1 for diem in diem_toan if diem >= 8)
    print(f"Có {so_luong_gioi} học sinh đạt điểm từ 8 trở lên.")

    # === Bài tập nhỏ ===
    print("\n=== Bài tập nhỏ: ===")
    print("Cho danh sách điểm lý: [7, 5, 9, 8, 6, 10, 7]")
    print("Yêu cầu:")
    print("1. In ra các điểm lớn hơn hoặc bằng 8")
    print("2. Tính điểm trung bình")
    print("3. Sắp xếp điểm theo thứ tự giảm dần")

    # Giải bài tập
    diem_ly = [7, 5, 9, 8, 6, 10, 7]
    print("\n-- Giải bài tập --")
    print("1. Các điểm >= 8:", [diem for diem in diem_ly if diem >= 8])
    print("2. Điểm trung bình:", round(sum(diem_ly) / len(diem_ly), 2))
    print("3. Sắp xếp giảm dần:", sorted(diem_ly, reverse=True))

    print("\nChương trình kết thúc.")


# Gọi hàm main để thực thi
if __name__ == "__main__":
    main()
```

---

**Tóm tắt nội dung:**
- Giới thiệu danh sách và các thao tác cơ bản: thêm, xóa, sửa, duyệt.
- Sử dụng `for`, `while`, `enumerate`, `reversed`.
- Ứng dụng thực tế: tính điểm trung bình, lọc dữ liệu.
- Bài tập nhỏ kèm lời giải để luyện tập.

> ✅ Chạy file Python này để xem kết quả và hiểu cách hoạt động của danh sách và vòng lặp trong Python.