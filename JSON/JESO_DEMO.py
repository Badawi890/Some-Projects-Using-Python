import json
import os
class User:
    def __init__(self,user_name,password,email,phone_No):
        self.user_name= user_name
        self.password=password
        self.email=email
        self.phone_No= phone_No
       

class User_maneger:
    def __init__(self):
        self.users=[]
        self.isLoggedIn= False
        self.currentUser= {}

        #load users from .json file
        self.loadusers()
    def loadusers(self):
        if os.path.exists("USERS.json"):
            with open("USERS.json","r",encoding="utf-8") as f:
               users= json.load(f)
               for user in users:
                    print(user)

    
    def register(self, user:User):
        self.users.append(user)
        self.save_to_file()
        print("Kullanıcı oluşturdu :)")
        print(maneger.users)

        
    def login(self,user_name,password):
        for user in self.users:
            if user.user_name == user_name and user.password == password:
                self.isLoggedIn= True
                self.currentUser=user
                print("login yapıldı.")
                break
    def logout(self):
        self.isLoggedIn=False
        self.currentUser= {}
        print("Çıkış yapıldı.")

    def identity(self):
        if self.isLoggedIn:
            print("user_name:",user_name)
        else:
            print("giriş yapılmadı. ")
        
    def save_to_file(self):
        list= []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("kullancilar.json","w",encoding="utf-8") as f:
            json.dump(list,f)
            

maneger=User_maneger()

while True:
    print(" Menu ".center(50,"*"))
    secim= input("1.Register\n 2.Login\n 3.Logout\n 4.identity\n 5.Exit\n Seçeceğiniz Sayı giriniz: ")
    if secim == "5":
        break
    else:
        if secim =="1":
            user_name=input("user name:")
            password=input("password :")
            email=input("email :")
            phone_No=input("phone No:")

            user= User(user_name=user_name,password=password,email=email,phone_No=phone_No)
            maneger.register(user)

        elif secim == "2":
            if maneger.isLoggedIn:
              print("zaten login oldunuz")
            else:
                user_name = input("Login User Name:")
                password = input("Login User password:")
                maneger.login(user_name,password)
        elif secim == "3":
            maneger.logout()
        elif secim =="4":
            maneger.identity()
        else:
            print("Yanlış Seçim Girdiniz :(")
