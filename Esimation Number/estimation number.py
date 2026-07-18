import random

sayi = random.randint(1, 10)
can = float(input("istdiğiniz hak giriniz: "))
hak=can
sayac=0

while hak > 0:
    hak -= 1
    tahmin = int(input("Tahmininizi giriniz: "))
    sayac += 1
    
    if tahmin == sayi:
        puan = 100 - (100 / can) * (sayac - 1)
        print(f"Tebrikler, {sayac}. defada tahmin ettiniz! Aldığınız puan: {puan}")
        
        break
       
    elif tahmin < sayi:
        print("Yukarı")
        
    else:
     print("Aşağı")  

if hak == 0:
    print(f"Haklarınız bitti, doğru cevap:{sayi}")
        