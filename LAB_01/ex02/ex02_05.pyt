sogiolam = float(input("Nhập số giờ làm mỗi tuần: "))
luonggio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam, giotieuchuan)
thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio

print("Số tiền thực lĩnh của nhân viên là:", thuclinh)
