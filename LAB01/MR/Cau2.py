import re

def tinh_tong_so_nguyen(chuoi):
    # Tìm tất cả số âm
    so_am = re.findall(r'-\d+', chuoi)
    tong_am = sum(int(so) for so in so_am)

    # Xoá số âm khỏi chuỗi để tách dương chính xác
    chuoi_khong_am = re.sub(r'-\d+', ' ', chuoi)

    # Tìm tất cả số dương còn lại (phải là \d+ chứ không phải \d)
    so_duong = re.findall(r'\d+', chuoi_khong_am)
    tong_duong = sum(int(so) for so in so_duong)

    return tong_duong, tong_am

# Test
chuoi = "-100#^sdfkj8902w3ir021@swf-20"
duong, am = tinh_tong_so_nguyen(chuoi)
print("Giá trị dương:", duong)
print("Giá trị âm:", am)
