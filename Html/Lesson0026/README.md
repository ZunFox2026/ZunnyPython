# Tạo hiệu ứng Parallax
## Giới thiệu
Hiệu ứng Parallax là một kỹ thuật thiết kế web tạo ra sự chuyển động của các lớp nền và các phần tử trên trang web khi người dùng cuộn chuột. Hiệu ứng này giúp tạo ra một trải nghiệm người dùng thú vị và hấp dẫn. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Parallax sử dụng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Parallax, chúng ta cần sử dụng thuộc tính `background-attachment` trong CSS. Thuộc tính này cho phép chúng ta đặt một hình nền cố định hoặc di chuyển cùng với nội dung của trang web. Chúng ta cũng cần sử dụng thuộc tính `background-position` để đặt vị trí của hình nền.

Ví dụ về cách sử dụng thuộc tính `background-attachment`:
```html
<div class="parallax">
  <div class="layer1"></div>
  <div class="layer2"></div>
</div>
```

```css
.parallax {
  perspective: 1000px;
}

.layer1 {
  background-image: url('image1.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 100vh;
  width: 100%;
}

.layer2 {
  background-image: url('image2.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 100vh;
  width: 100%;
  transform: translateZ(-1px);
}
```
Trong ví dụ trên, chúng ta tạo hai lớp nền với hai hình ảnh khác nhau. Lớp nền đầu tiên có thuộc tính `background-attachment` là `fixed`, nghĩa là hình nền sẽ cố định khi người dùng cuộn chuột. Lớp nền thứ hai cũng có thuộc tính `background-attachment` là `fixed`, nhưng chúng ta thêm thuộc tính `transform` để tạo hiệu ứng sâu.

## Ví dụ
Chúng ta có thể tạo một trang web đơn giản với hiệu ứng Parallax như sau:
```html
<div class="parallax">
  <div class="layer1"></div>
  <div class="layer2"></div>
  <div class="content">
    <h1>Hiệu ứng Parallax</h1>
    <p>Đây là một trang web với hiệu ứng Parallax.</p>
  </div>
</div>
```

```css
.parallax {
  perspective: 1000px;
}

.layer1 {
  background-image: url('image1.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 100vh;
  width: 100%;
}

.layer2 {
  background-image: url('image2.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 100vh;
  width: 100%;
  transform: translateZ(-1px);
}

.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```
Trong ví dụ trên, chúng ta tạo một trang web với hai lớp nền và một nội dung chính. Khi người dùng cuộn chuột, hai lớp nền sẽ di chuyển tạo ra hiệu ứng Parallax.

## Bài tập
Bài tập cho bạn: Tạo một trang web với hiệu ứng Parallax sử dụng HTML và CSS. Trang web nên có ít nhất hai lớp nền và một nội dung chính. Bạn có thể sử dụng các hình ảnh hoặc màu sắc khác nhau để tạo ra hiệu ứng Parallax thú vị. Hãy thử nghiệm và sáng tạo!