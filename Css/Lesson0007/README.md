# Tìm hiểu về Shadow
## Giới thiệu
Shadow là một thuộc tính trong CSS giúp tạo ra bóng cho các phần tử HTML. Bóng này có thể được sử dụng để tạo ra hiệu ứng chiều sâu, làm cho trang web trở nên hấp dẫn và thu hút hơn. Trong bài học này, chúng ta sẽ tìm hiểu về cách sử dụng thuộc tính Shadow trong CSS.

## Lý thuyết
Thuộc tính Shadow trong CSS được sử dụng để tạo ra bóng cho các phần tử HTML. Có hai loại bóng chính: bóng trong (box-shadow) và bóng ngoài (text-shadow). Bóng trong được sử dụng để tạo ra bóng cho các phần tử khối, trong khi bóng ngoài được sử dụng để tạo ra bóng cho văn bản.
Để tạo ra bóng trong, chúng ta sử dụng thuộc tính `box-shadow` với cú pháp sau:
```css
box-shadow: offset-x offset-y blur-radius spread-radius color;
```
Trong đó:
- `offset-x` và `offset-y` là giá trị xác định vị trí của bóng so với phần tử.
- `blur-radius` là giá trị xác định mức độ mờ của bóng.
- `spread-radius` là giá trị xác định mức độ lan rộng của bóng.
- `color` là giá trị xác định màu của bóng.
Ví dụ:
```css
div {
  box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.5);
}
```
Để tạo ra bóng ngoài, chúng ta sử dụng thuộc tính `text-shadow` với cú pháp sau:
```css
text-shadow: offset-x offset-y blur-radius color;
```
Trong đó:
- `offset-x` và `offset-y` là giá trị xác định vị trí của bóng so với văn bản.
- `blur-radius` là giá trị xác định mức độ mờ của bóng.
- `color` là giá trị xác định màu của bóng.
Ví dụ:
```css
p {
  text-shadow: 2px 2px 5px rgba(0,0,0,0.5);
}
```
## Ví dụ
Chúng ta có thể sử dụng thuộc tính Shadow để tạo ra hiệu ứng chiều sâu cho các phần tử HTML. Ví dụ, chúng ta có thể tạo ra một nút bấm với bóng như sau:
```css
button {
  box-shadow: 5px 5px 10px 0px rgba(0,0,0,0.5);
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}
```
Khi chúng ta di chuột qua nút bấm, bóng sẽ tạo ra hiệu ứng chiều sâu, làm cho nút bấm trở nên nổi bật hơn.

## Bài tập
Bài tập cho bạn:
- Tạo ra một trang web với một nút bấm có bóng.
- Tạo ra một đoạn văn bản có bóng.
- Thử nghiệm với các giá trị khác nhau của thuộc tính Shadow để tạo ra hiệu ứng chiều sâu khác nhau.
Lưu ý: Bạn có thể sử dụng các giá trị khác nhau của thuộc tính Shadow để tạo ra hiệu ứng chiều sâu khác nhau. Hãy thử nghiệm và tìm ra giá trị phù hợp cho trang web của bạn.