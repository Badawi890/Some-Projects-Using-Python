

import numpy as np

#1.(10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result1 = np.array([(10,15,30,45,60)])
print("1.Soru:(10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.")
print("Çözüm:")
print(result1)
print("*"*35)

#2.(5,15) arasındaki sayılarla numpy dizisi oluşturunuz.
result2= np.arange(5,15)
print("2.Soru:(5,15) arasındaki sayılarla numpy dizisi oluşturunuz.")
print("Çözüm:")
print(result2)
print("*"*35)

#3.(50-100) arasında 5'er 5'er  artarak numpy dizisi oluşturunuz.
result3= np.arange(50,100,5)
print("3.Soru: (50-100) arasında 5'er 5'er  artarak numpy dizisi oluşturunuz.")
print("Çözüm:")
print(result3)
print("*"*35)

#4. (10) elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
 
result4= np.zeros(10)
print("4.Soru: (10) elemanlı sıfırlardan oluşan bir dizi oluşturunuz.")
print("Çözüm:")
print(result4)
print("*"*35)

#5. (10) elemanlı birlerden oluşan bir dizi oluşturunuz.
 
result5= np.ones(10)
print("5.Soru: (10) elemanlı birlerden oluşan bir dizi oluşturunuz.")
print("Çözüm:")
print(result5)
print("*"*35)

#6.(0-100) arasında eşit aralıkı 5 sayı üretin.

result6= np.linspace(0,100,5)
print("6.Soru: (0-100) arasında eşit aralıkı 5 sayı üretin.")
print("Çözüm:")
print(result6)
print("*"*35)

#7.(10-30) arasında rastgele 5 tane tam sayı üretin.

result7= np.random.randint(10,30,5)
print("7.Soru: (10-30) arasında rastgele 5 tane tam sayı üretin.")
print("Çözüm:")
print(result7)
print("*"*35)

#8.[-1 ile 1] arasında 10 adet sayı üretin.

result8= np.random.randn(10)
print("8.Soru: [-1 ile 1] arasında 10 adet sayı üretin.")
print("Çözüm:")
print(result8)
print("*"*35)

#9.(3x5) boyutlarında (10-50) arasında rastgele bir matrix oluşturunuz.

result9 = np.random.randint(10,50,15).reshape(3,5)
print("9.Soru: (3x5) boyutlarında (10-50) arasında rastgele bir matrix oluşturunuz.")
print("Çözüm:")
print(result9)
print("*"*35)

#10. Üretilen matrix satır ve sütun sayıları toplamlarını hesaplayınız?

matrix=np.random.randint(-50,50,15).reshape(3,5)

rewTotal= matrix.sum(axis=1) 
result10= matrix.sum(axis=0) 
print("10.Soru: Üretilen matrix satır ve sütun sayıları toplamlarını hesaplayınız?")
print("Çözüm:")
print("Matrix değerleri: =>",matrix)
print("-"*10)
print("Satır toplama değeri: =>",rewTotal)
print("-"*10)
print("Sütun toplama değeri: =>",result10)
print("*"*35)

#11. Üretilen matrix en büyük, en küçük ve ortalaması bulunuz.
number3= np.random.randint(0,30,6)

result11= np.max(number3)
result11_1= np.min(number3)
result11_2= np.mean(number3)
print("11.Soru: Üretilen matrix en büyük, en küçük ve ortalaması bulunuz.")
print("Çözüm:")
print(number3,"Max değeri: =>",result11)
print("-"*10)
print(number3,"Min değeri:=>",result11_1)
print("-"*10)
print(number3,"Ortalama değeri:=>",result11_2)
print("*"*35)

#12. Üretilen matrix en büyük degerinin index kaçtır?

result12= matrix.argmax()
result12_1= matrix.argmin()
print("12.Soru: Üretilen matrix en büyük degerinin index kaçtır?")
print("Çözümü:")
print(matrix,"=> Max index:",result12)
print("-"*10)
print(matrix,"=> Min index:",result12_1)
print("*"*35)

#13.(10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

arr= np.arange(10,20)
result13= arr[:3]
print("13.Soru: (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.")
print("Çözüm:")
print("Matrix: =>",arr)
print("-"*10)
print("Matrix ilk 3 eleman: =>",result13)
print("*"*35)

#14.Üretilen dizinin elemanlarını tersten yazdırın.

result14= arr[::-1]

print("14.Soru: Üretilen dizinin elemanlarını tersten yazdırın.")
print("Çözüm:")
print("Matrix: =>",arr)
print("-"*10)
print("Matrix tersi: =>",result14)
print("*"*35)

#15.Üretilen matrix ilk satırını seçiniz.

result15= matrix[0]

print("15.Soru: Üretilen matrix ilk satırını seçiniz.")
print("Çözüm:")
print("Matrix: =>",matrix)
print("Matrix ilk satırını: =>",result15)
print("*"*35)

#16. Üretilen matrix 2.satır ve 3. sütundeki elemanı hangisidir?

result16= matrix[1,2]

print("16.Soru: Üretilen matrix 2.satır ve 3. sütundeki elemanı hangisidir?")
print("Çözüm:")
print("Matrix: =>",matrix)
print("Matrix 2.satır ve 3.sütundeki elemanı: => ",result16)
print("*"*35)

#17. Üretilen matrix tüm satırlardaki ilk elemanı hangisidir?
result17= matrix[::,0]

print("17.Soru: Üretilen matrix tüm satırlardaki ilk elemanı hangisidir?")
print("Çözüm:")
print("Matrix: =>",matrix)
print("matrix tüm satırlardaki ilk elemanı: =>",result17)
print("*"*35)

#18. Üretilen matrix her bir elemanının karesini alınız.
result18= matrix[::]**2

print("18.Soru: Üretilen matrix her bir elemanının karesini alınız")
print("Çözüm:")
print("Matrix: =>",matrix)
print("Matrix tüm sayılar karesi: =>",result18)
print("*"*35)

#19. Üretilen matrix elemanlarının hangisi pozitif çiftsayıdı??
# Aralığı (-50,+50) arasında yapınız.

result19= matrix %2 == 0
result19_1= matrix[matrix %2 == 0]
result19_1= result19_1[result19_1>0]


print("19.Soru: Üretilen matrix elemanlarının hangisi pozitif çiftsayıdı??")
print(" Aralığı (-50,+50) arasında yapınız.")
print("Çözüm:")
# print("Matrix Çift sayılar(True),\nTek sayılar(False): =>",result19)
print("Matrix sadece Çift sayılar: =>",result19_1)
# print("Matrix sadece Çift pozitif sayılar: =>",result19_2)
print("*"*35)