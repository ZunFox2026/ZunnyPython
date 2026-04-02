# Tạo hiệu ứng glow cho văn bản
## Giới thiệu
Trong thiết kế web, hiệu ứng glow (hiệu ứng phát sáng) cho văn bản có thể giúp thu hút sự chú ý của người dùng và tạo ra điểm nhấn trên trang web. Bài viết này sẽ hướng dẫn cách tạo hiệu ứng glow cho văn bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng glow cho văn bản, chúng ta có thể sử dụng thuộc tính `text-shadow` trong CSS. Thuộc tính này cho phép chúng ta tạo ra bóng cho văn bản, và bằng cách điều chỉnh các giá trị của thuộc tính này, chúng ta có thể tạo ra hiệu ứng glow.

Cú pháp của thuộc tính `text-shadow` như sau:
```html
text-shadow: offset-x offset-y blur-radius color;
```
Trong đó:
- `offset-x` và `offset-y` là giá trị X và Y của bóng văn bản, tính từ vị trí ban đầu của văn bản.
- `blur-radius` là giá trị làm mờ bóng văn bản.
- `color` là màu của bóng văn bản.

Ví dụ:
```html
<p style="text-shadow: 0 0 10px yellow;">Văn bản có hiệu ứng glow</p>
```
Trong ví dụ trên, văn bản sẽ có hiệu ứng glow màu vàng với độ mờ 10px.

## Ví dụ
Dưới đây là một ví dụ minh họa cách tạo hiệu ứng glow cho văn bản bằng HTML và CSS:
```html
<html>
<head>
<style>
.glow {
  font-size: 36px;
  text-shadow: 0 0 10px yellow;
}
</style>
</head>
<body>
<p class="glow">Văn bản có hiệu ứng glow</p>
</body>
</html>
```
Trong ví dụ trên, chúng ta định nghĩa một lớp CSS có tên là `.glow` với thuộc tính `text-shadow` để tạo hiệu ứng glow cho văn bản. Sau đó, chúng ta áp dụng lớp này cho phần tử `p` trong HTML.

## Bài tập
Bài tập: Tạo một trang web với một đoạn văn bản có hiệu ứng glow màu xanh lá cây. Đoạn văn bản nên có kích thước font là 24px và độ mờ của hiệu ứng glow là 5px.

Gợi ý: Sử dụng thuộc tính `text-shadow` trong CSS để tạo hiệu ứng glow cho văn bản. Điều chỉnh các giá trị của thuộc tính này để đạt được hiệu ứng mong muốn.