class Human():

    def __init__(self, fio, birsdey, phone, city, country, address):
        self.fio = fio
        self.birsdey = birsdey
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def setFio(self):
        self.fio = input("enter FIO - ")

    def setBirsdey(self):
        self.birsdey = input("enter birsdey - ")

    def setPhone(self):
        self.phone = input("enter phone - ")

    def setCity(self):
        self.city = input("enter city - ")

    def setCountry(self):
        self.country = input("enter country - ")

    def setAddress(self):
        self.address = input("enter address - ")

    def setAll(self):
        self.fio = input("enter FIO - ")
        self.birsdey = input("enter birsdey - ")
        self.phone = input("enter phone - ")
        self.city = input("enter city - ")
        self.country = input("enter country - ")
        self.address = input("enter address - ")

    def getFio(self):
        print(self.fio)

    def getBirsdey(self):
        print(self.birsdey)

    def getPhone(self):
        print(self.phone)

    def getCity(self):
        print(self.city)

    def getCountry(self):
        print(self.country)

    def getAddress(self):
        print(self.address)

    def out(self):
        print("FID = ", self.fio)
        print("Birsdey = ", self.birsdey)
        print("Phone = ", self.phone)
        print("City = ", self.city)
        print("Country = ", self.country)
        print("Address = ", self.address)

DAN = Human("Ivan","13.08.2005","71051057215","Sochi","fd","Areda")
# DAN.out()
# DAN.setCountry()
# DAN.out()

anonimus = Human(" "," "," "," "," "," ")
anonimus.out()
anonimus.setAll()
anonimus.out()