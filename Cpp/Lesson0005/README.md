# Làm quen với cấu trúc dữ liệu và thuật toán
## Giới thiệu
Cấu trúc dữ liệu và thuật toán là nền tảng quan trọng của lập trình máy tính. Cấu trúc dữ liệu giúp chúng ta tổ chức và lưu trữ dữ liệu một cách hiệu quả, trong khi thuật toán cho phép chúng ta thực hiện các hoạt động trên dữ liệu đó. Trong bài này, chúng ta sẽ tìm hiểu về các loại cấu trúc dữ liệu và thuật toán cơ bản, cũng như cách áp dụng chúng vào lập trình C++.

## Lý thuyết
Có nhiều loại cấu trúc dữ liệu, bao gồm mảng, danh sách liên kết,堆, và cây. Mỗi loại cấu trúc dữ liệu có những ưu và nhược điểm riêng, và được sử dụng trong các tình huống khác nhau. Ví dụ, mảng là một cấu trúc dữ liệu đơn giản và hiệu quả, nhưng nó có hạn chế về kích thước và không thể thay đổi được. Danh sách liên kết, mặt khác, cho phép chúng ta thêm và xóa các phần tử một cách linh hoạt, nhưng nó có thể phức tạp hơn và tốn nhiều bộ nhớ.

Ví dụ về khai báo và sử dụng mảng trong C++:
```cpp
int arr[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
    std::cout << arr[i] << " ";
}
```
## Ví dụ
Một ví dụ khác là sử dụng danh sách liên kết để lưu trữ và hiển thị một danh sách các số nguyên. Chúng ta có thể sử dụng lớp `std::list` trong C++ để tạo một danh sách liên kết.
```cpp
#include <list>
#include <iostream>

int main() {
    std::list<int> lst = {1, 2, 3, 4, 5};
    for (int num : lst) {
        std::cout << num << " ";
    }
    return 0;
}
```
## Bài tập
Bài tập 1: Tạo một mảng có kích thước 10 và lưu trữ các số nguyên từ 1 đến 10 vào đó. Sau đó, hãy hiển thị tất cả các phần tử trong mảng.
Bài tập 2: Sử dụng danh sách liên kết để lưu trữ và hiển thị một danh sách các số nguyên. Hãy thêm và xóa các phần tử từ danh sách và hiển thị kết quả sau mỗi thao tác.
Bài tập 3: Tìm hiểu về cấu trúc dữ liệu堆 và cây, và hãy tạo một chương trình C++ để kiểm tra kiến thức của bạn về các cấu trúc dữ liệu này.