# Làm quen với thư viện NumPy
## Giới thiệu
Thư viện NumPy (Numerical Python) là một thư viện quan trọng trong Python, được sử dụng rộng rãi trong lĩnh vực khoa học máy tính, phân tích dữ liệu và trí tuệ nhân tạo. NumPy cung cấp hỗ trợ cho các mảng và ma trận lớn, cùng với một tập hợp lớn các hàm toán học để操作 chúng. Trong bài này, chúng ta sẽ tìm hiểu về cách làm quen với thư viện NumPy và cách sử dụng nó trong các ứng dụng thực tế.

## Lý thuyết
NumPy cung cấp một số tính năng quan trọng, bao gồm:
- **Mảng và ma trận**: NumPy cho phép tạo và xử lý các mảng và ma trận lớn một cách hiệu quả.
- **Hàm toán học**: NumPy cung cấp một tập hợp lớn các hàm toán học, bao gồm cả các hàm cơ bản như cộng, trừ, nhân, chia, và các hàm phức tạp hơn như sin, cos, exp, v.v.
- **Tính toán vector**: NumPy cho phép thực hiện các tính toán vector một cách hiệu quả, giúp giảm thiểu thời gian và tăng tốc độ xử lý dữ liệu.
- **Hỗ trợ cho các loại dữ liệu khác nhau**: NumPy hỗ trợ cho các loại dữ liệu khác nhau, bao gồm số nguyên, số thực, chuỗi, và các loại dữ liệu khác.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng thư viện NumPy:
- Tạo một mảng NumPy: `import numpy as np; arr = np.array([1, 2, 3, 4, 5])`
- Thực hiện các phép toán cơ bản: `arr + 2`, `arr * 2`, `arr / 2`
- Sử dụng các hàm toán học: `np.sin(arr)`, `np.cos(arr)`, `np.exp(arr)`
- Tính toán vector: `arr1 = np.array([1, 2, 3]); arr2 = np.array([4, 5, 6]); arr1 + arr2`

## Bài tập
Để nắm vững kiến thức về thư viện NumPy, bạn có thể thực hiện các bài tập sau:
- Tạo một mảng NumPy từ một danh sách các số thực.
- Thực hiện các phép toán cơ bản trên mảng NumPy.
- Sử dụng các hàm toán học để tính toán các giá trị sin, cos, exp của một mảng NumPy.
- Tính toán vector giữa hai mảng NumPy.
- Đọc và viết dữ liệu từ/to một tệp tin bằng cách sử dụng các hàm của NumPy.