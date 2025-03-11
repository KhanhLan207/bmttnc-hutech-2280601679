def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input = input("Nhập danh sách các số cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input.split(',')))

print("Tổng các số chẵn: ", tinh_tong_so_chan(numbers))