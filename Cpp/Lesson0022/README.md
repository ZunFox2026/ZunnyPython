# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và truy xuất dữ liệu từ tệp tin. Trong C++, bạn có thể sử dụng các hàm và lớp để đọc và ghi tệp tin. Bài viết này sẽ giới thiệu về cách làm việc với tệp tin trong C++.

## Lý thuyết
Trong C++, có hai loại tệp tin chính: tệp tin văn bản (text file) và tệp tin nhị phân (binary file). Tệp tin văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp tin nhị phân chứa dữ liệu dưới dạng mã máy. Để làm việc với tệp tin, bạn cần sử dụng các hàm và lớp sau:
- `fstream`: lớp cơ bản để làm việc với tệp tin.
- `ifstream`: lớp để đọc tệp tin.
- `ofstream`: lớp để ghi tệp tin.
- `fstream`: lớp để đọc và ghi tệp tin.

Ví dụ, để mở một tệp tin văn bản để đọc, bạn có thể sử dụng lớp `ifstream` như sau:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::cout << "Tệp tin đã được mở." << std::endl;
        file.close();
    } else {
        std::cout << "Không thể mở tệp tin." << std::endl;
    }
    return 0;
}
```

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi tệp tin văn bản:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Ghi tệp tin
    std::ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào, thế giới!" << std::endl;
        outFile.close();
        std::cout << "Đã ghi tệp tin thành công." << std::endl;
    } else {
        std::cout << "Không thể ghi tệp tin." << std::endl;
    }

    // Đọc tệp tin
    std::ifstream inFile("example.txt");
    if (inFile.is_open()) {
        std::string line;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "Không thể đọc tệp tin." << std::endl;
    }
    return 0;
}
```

## Bài tập
Bài tập này yêu cầu bạn thực hiện các việc sau:
- Tạo một tệp tin văn bản mới có tên là "bai_tap.txt".
- Ghi nội dung "Xin chào, thế giới!" vào tệp tin đó.
- Đọc nội dung của tệp tin và hiển thị ra màn hình.
- Đóng tệp tin và thông báo về việc đã thực hiện thành công hoặc không thành công.
Hãy thử viết code để giải quyết bài tập này dựa trên kiến thức đã học về làm việc với tệp tin trong C++.