Agirlik=float(input("Kilogram ağırlığı:"))
Boyu=float(input("Boyu uzunluk:"))

bmi= Agirlik/(Boyu**2)

if bmi<=float(0.00185):
    print(bmi,"\t BMI Sonuçları Göre Zayıf sınız")
elif float(0.00185) <bmi<=float(0.00249):
    print(bmi,"\t BMI Sonuçları Göre Normal sınız")
elif float(0.00249) <bmi<=float(0.00299):
    print(bmi,"\t BMI Sonuçları Göre Kilolu sınız")
elif float(0.00299) <bmi<=float(0.00349):
    print(bmi,"\t BMI Sonuçları Şişman sınız")
elif float(0.00349) <bmi<=float(0.00399):
    print(bmi,"\t BMI Sonuçları Aşırı Şişman sınız")
else:
        print(bmi,"\t BMI Sonuçları Aşırı Aşırı Şişman sınız")