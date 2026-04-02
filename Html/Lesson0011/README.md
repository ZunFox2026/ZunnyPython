# Tạo Trang Web Về Du Lịch
## Giới thiệu
Trong bài học này, chúng ta sẽ tìm hiểu cách tạo một trang web về du lịch bằng sử dụng HTML và CSS. Bài học này sẽ giúp bạn hiểu rõ hơn về cách tạo cấu trúc trang web, thêm nội dung và thiết kế giao diện bằng CSS. Đây là một chủ đề thú vị và phù hợp cho những người mới bắt đầu học về phát triển web.

## Lý thuyết
Trước khi bắt đầu tạo trang web, chúng ta cần hiểu một số khái niệm cơ bản về HTML và CSS. HTML (HyperText Markup Language) là ngôn ngữ đánh dấu được sử dụng để tạo cấu trúc và nội dung của trang web. CSS (Cascading Style Sheets) là ngôn ngữ được sử dụng để thiết kế giao diện và bố cục của trang web.

Ví dụ về HTML và CSS cơ bản:
```html
<html>
<head>
<title>Trang Web Về Du Lịch</title>
</head>
<body>
<h1>Chào mừng đến với trang web về du lịch!</h1>
<p>Đây là trang web về du lịch, nơi bạn có thể tìm thấy thông tin về các điểm du lịch hấp dẫn.</p>
</body>
</html>
```
Và CSS:
```css
body {
background-color: #f2f2f2;
font-family: Arial, sans-serif;
}

h1 {
color: #00698f;
}
```
## Ví dụ
Giả sử chúng ta muốn tạo một trang web về du lịch với các phần chính: giới thiệu, điểm du lịch, và liên hệ. Chúng ta có thể sử dụng HTML và CSS như sau:

HTML:
```html
<html>
<head>
<title>Trang Web Về Du Lịch</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<h1>Trang Web Về Du Lịch</h1>
<nav>
<ul>
<li><a href="#gioi-thieu">Giới thiệu</a></li>
<li><a href="#diem-du-lich">Điểm du lịch</a></li>
<li><a href="#lien-he">Liên hệ</a></li>
</ul>
</nav>
</header>
<section id="gioi-thieu">
<h2>Giới thiệu</h2>
<p>Chào mừng đến với trang web về du lịch!</p>
</section>
<section id="diem-du-lich">
<h2>Điểm du lịch</h2>
<ul>
<li>Điểm du lịch 1</li>
<li>Điểm du lịch 2</li>
<li>Điểm du lịch 3</li>
</ul>
</section>
<section id="lien-he">
<h2>Liên hệ</h2>
<p>Để biết thêm thông tin, vui lòng liên hệ với chúng tôi.</p>
</section>
</body>
</html>
```
Và CSS (trong file style.css):
```css
body {
background-color: #f2f2f2;
font-family: Arial, sans-serif;
}

header {
background-color: #00698f;
color: #ffffff;
padding: 20px;
text-align: center;
}

nav ul {
list-style: none;
margin: 0;
padding: 0;
}

nav li {
display: inline-block;
margin-right: 20px;
}

nav a {
color: #ffffff;
text-decoration: none;
}

section {
padding: 20px;
}

h2 {
color: #00698f;
}
```
## Bài tập
Bài tập này yêu cầu bạn tạo một trang web về du lịch với các phần chính: giới thiệu, điểm du lịch, và liên hệ. Bạn cần sử dụng HTML và CSS để tạo cấu trúc và thiết kế giao diện cho trang web.

Yêu cầu:

* Tạo một file HTML với tên `index.html`
* Tạo một file CSS với tên `style.css`
* Thêm nội dung và cấu trúc cho trang web bằng HTML
* Thiết kế giao diện cho trang web bằng CSS
* Thêm liên kết giữa các phần của trang web

Khi hoàn thành bài tập, bạn sẽ có một trang web về du lịch hoàn chỉnh với cấu trúc và giao diện đẹp. Chúc bạn thành công!