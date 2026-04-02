#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới để viết dữ liệu
    ofstream outFile("example.txt");
    
    // Kiểm tra nếu tệp tin được mở thành công
    if (outFile.is_open()) {
        // Viết dữ liệu vào tệp tin
        outFile << "Xin chào, đây là nội dung của tệp tin example.txt" << endl;
        
        // Đóng tệp tin
        outFile.close();
        cout << "Tệp tin đã được tạo và ghi dữ liệu thành công!" << endl;
    } else {
        cout << "Không thể mở tệp tin để ghi dữ liệu!" << endl;
    }

    // Đọc dữ liệu từ tệp tin
    ifstream inFile("example.txt");
    
    // Kiểm tra nếu tệp tin được mở thành công
    if (inFile.is_open()) {
        string line;
        // Đọc từng dòng dữ liệu từ tệp tin
        while (getline(inFile, line)) {
            // In ra màn hình
            cout << "Nội dung tệp tin: " << line << endl;
        }
        
        // Đóng tệp tin
        inFile.close();
    } else {
        cout << "Không thể mở tệp tin để đọc dữ liệu!" << endl;
    }

    return 0;
}