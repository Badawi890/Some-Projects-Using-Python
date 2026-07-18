
# kelime tekrar eden bir fonksiyon
# Bu fonksiyon verilen kelimeyi belirtilen sayıda tekrar eder ve ekrana yazdırır.
def yazdir(kelime,adet):
    print(kelime * adet)
yazdir("Merhaba\n", 3)

#bu kod sinirsiz paramater ektarmak.
def listeyi(*params):
    list=[]
    for param in params:
        list.append(param)
    return list
result=listeyi(10,20,"elma", "armut", "muz")
print(result)

# iki sayi asal sayi olduğunğ olmadığını kontrol eden bir fonksiyon
# Bu fonksiyon iki sayı arasındaki asal sayıları bulur ve ekrana yazdırır 
def asalsayi(sayi1,sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2,sayi):
                 if (sayi % i ==0):
                        print("asal sayi degildir:",sayi )
                        break
            else:
                print(sayi)
                print("asal sayidir:",sayi)
sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))
asalsayi(sayi1,sayi2)

#kendisine gönderilen bir sayının tam bölenlerini bir liste olarak döndüren bir fonksiyon
# Bu fonksiyon verilen sayının tam bölenlerini bulur ve bir liste olarak döndür
def tambolum(tam):
    tambolum = []
    for i in range(2, tam ):
        if (tam % i == 0):
            tambolum.append(i)
    return tambolum
print(tambolum(50))
