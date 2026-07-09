cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)


talabalar = ['jonibek', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho

print(baholangan_talabalar)
print(talabalar)