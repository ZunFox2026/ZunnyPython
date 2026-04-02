# Import thư viện cần thiết
from PIL import Image, ImageFilter

# Mở hình ảnh
img = Image.open('image.jpg')

# Hiển thị thông tin hình ảnh
print("Thông tin hình ảnh:")
print("Kích thước:", img.size)
print("Định dạng:", img.format)

# Chuyển đổi hình ảnh sang grayscale
img_gray = img.convert('L')
img_gray.save('image_gray.jpg')

# Áp dụng bộ lọc Gaussian Blur
img_blur = img.filter(ImageFilter.GaussianBlur(radius=5))
img_blur.save('image_blur.jpg')

# Cắt hình ảnh
box = (100, 100, 300, 300)
img_crop = img.crop(box)
img_crop.save('image_crop.jpg')

# Xoay hình ảnh
img_rotate = img.rotate(45)
img_rotate.save('image_rotate.jpg')

# Hiện thị hình ảnh
img.show()
img_gray.show()
img_blur.show()
img_crop.show()
img_rotate.show()