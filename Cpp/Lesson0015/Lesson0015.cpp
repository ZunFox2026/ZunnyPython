#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một file mới tên là "example.txt" và mở nó ở chế độ viết
    ofstream outFile("example.txt");
    
    // Kiểm tra nếu file đã được mở thành công
    if (outFile.is_open()) {
        // Viết nội dung vào file
        outFile << "Xin chào, thế giới!" << endl;
        outFile << "Đây là một file mẫu." << endl;
        
        // Đóng file
        outFile.close();
        cout << "File đã được tạo và viết thành công!" << endl;
    } else {
        cout << "Không thể mở file!" << endl;
    }

    // Mở file "example.txt" ở chế độ đọc
    ifstream inFile("example.txt");
    
    // Kiểm tra nếu file đã được mở thành công
    if (inFile.is_open()) {
        // Đọc nội dung từ file và hiển thị trên màn hình
        string line;
        while (getline(inFile, line)) {
            cout << line << endl;
        }
        
        // Đóng file
        inFile.close();
        cout << "File đã được đọc thành công!" << endl;
    } else {
        cout << "Không thể mở file!" << endl;
    }

    return 0;
}