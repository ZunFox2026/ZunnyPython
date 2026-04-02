# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin trên máy tính. Trong C++, bạn có thể sử dụng các lớp và hàm có sẵn để thực hiện các tác vụ này. Bài viết này sẽ giới thiệu về cách làm việc với tệp tin trong C++.

## Lý thuyết
Để làm việc với tệp tin trong C++, bạn cần sử dụng thư viện `fstream`. Thư viện này cung cấp các lớp như `ifstream`, `ofstream` và `fstream` để đọc và viết tệp tin.

- `ifstream`: Sử dụng để đọc tệp tin.
- `ofstream`: Sử dụng để viết tệp tin.
- `fstream`: Sử dụng để đọc và viết tệp tin.

Ngoài ra, bạn cũng cần biết về các mode mở tệp tin:
- `ios::in`: Mở tệp tin để đọc.
- `ios::out`: Mở tệp tin để viết.
- `ios::app`: Mở tệp tin để thêm dữ liệu vào cuối tệp tin.
- `ios::trunc`: Mở tệp tin và xóa nội dung hiện tại.
- `ios::binary`: Mở tệp tin ở chế độ binary.

Ví dụ:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream file("example.txt", std::ios::out);
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    } else {
        std::cout << "Không thể mở tệp tin.";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và viết tệp tin trong C++:

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Tạo tệp tin và viết nội dung
    std::ofstream outFile("example.txt", std::ios::out);
    if (outFile.is_open()) {
        outFile << "Dòng 1" << std::endl;
        outFile << "Dòng 2" << std::endl;
        outFile.close();
    } else {
        std::cout << "Không thể mở tệp tin để viết.";
    }

    // Đọc nội dung từ tệp tin
    std::ifstream inFile("example.txt", std::ios::in);
    if (inFile.is_open()) {
        std::string line;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "Không thể mở tệp tin để đọc.";
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để ghi một danh sách sinh viên vào tệp tin `sinh_vien.txt`. Mỗi sinh viên có thông tin включ tên, tuổi và điểm trung bình.

Bài tập 2: Đọc nội dung từ tệp tin `sinh_vien.txt` và hiển thị thông tin của từng sinh viên ra màn hình.

Bài tập 3: Thêm chức năng để người dùng có thể thêm, xóa, sửa thông tin sinh viên trong tệp tin.