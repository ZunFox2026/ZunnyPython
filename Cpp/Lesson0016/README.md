# Xử lý tệp
## Giới thiệu
Xử lý tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp trên thiết bị. Trong C++, chúng ta có thể sử dụng các lớp và hàm trong thư viện chuẩn để thực hiện việc này. Bài viết này sẽ giới thiệu về cách xử lý tệp trong C++.

## Lý thuyết
Trong C++, có hai loại tệp chính: tệp văn bản (text file) và tệp nhị phân (binary file). Tệp văn bản lưu trữ dữ liệu dưới dạng văn bản, trong khi tệp nhị phân lưu trữ dữ liệu dưới dạng nhị phân. Để xử lý tệp, chúng ta cần sử dụng các hàm và lớp sau:
- `fstream`: lớp này cho phép chúng ta đọc và ghi tệp.
- `ifstream`: lớp này cho phép chúng ta đọc tệp.
- `ofstream`: lớp này cho phép chúng ta ghi tệp.
- `open()`: hàm này mở tệp để đọc hoặc ghi.
- `close()`: hàm này đóng tệp sau khi đọc hoặc ghi.
- `read()`: hàm này đọc dữ liệu từ tệp.
- `write()`: hàm này ghi dữ liệu vào tệp.

Ví dụ về cách mở và đóng tệp:
```cpp
#include <fstream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào!";
        file.close();
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và ghi tệp văn bản:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Ghi tệp
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào!\n";
        file << "Đây là một ví dụ về xử lý tệp.";
        file.close();
    }

    // Đọc tệp
    std::ifstream readFile("example.txt");
    if (readFile.is_open()) {
        std::string line;
        while (std::getline(readFile, line)) {
            std::cout << line << std::endl;
        }
        readFile.close();
    }
    return 0;
}
```

## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình C++ để quản lý danh sách sinh viên. Chương trình sẽ có các chức năng sau:
- Thêm sinh viên: thêm một sinh viên mới vào danh sách.
- Liệt kê sinh viên: liệt kê tất cả các sinh viên trong danh sách.
- Lưu danh sách: lưu danh sách sinh viên vào một tệp văn bản.
- Đọc danh sách: đọc danh sách sinh viên từ một tệp văn bản.

Yêu cầu:
- Tạo một cấu trúc `SinhVien` để lưu trữ thông tin về một sinh viên.
- Tạo các hàm để thêm, liệt kê, lưu và đọc danh sách sinh viên.
- Sử dụng các lớp và hàm trong thư viện chuẩn C++ để xử lý tệp.

Khi hoàn thành, chương trình sẽ có thể thêm, liệt kê, lưu và đọc danh sách sinh viên từ một tệp văn bản.