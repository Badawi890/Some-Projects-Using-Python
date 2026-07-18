Hak=3
scelet= int(input("İf you have an acount click (1) or you don't have an acount click (2): "))
first= 1
second=2


if  first== scelet :

 Name_Surname= str(input("login your name and surname: "))
 Birthdate= str(input("login your birthdate: "))
 Phone_Number= str(input("login your phone number: "))
 Email= str(input("login your E-mail: "))
 make_new_password = str(input("Make New Password:"))
 while Hak > 0:
     Hak -= 1
     password = str(input("login your password:"))
     if make_new_password == password:
         print("Wellcome in your bank System:)")
         break
     else:
         print("Try again:(", f"{Hak}  you have the right! ")
     if Hak == 0:
         print(" You use final right your system close it:(")
elif second == scelet:
    print("You don't have an account. Please create one to continue!")
    Name_Surname= str(input("login your name and surname: "))
    Birthdate= str(input("login your birthdate: "))
    Phone_Number= str(input("login your phone number: "))
    Email= str(input("login your E-mail: "))
    make_new_password = str(input("Make New Password:"))
else:
    print("You don't have an account!")



HesapA = {
  "ad": "laith",
  "Hesap No": "12345",
  "Bakıya": 4000,
  "Ek Hesap": 3000

}

HesapB = {
  "ad": "rana",
  "Hesap No": "12344",
  "Bakıya": 6000,
  "Ek Hesap": 2000

}

def para_cek(hesap, miktar):
    print(f"{hesap['ad']} hesabından {miktar} TL çekmek istiyor.")
    if hesap["Bakıya"] >= miktar:
        print("paranız çekebilirsiniz.")
        hesap["Bakıya"] -= miktar
        print(f"{hesap['ad']} hesabından {miktar} TL çekildi. Yeni bakiye: {hesap['Bakıya']} TL")
    else:
        toplam = hesap["Bakıya"] + hesap["Ek Hesap"]
        if toplam >= miktar:
            ekhesap = input("Ek hesap kullanmak ister misiniz? (E/H): ")
            if ekhesap == "E":
                print("Ek hesap kullanabilirsiniz.")
                hesap["Ek Hesap"] -= (miktar - hesap["Bakıya"])
                hesap["Bakıya"] = 0
                print(f"{hesap['ad']} hesabından {miktar} TL çekildi. Yeni bakiye: {hesap['Bakıya']} TL, Ek Hesap: {hesap['Ek Hesap']} TL")
            else:
                print(f"{hesap}Hesap No nolu hesabınız {hesap}Bakıya bulunmaktadtır.")
        else:
            print("Yetersiz bakiye ve ek hesap. İşlem yapılamıyor.")
para_cek(HesapA, 6000)
para_cek(HesapB, 3000)