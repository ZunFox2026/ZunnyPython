# Lập Trình Game bằng Python
# Sử dụng thư viện Pygame

import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước màn hình
man_hinh = pygame.display.set_mode((800, 600))

# Thiết lập tiêu đề màn hình
pygame.display.set_caption('Lập Trình Game')

# Thiết lập màu sắc
mau_den = (0, 0, 0)
mau_trang = (255, 255, 255)

# Thiết lập font chữ
font = pygame.font.Font(None, 36)

# Hàm vẽ chữ lên màn hình
def ve_chu(chu, x, y):
    chu_ve = font.render(chu, True, mau_den)
    man_hinh.blit(chu_ve, (x, y))

# Hàm vẽ hình chữ nhật lên màn hình
def ve_hinh_chu_nhat(x, y, rong, cao, mau):
    pygame.draw.rect(man_hinh, mau, (x, y, rong, cao))

# Vòng lặp chính của game
while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu trắng
    man_hinh.fill(mau_trang)

    # Vẽ hình chữ nhật màu đen
    ve_hinh_chu_nhat(100, 100, 200, 200, mau_den)

    # Vẽ chữ lên màn hình
    ve_chu('Lập Trình Game', 300, 300)

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt tốc độ khung hình
    pygame.time.Clock().tick(60)