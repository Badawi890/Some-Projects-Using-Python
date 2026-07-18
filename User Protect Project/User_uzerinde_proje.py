'''
ogrnciler={
    '120':{
         'isim':'Ali',
          'soyisim':'Yılmaz',
           'telefon':'555-1234',
  },
    '121':{
           'isim':'Ayşe',
            'soyisim':'Demir',
            'telefon':'555-5678',
  },
     '122':{
               'isim':'Mehmet',
                  'soyisim':'Kara',
                     'telefon':'555-9012',
   },
}
'''

ogrenciler = {}
# Öğrenci bilgilerini kullanıcıdan al
ID= input("Öğrenci ID:   ")
number = input("Öğrenci NO:    ")
Name= input("Öğrenci Adı:  ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefonu: ")
# Öğrenci bilgilerini sözlüğe ekle
#ogrenciler['ogrenci ID:  '+ID] = {
   # 'ogrenci_no': number,
    #'isim': Name,
    #'soyisim': surname,
    #'telefon': phone
#}
#print(ogrenciler)
# matot.update istediğim kadar öğrenci ekleyebilir 

ogrenciler.update({
    'ogrenci ID:  '+ID: {
        'ogrenci_no': number,
        'isim': Name,
        'soyisim': surname,
        'telefon': phone
    }
})
print("")
ID= input("Öğrenci ID:   ")
number = input("Öğrenci NO:    ")
Name= input("Öğrenci Adı:  ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefonu: ")
ogrenciler.update({
    'ogrenci ID:  '+ID: {
        'ogrenci_no': number,
        'isim': Name,
        'soyisim': surname,
        'telefon': phone
    }
})
print("")
ID= input("Öğrenci ID:   ")
number = input("Öğrenci NO:    ")
Name= input("Öğrenci Adı:  ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefonu: ")
ogrenciler.update({
    'ogrenci ID:  '+ID: {
        'ogrenci_no': number,
        'isim': Name,
        'soyisim': surname,
        'telefon': phone
    }
})
print("*"*50)
print( ogrenciler )
print("*"*50)
ogrno = input("ogrenci ID: ")

ogrenci= ogrenciler["ogrenci ID:  "+ogrno]

print(f"aradğınız öğrenci ID: {ogrno}\n adı: {ogrenci["isim"]}\n soyadı: {ogrenci["soyisim"] } \n  telefon numarası: {ogrenci["telefon"]}")