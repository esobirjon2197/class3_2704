
# 5-m
class Ishchi:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def ishla(self):
        print("Ishlamoqda")

class Dasturchi(Ishchi):
    def ishla(self):
        super().ishla()
        print("Koq yozmoqda")

d1 = Dasturchi("Sobirjon", 0)
d1.ishla()


# 6-m
class Telefon:
    def __init__(self, madel):
        self.madel = madel

    def qongiroq(self):
        print("Qo‘ng‘iroq qilmoqda")

class Samrtfon(Telefon):
    def qongiroq(self):
        super().qongiroq()
        print("Video qo‘ng‘iroq")

s1 = Samrtfon("iPhone")
s1.qongiroq()
