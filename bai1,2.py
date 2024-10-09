### Bài 1:
class HCN:
    def __init__(self):
        self.dai = 0
        self.rong = 0

    def nhap_du_lieu(self):
        self.dai = float(input("Nhập chiều dài: "))
        self.rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        print(f"Chiều dài: {self.dai}")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

hinh_chu_nhat = HCN()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.in_thong_tin()


