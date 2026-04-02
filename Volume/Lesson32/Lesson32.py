import requests

# Gửi yêu cầu GET đến địa chỉ URL
url = 'https://www.google.com'
response = requests.get(url)

# Kiểm tra trạng thái của yêu cầu
if response.status_code == 200:
    print('Yêu cầu thành công')
else:
    print('Yêu cầu thất bại')

# In nội dung của yêu cầu
print(response.text)

# Gửi yêu cầu POST đến địa chỉ URL
url_post = 'https://httpbin.org/post'
data = {'key': 'value'}
response_post = requests.post(url_post, data=data)

# Kiểm tra trạng thái của yêu cầu
if response_post.status_code == 200:
    print('Yêu cầu POST thành công')
else:
    print('Yêu cầu POST thất bại')

# In nội dung của yêu cầu
print(response_post.text)

# Gửi yêu cầu GET với tham số URL
url_param = 'https://httpbin.org/get'
params = {'key': 'value'}
response_param = requests.get(url_param, params=params)

# Kiểm tra trạng thái của yêu cầu
if response_param.status_code == 200:
    print('Yêu cầu GET với tham số thành công')
else:
    print('Yêu cầu GET với tham số thất bại')

# In nội dung của yêu cầu
print(response_param.text)

# Gửi yêu cầu HEAD đến địa chỉ URL
url_head = 'https://www.google.com'
response_head = requests.head(url_head)

# Kiểm tra trạng thái của yêu cầu
if response_head.status_code == 200:
    print('Yêu cầu HEAD thành công')
else:
    print('Yêu cầu HEAD thất bại')

# In nội dung của yêu cầu
print(response_head.headers)