def ktra_snto(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num = int(input("Nhập vào số cần kiểm tra: "))
if ktra_snto(num):
    print(num, "là số nguyên tố.")
else:
    print(num, "không phải là số nguyên tố.")
    