# Lập Trình Game
Bài học này sẽ giới thiệu về lập trình game cơ bản bằng ngôn ngữ Python.

## Giới thiệu
Lập trình game là một lĩnh vực thú vị và đầy thách thức trong thế giới công nghệ. Với sự phát triển của công nghệ, các trò chơi điện tử đã trở thành một phần không thể thiếu trong cuộc sống hàng ngày. Python là một ngôn ngữ lập trình đơn giản và dễ học, rất phù hợp cho những người mới bắt đầu lập trình game. Trong bài học này, chúng ta sẽ tìm hiểu về các khái niệm cơ bản và cách tạo ra một trò chơi đơn giản bằng Python.

## Lý thuyết
Để lập trình game, chúng ta cần hiểu về các khái niệm như:
- Biến và dữ liệu: dùng để lưu trữ thông tin về trò chơi, như điểm số, vị trí của nhân vật, v.v.
- Hàm và phương thức: dùng để thực hiện các hành động trong trò chơi, như di chuyển nhân vật, kiểm tra va chạm, v.v.
- Vòng lặp và điều kiện: dùng để kiểm soát luồng của trò chơi, như lặp lại một hành động, kiểm tra một điều kiện, v.v.
- Thư viện và mô-đun: dùng để thêm các tính năng mới vào trò chơi, như đồ họa, âm thanh, v.v.

Chúng ta sẽ sử dụng thư viện Pygame, một thư viện phổ biến và dễ sử dụng để lập trình game bằng Python.

## Ví dụ
Dưới đây là một ví dụ đơn giản về trò chơi "Pong" bằng Pygame:
```python
import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ trò chơi
screen = pygame.display.set_mode((800, 600))

# Tạo nhân vật và bóng
paddle = pygame.Rect(375, 275, 50, 50)
ball = pygame.Rect(395, 295, 10, 10)

# Vòng lặp trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        paddle.move_ip(0, 5)

    # Di chuyển bóng
    ball.move_ip(5, 5)

    # Kiểm tra va chạm
    if ball.colliderect(paddle):
        ball.move_ip(-5, -5)

    # Vẽ trò chơi
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.display.flip()

    # Delay
    pygame.time.delay(1000 // 60)
```
Trò chơi này sẽ tạo ra một cửa sổ với một nhân vật và một bóng. Nhân vật có thể di chuyển lên xuống bằng các phím mũi tên, và bóng sẽ di chuyển tự động. Khi bóng va chạm với nhân vật, nó sẽ đổi hướng.

## Bài tập
Bài tập cho bạn:
- Tạo một trò chơi "Snake" bằng Pygame, trong đó nhân vật là một con rắn và mục tiêu là ăn các quả táo.
- Thêm tính năng điểm số và hiển thị điểm số trên màn hình.
- Thêm tính năng âm thanh khi con rắn ăn quả táo hoặc khi trò chơi kết thúc.