def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
#Sử dụng hàm và in ra kết quả
my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)

# input = input("Nhập phần tử muốn xóa: ")
# result = xoa_phan_tu(my_dict, input)

if result:
    print("Phần tử đã được xóa từ Dictionary: ", my_dict)
else:
    print("Phần tử không tồn tại trong Dictionary.")