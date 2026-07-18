sayi= int(input("Bir sayı giriniz: "))
asal = True



if sayi== 1:
    asal = False
for i in range(2, sayi):
    if sayi % i == 0:
        asal = False
        break
if asal :
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")
