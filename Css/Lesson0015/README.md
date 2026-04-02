# Tạo Hình Nền
Bài này sẽ hướng dẫn bạn cách tạo hình nền cho trang web bằng CSS.

## Giới thiệu
Hình nền là một phần quan trọng của thiết kế web, giúp tạo ấn tượng và thu hút người dùng. Trong bài này, bạn sẽ học cách sử dụng CSS để tạo hình nền cho trang web của mình. Chúng ta sẽ khám phá các thuộc tính khác nhau có thể được sử dụng để tạo hình nền, bao gồm cả cách chọn hình ảnh, màu sắc và các hiệu ứng khác.

Ví dụ, bạn có thể sử dụng thuộc tính `background-color` để đặt màu nền cho trang web:
```css
body {
  background-color: #f2f2f2;
}
```
Hoặc, bạn có thể sử dụng thuộc tính `background-image` để đặt hình ảnh nền:
```css
body {
  background-image: url('hinhnen.jpg');
}
```

## Lý thuyết
Để tạo hình nền, bạn có thể sử dụng các thuộc tính sau:
- `background-color`: đặt màu nền cho trang web.
- `background-image`: đặt hình ảnh nền cho trang web.
- `background-repeat`: đặt cách hình ảnh nền được lặp lại (ví dụ: `repeat`, `no-repeat`, `repeat-x`, `repeat-y`).
- `background-position`: đặt vị trí của hình ảnh nền (ví dụ: `center`, `top`, `bottom`, `left`, `right`).
- `background-size`: đặt kích thước của hình ảnh nền (ví dụ: `cover`, `contain`, `100% 100%`).

Ví dụ, bạn có thể sử dụng các thuộc tính trên như sau:
```css
body {
  background-image: url('hinhnen.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
```

## Ví dụ
Dưới đây là một ví dụ về cách tạo hình nền cho trang web:
```css
body {
  background-image: linear-gradient(to bottom, #f2f2f2, #cccccc);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
```
Ví dụ trên tạo một hình nền với hiệu ứng gradient từ màu `#f2f2f2` đến màu `#cccccc`.

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web với hình nền. Hãy thực hiện các bước sau:
- Tạo một tệp tin HTML mới và thêm một thẻ `body`.
- Thêm một thuộc tính `style` vào thẻ `body` và đặt màu nền hoặc hình ảnh nền cho trang web.
- Thử nghiệm với các thuộc tính khác nhau để tạo ra hiệu ứng hình nền mong muốn.
- Lưu tệp tin và mở nó trong trình duyệt để xem kết quả.

Hãy thử nghiệm và tạo ra một hình nền độc đáo cho trang web của mình!