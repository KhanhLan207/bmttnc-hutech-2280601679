def chia_het_cho_5(sonhiphan):
    # Chuyển đổi số nhị phân sang số thập phân
    sothapphan = int(sonhiphan, 2)
    
    if sothapphan % 5 == 0:
        return True
    else:
        return False
    
chuoi_so_nhiphan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

so_nhiphan_list = chuoi_so_nhiphan.split(',')
so_chia_het_5 = [so for so in so_nhiphan_list if chia_het_cho_5(so)]

if len(so_chia_het_5 ) >0:
    ketqua = ','.join(so_chia_het_5)
    print("Các số nhị phân chia hết cho 5:", ketqua)
else:
    print("Không tìm thấy số nhị phân nào chia hết cho 5.")