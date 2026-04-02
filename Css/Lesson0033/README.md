# Tạo hình nền động
## Giới thiệu
Bài học này sẽ hướng dẫn bạn cách tạo hình nền động bằng CSS. Hình nền động là một kỹ thuật thường được sử dụng trong thiết kế web để tạo ra hiệu ứng chuyển động trên trang web. Với CSS, bạn có thể tạo ra các hiệu ứng chuyển động đơn giản mà không cần sử dụng JavaScript.

## Lý thuyết
Để tạo hình nền động, bạn cần sử dụng thuộc tính `background` trong CSS. Thuộc tính `background` cho phép bạn đặt hình nền cho một phần tử HTML. Bạn cũng cần sử dụng thuộc tính `animation` để tạo ra hiệu ứng chuyển động.

Ví dụ, bạn có thể sử dụng CSS như sau:
```css
.background {
  background-image: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 400% 400%;
  animation: move 10s ease infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta tạo ra một hình nền động bằng cách sử dụng thuộc tính `background-image` để đặt hình nền và thuộc tính `animation` để tạo ra hiệu ứng chuyển động.

## Ví dụ
Dưới đây là một ví dụ cụ thể về cách tạo hình nền động bằng CSS:
```css
body {
  margin: 0;
  padding: 0;
  background-image: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 400% 400%;
  animation: move 10s ease infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ này, chúng ta tạo ra một hình nền động cho toàn bộ trang web bằng cách sử dụng thuộc tính `background-image` và `animation`.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một hình nền động bằng CSS. Hãy thực hiện các bước sau:
- Tạo một tệp HTML mới và thêm một phần tử `div` vào trong đó.
- Thêm CSS vào tệp HTML để tạo ra hình nền động cho phần tử `div`.
- Sử dụng thuộc tính `background-image` để đặt hình nền và thuộc tính `animation` để tạo ra hiệu ứng chuyển động.
- Thử nghiệm với các giá trị khác nhau của thuộc tính `background-size` và `animation` để tạo ra các hiệu ứng chuyển động khác nhau.