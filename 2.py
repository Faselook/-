class City():

    def __init__(self, nameCity, nameRegion, nameCountry, numberOfInhabitants, postcode, phoneNumber):
        self.nameCity = nameCity
        self.nameRegion = nameRegion
        self.nameCountry = nameCountry
        self.numberOfInhabitants = numberOfInhabitants
        self.postcode = postcode
        self.phoneNumber = phoneNumber

    def setNameCity(self):
        self.nameCity = input("enter nameCity - ")

    def setNameRegion(self):
        self.nameRegion = input("enter nameRegion - ")

    def setNameCountry(self):
        self.nameCountry = input("enter nameCountry - ")

    def setNumberOfInhabitants(self):
        self.numberOfInhabitants = input("enter numberOfInhabitants - ")

    def setPostcodey(self):
        self.postcode = input("enter postcode - ")

    def setPhoneNumber(self):
        self.phoneNumber = input("enter phoneNumber - ")

    def setAll(self):
        self.nameCity = input("enter nameCity - ")
        self.nameRegion = input("enter nameRegion - ")
        self.nameCountry = input("enter nameCountry - ")
        self.numberOfInhabitants = input("enter numberOfInhabitants - ")
        self.postcode = input("enter postcode - ")
        self.phoneNumber = input("enter phoneNumber - ")

    def getNameCity(self):
        print(self.nameCity)

    def getNameRegion(self):
        print(self.nameRegion)

    def getNameCountry(self):
        print(self.nameCountry)

    def getNumberOfInhabitants(self):
        print(self.numberOfInhabitants)

    def getPostcode(self):
        print(self.postcode)

    def getPhoneNumber(self):
        print(self.phoneNumber)

    def out(self):
        print("nameCity = ", self.nameCity)
        print("nameRegion = ", self.nameRegion)
        print("nameCountry = ", self.nameCountry)
        print("numberOfInhabitants = ", self.numberOfInhabitants)
        print("postcode = ", self.postcode)
        print("phoneNumber = ", self.phoneNumber)

DAN = City("NewYork","POI","USA","2151515","67584","41234569234")
DAN.out()