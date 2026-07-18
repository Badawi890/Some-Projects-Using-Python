# bu kod, kullanıcıdan kişisel bilgileri alır ve belirtilen sayıda tekrarlayarak ekrana yazdırır.
# Kullanıcıdan alınan bilgiler: isim, yaş, iş, numara ve e-posta.
# Kullanıcıdan alınan sayı kadar kişisel bilgileri ekrana yazdırır.

Z = 0
Q = float(input("Lütfen bir sayı giriniz: "))
Name= str(input("login your Name and Surname, please!: ")),"\n",
Old= str(input("login your Old, please!: ")), "\n", 
Job= str(input("login your Job, please!: ")), "\n", 
Numberes= str(input("login your Numbere, please!: ")),"\n", 
e_mail= str(input("login your E-mail, please!: "))
while Z < Q:
    Z = Z + 1
     
    print( Z,".","\t","Name:" ,Name,"\n",
                 "\t","Old:" ,Old, "\n", 
                 "\t","Job:" , Job, "\n", 
                 "\t","Numbere:" , Numberes,"\n", 
                 "\t","E-mail:" , e_mail)
    


# İsimler ve telefon numaralarını birleştiren zip() fonksiyonu örneği
Names = ["Laith" , "Badawi", "Python", "Developer", "Engineer"]
Numbers = ["05357316675", "0531547335" , "0543756422077" , "05396445272"  , "0585937357554"]
Email = ["lays2017lays@gmail.com","electrical_engineer_2025 laith_badawi@gmail.com","eng.laith2025master@gmail.com","eng.laith2024badawi@gmail.com","laith2001badawi@gmail.com",]
for  name ,number, email  in zip(Names, Numbers,Email ):
    print(f"Name: {name}, Phone Number: {number}, Email: {email}")
# Bu kod, telefon numaraları ve isimleri ve E-mailler birleştirerek her bir numaranın ismini yazdırır.