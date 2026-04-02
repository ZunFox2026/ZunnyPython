# Tạo hiệu ứng Parallax
## Giới thiệu
Hiệu ứng Parallax là một kỹ thuật thiết kế web tạo ra cảm giác sâu và động bằng cách di chuyển các lớp nền và lớp trước với tốc độ khác nhau khi người dùng cuộn trang. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Parallax cơ bản sử dụng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Parallax, bạn cần tạo các lớp chồng lên nhau, mỗi lớp có thể chứa ảnh nền hoặc nội dung khác. Lớp trên cùng sẽ chứa nội dung chính của trang, trong khi các lớp dưới sẽ chứa ảnh nền hoặc các yếu tố đồ họa khác. Khi người dùng cuộn trang, các lớp này sẽ di chuyển với tốc độ khác nhau, tạo ra cảm giác sâu và động.

Ví dụ về cấu trúc HTML và CSS cơ bản để tạo hiệu ứng Parallax:
```html
<div class="parallax-container">
  <div class="parallax-layer layer1"></div>
  <div class="parallax-layer layer2"></div>
  <div class="parallax-content"></div>
</div>
```

```css
.parallax-container {
  perspective: 1000px;
}

.parallax-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
}

.layer1 {
  background-image: url('image1.jpg');
  transform: translateZ(-300px);
}

.layer2 {
  background-image: url('image2.jpg');
  transform: translateZ(-200px);
}
```

## Ví dụ
Dưới đây là ví dụ cụ thể về tạo hiệu ứng Parallax sử dụng HTML và CSS:
```html
<div class="parallax-container">
  <div class="parallax-layer layer1" style="background-image: url('https://example.com/image1.jpg');"></div>
  <div class="parallax-layer layer2" style="background-image: url('https://example.com/image2.jpg');"></div>
  <div class="parallax-content">
    <h1>Tạo hiệu ứng Parallax</h1>
    <p>Đây là ví dụ về tạo hiệu ứng Parallax sử dụng HTML và CSS.</p>
  </div>
</div>
```

```css
.parallax-container {
  perspective: 1000px;
  height: 100vh;
  overflow-x: hidden;
  overflow-y: auto;
}

.parallax-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-attachment: fixed;
}

.layer1 {
  transform: translateZ(-300px);
}

.layer2 {
  transform: translateZ(-200px);
}

.parallax-content {
  position: relative;
  z-index: 1;
  color: #fff;
  text-align: center;
  padding: 20px;
}
```

## Bài tập
Bài tập: Tạo một trang web đơn giản với hiệu ứng Parallax, bao gồm 3 lớp: lớp trên cùng chứa nội dung chính, lớp giữa chứa ảnh nền và lớp dưới cùng chứa ảnh nền khác. Sử dụng HTML và CSS để tạo hiệu ứng Parallax.

Yêu cầu:
- Tạo cấu trúc HTML cho trang web
- Thêm CSS để tạo hiệu ứng Parallax
- Thêm nội dung cho từng lớp
- Kiểm tra hiệu ứng Parallax trên trang web

Ghi chú: Bài tập này giúp bạn thực hành tạo hiệu ứng Parallax và hiểu rõ hơn về cách sử dụng HTML và CSS để tạo ra hiệu ứng này.