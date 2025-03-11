from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien =[]
    def generateID(self):
        maxID = 1
        if(self.soluongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxID < sv._id ):
                    maxID = sv._id
            maxID += 1
        return maxID
    
    def soluongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svID = self.generateID()
        
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh cua sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemtb = input("Nhap diem tb cua sinh vien: ")
        
        sv = SinhVien(svID, name, sex, major, diemtb)
        self.xeploaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, id):
        sv:SinhVien = self.findByID(id)
        if(sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh cua sin vien:")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemtb = float(input("Nhap diem trung binh: "))

        
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemtb = diemtb
            
            self.xeploaiHocLuc(sv)
            
        else: 
            print("Sinh vien co ID = {} khong ton tai!" .format(id))
        
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reversed=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reversed=False)
    
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemtb, reversed=False)
    
    def findByID(self, id):
        searchResult = None
        if(self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == id):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, id):
        isDel = False
        sv = self.findByID(id)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDel = True
        return isDel
    
    def xeploaiHocLuc(self, sv:SinhVien):
        if(sv._diemtb >= 8):
            sv._hocluc = "Gioi"
        elif(sv._diemtb >= 6.5):
            sv._hocluc = "Kha"
        elif(sv._diemtb >= 5):
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem tb", "Hoc luc"))
        
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8.2f} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemtb, sv._hocluc))
        print("\n")
        
    def getlistSinhVien(self):
        return self.listSinhVien