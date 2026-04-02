# Bài 35: Làm việc với tệp hình ảnh
# Sử dụng thư viện Pillow để làm việc với hình ảnh

from PIL import Image

# Mở hình ảnh
def mo_hinh_anh(ten_tap_tin):
    try:
        # Mở hình ảnh từ tệp tin
        hinh_anh = Image.open(ten_tap_tin)
        # Hiển thị thông tin về hình ảnh
        print("Thông tin hình ảnh:")
        print(f"Kích thước: {hinh_anh.size}")
        print(f"Độ phân giải: {hinh_anh.mode}")
        return hinh_anh
    except Exception as e:
        print(f"Không thể mở hình ảnh: {e}")

# Lưu hình ảnh
def luu_hinh_anh(hinh_anh, ten_tap_tin):
    try:
        # Lưu hình ảnh vào tệp tin
        hinh_anh.save(ten_tap_tin)
        print(f"Hình ảnh đã được lưu vào {ten_tap_tin}")
    except Exception as e:
        print(f"Không thể lưu hình ảnh: {e}")

# Chỉnh sửa hình ảnh
def chinh_sua_hinh_anh(hinh_anh):
    try:
        # Chuyển hình ảnh sang grayscale
        hinh_anh_grayscale = hinh_anh.convert('L')
        return hinh_anh_grayscale
    except Exception as e:
        print(f"Không thể chỉnh sửa hình ảnh: {e}")

# Chương trình chính
if __name__ == "__main__":
    ten_tap_tin = "test.jpg"
    hinh_anh = mo_hinh_anh(ten_tap_tin)
    if hinh_anh:
        hinh_anh_grayscale = chinh_sua_hinh_anh(hinh_anh)
        if hinh_anh_grayscale:
            luu_hinh_anh(hinh_anh_grayscale, "test_grayscale.jpg")