import socket

# Tạo một socket mới
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Đặt địa chỉ và cổng cho socket
dia_chi = '127.0.0.1'
cong = 12345

# Bind socket với địa chỉ và cổng
server_socket.bind((dia_chi, cong))

# Listen đến các kết nối từ client
server_socket.listen(1)

print(f"Server đang chạy tại {dia_chi}:{cong}")

# Chấp nhận kết nối từ client
client_socket, dia_chi_client = server_socket.accept()
print(f"Đã kết nối với client tại {dia_chi_client}")

# Nhận dữ liệu từ client
du_lieu = client_socket.recv(1024)
print(f"Client gửi: {du_lieu.decode()}")

# Gửi dữ liệu về client
client_socket.sendall(b"Xin chào client!")

# Đóng kết nối
client_socket.close()
server_socket.close()