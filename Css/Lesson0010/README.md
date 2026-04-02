# Tạo Hình Nền
Bài 10: Tạo Hình Nền là một phần quan trọng trong khóa học Cơ bản về CSS. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hình nền cho trang web của mình bằng cách sử dụng các thuộc tính CSS.

## Giới thiệu
Hình nền là một phần quan trọng của thiết kế web, giúp tạo ấn tượng và thu hút người dùng. Với CSS, chúng ta có thể tạo hình nền dễ dàng và linh hoạt. Bài này sẽ giới thiệu các phương pháp tạo hình nền cơ bản và cung cấp ví dụ minh họa.

## Lý thuyết
Để tạo hình nền, chúng ta sử dụng thuộc tính `background` trong CSS. Thuộc tính này cho phép chúng ta đặt hình ảnh hoặc màu sắc làm hình nền cho phần tử HTML. Dưới đây là một số ví dụ về cách sử dụng thuộc tính `background`:
- `background-color`: đặt màu sắc cho hình nền
- `background-image`: đặt hình ảnh cho hình nền
- `background-repeat`: đặt cách hình nền được lặp lại
- `background-position`: đặt vị trí của hình nền

Ví dụ:
```css
body {
  background-color: #f2f2f2; /* đặt màu sắc cho hình nền */
  background-image: url('hinhnen.jpg'); /* đặt hình ảnh cho hình nền */
  background-repeat: no-repeat; /* không lặp lại hình nền */
  background-position: center; /* đặt vị trí của hình nền */
}
```

## Ví dụ
Chúng ta có thể tạo một trang web đơn giản với hình nền như sau:
```css
body {
  background-image: url('hinhnen.jpg');
  background-size: cover; /* đặt kích thước hình nền */
  background-attachment: fixed; /* cố định hình nền khi cuộn trang */
}

.container {
  width: 80%;
  margin: 40px auto;
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
```
Trong ví dụ này, chúng ta tạo một trang web với hình nền là hình ảnh `hinhnen.jpg`. Chúng ta cũng tạo một phần tử `.container` với màu sắc và hiệu ứng bóng đổ.

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web với hình nền là hình ảnh mà bạn chọn. Bạn cần:
- Tạo một file HTML và thêm phần tử `body`
- Tạo một file CSS và thêm thuộc tính `background` cho phần tử `body`
- Thêm hình ảnh làm hình nền và đặt các thuộc tính `background-repeat`, `background-position` và `background-size` cho phù hợp
- Tạo một phần tử `.container` với màu sắc và hiệu ứng bóng đổ như trong ví dụ trên
- Thử nghiệm với các thuộc tính `background` khác nhau để tạo ra các hiệu ứng hình nền khác nhau.