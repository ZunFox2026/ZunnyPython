# Tạo hiệu ứng Glow
## Giới thiệu
Hiệu ứng Glow là một kỹ thuật thiết kế giúp tạo ra một bóng sáng xung quanh các yếu tố trên trang web, giúp chúng nổi bật và thu hút sự chú ý của người dùng. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Glow bằng sử dụng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Glow, chúng ta có thể sử dụng thuộc tính `box-shadow` trong CSS. Thuộc tính này cho phép chúng ta tạo ra một bóng tối hoặc bóng sáng xung quanh các yếu tố trên trang web. Để tạo hiệu ứng Glow, chúng ta cần sử dụng giá trị `inset` của thuộc tính `box-shadow` và kết hợp với màu sắc phù hợp.

Ví dụ, chúng ta có thể sử dụng mã CSS sau để tạo hiệu ứng Glow:
```html
<div class="glow">Nội dung</div>
```

```css
.glow {
  box-shadow: 0 0 10px 5px rgba(255, 255, 0, 0.5) inset;
  border-radius: 10px;
  padding: 20px;
  width: 200px;
  height: 100px;
  background-color: #f0f0f0;
}
```
Trong ví dụ trên, chúng ta đã tạo ra một hiệu ứng Glow vàng xung quanh phần tử `div` bằng cách sử dụng thuộc tính `box-shadow` với giá trị `inset` và màu sắc phù hợp.

## Ví dụ
Chúng ta cũng có thể tạo hiệu ứng Glow cho các phần tử khác như hình ảnh, nút bấm, v.v. Dưới đây là một ví dụ về tạo hiệu ứng Glow cho một hình ảnh:
```html
<img src="image.jpg" class="glow-image">
```

```css
.glow-image {
  box-shadow: 0 0 10px 5px rgba(0, 0, 255, 0.5) inset;
  border-radius: 10px;
  padding: 10px;
  width: 300px;
  height: 200px;
}
```
Trong ví dụ này, chúng ta đã tạo ra một hiệu ứng Glow xanh xung quanh hình ảnh bằng cách sử dụng thuộc tính `box-shadow` với giá trị `inset` và màu sắc phù hợp.

## Bài tập
Bài tập của bạn là tạo ra một hiệu ứng Glow cho một nút bấm. Bạn cần sử dụng thuộc tính `box-shadow` và màu sắc phù hợp để tạo ra hiệu ứng Glow. Dưới đây là một ví dụ về HTML và CSS để bạn bắt đầu:
```html
<button class="glow-button">Nút bấm</button>
```

```css
.glow-button {
  /* Thêm mã CSS của bạn ở đây */
}
```
Hãy thử nghiệm với các giá trị khác nhau của thuộc tính `box-shadow` và màu sắc để tạo ra hiệu ứng Glow phù hợp với nhu cầu của bạn.