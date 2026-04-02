## Giới thiệu
Trong thiết kế web, hình nền là một phần quan trọng giúp trang web trở nên bắt mắt và thu hút. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hình nền bằng CSS. Bạn sẽ học được cách sử dụng thuộc tính `background` để thêm hình nền vào trang web của mình.

## Lý thuyết
Để tạo hình nền, bạn có thể sử dụng thuộc tính `background` trong CSS. Thuộc tính này cho phép bạn thêm hình nền vào một phần tử HTML. Có nhiều cách để sử dụng thuộc tính `background`, bao gồm:
- `background-color`: đặt màu nền cho phần tử
- `background-image`: đặt hình ảnh làm nền cho phần tử
- `background-repeat`: quy định cách hình nền sẽ được lặp lại
- `background-position`: quy định vị trí của hình nền

Ví dụ:
```css
body {
  background-color: #f2f2f2; /* đặt màu nền */
  background-image: url('hinhnen.jpg'); /* đặt hình ảnh làm nền */
  background-repeat: no-repeat; /* không lặp lại hình nền */
  background-position: center; /* đặt hình nền ở vị trí trung tâm */
}
```

## Ví dụ
Chúng ta có thể tạo một trang web đơn giản với hình nền bằng cách sử dụng CSS. Ví dụ, chúng ta có một đoạn mã HTML như sau:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Trang web của tôi</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <h1>Chào mừng đến trang web của tôi!</h1>
</body>
</html>
```
Và đoạn mã CSS như sau:
```css
body {
  background-image: linear-gradient(to bottom, #33ccff, #ffffff);
  background-attachment: fixed;
}

h1 {
  color: #00698f;
  text-align: center;
}
```
Kết quả sẽ là một trang web với hình nền màu xanh biển và chữ màu xanh đậm.

## Bài tập
Bài tập của bạn là tạo một trang web đơn giản với hình nền bằng cách sử dụng CSS. Hãy thực hiện các bước sau:
- Tạo một file HTML mới và thêm đoạn mã HTML đơn giản vào đó
- Tạo một file CSS mới và thêm đoạn mã CSS để tạo hình nền
- Thêm thuộc tính `background` vào file CSS để tạo hình nền
- Thử nghiệm với các thuộc tính `background` khác nhau để tạo ra các hiệu ứng khác nhau
- Đặt hình nền ở vị trí trung tâm và không lặp lại
- Thêm màu nền và hình ảnh làm nền vào trang web của bạn.