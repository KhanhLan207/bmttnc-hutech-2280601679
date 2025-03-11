from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while(1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("================================")
    print("** 1. Them sinh vien")
    print("** 2. Cap nhat thong tinsinh vien boi ID")
    print("** 3. Xoa sinh vien boi ID")
    print("** 4. Tim kiem sinh vien theo ten")
    print("** 5. Sap xep sinh vien theo diem trung binh")
    print("** 6. Sap xep sinh vien theo chuyen nganh")
    print("** 7. Hien thi danh sach sinh vien")
    print("** 0. Thoat")
    print("================================")
    
    
    
    key = int(input("Nhap tuy chon: "))
    if(key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong.")
        
    elif(key == 2):
        if(qlsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien boi ID.")
            print("Nhap ID: ")
            id = int(input())
            qlsv.updateSinhVien(id)
        else:
            print("Danh sach sinh vien rong.")
    
    elif(key == 3):
        if(qlsv.soluongSinhVien() > 0):
            print("\n3. Xoa sinh vien boi ID.")
            print("Nhap ID: ")
            id = int(input())
            if(qlsv.deleteByID(id)):
                print("Sinh vien co ID = ", id, "da bi xoa.")
            else:
                print("Sinh vien co ID = ", id, "khong ton tai.")
        else:
            print("Danh sach sinh vien rong.")
    
    elif(key == 4):
        if(qlsv.soluongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten sinh vien: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
            
        else:
            print("\nDanh sach sinh vien trong")
            
    elif(key == 5):
        if(qlsv.soluongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien)
        else:
            print("\nDanh sach sinh vien trong")
            
    elif(key == 6):
        if(qlsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
            
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 7):
        if(qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
            
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 0):
        print("\nBye!")
        break