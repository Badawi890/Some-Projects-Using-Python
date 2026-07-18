import requests
import json
# import tkinter as tk
# from tkinter import ttk, messagebox

# class DovizCevirici:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Döviz Çevirici")
#         self.root.geometry("1200x900")
#         self.root.configure(padx=20, pady=20)

#         self.api_key = "2fefbd7dc14a6f8fc162d65c"
#         self.api_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/"

#         # Döviz türleri (örnek olarak en yaygın olanlar)
#         self.doviz_turleri = ["USD", "EUR", "TRY", "GBP", "JPY", "CHF", "CAD", "AUD"]

#         # Arayüz elemanları
#         self.create_widgets()

#     def create_widgets(self):
#         # Bozulan Döviz
#         tk.Label(self.root, text="Bozulan Döviz Türü:").pack(anchor="w")
#         self.bozulan_doviz = ttk.Combobox(self.root, values=self.doviz_turleri)
#         self.bozulan_doviz.pack(fill="x", pady=(0, 10))
#         self.bozulan_doviz.set("USD")

#         # Alınan Döviz
#         tk.Label(self.root, text="Alınan Döviz Türü:").pack(anchor="w")
#         self.alinan_doviz = ttk.Combobox(self.root, values=self.doviz_turleri)
#         self.alinan_doviz.pack(fill="x", pady=(0, 10))
#         self.alinan_doviz.set("TRY")

#         # Miktar
#         tk.Label(self.root, text="Miktar:").pack(anchor="w")
#         self.miktar = tk.Entry(self.root)
#         self.miktar.pack(fill="x", pady=(0, 10))

#         # Hesapla butonu
#         self.hesapla_btn = tk.Button(self.root, text="Hesapla", command=self.hesapla)
#         self.hesapla_btn.pack(fill="x", pady=(0, 10))

#         # Sonuç
#         self.sonuc_frame = tk.LabelFrame(self.root, text="Sonuç", padx=10, pady=10)
#         self.sonuc_frame.pack(fill="x")

#         self.kur_label = tk.Label(self.sonuc_frame, text="")
#         self.kur_label.pack()

#         self.sonuc_label = tk.Label(self.sonuc_frame, text="")
#         self.sonuc_label.pack()

#     def hesapla(self):
#         try:
#             bozulan = self.bozulan_doviz.get()
#             alinan = self.alinan_doviz.get()
#             miktar = float(self.miktar.get())

#             # API'den veri çekme
#             sonuc = requests.get(self.api_url + bozulan)
#             sonuc_json = json.loads(sonuc.text)

#             # Dönüşüm oranı
#             oran = sonuc_json["conversion_rates"][alinan]
#             toplam = miktar * oran

#             # Sonuçları gösterme
#             self.kur_label.config(text=f"1 {bozulan} = {oran:.4f} {alinan}")
#             self.sonuc_label.config(text=f"{miktar:.2f} {bozulan} = {toplam:.2f} {alinan}")

#         except ValueError:
#             messagebox.showerror("Hata", "Lütfen geçerli bir miktar giriniz!")
#         except Exception as e:
#             messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DovizCevirici(root)
#     root.mainloop()

api_key="2fefbd7dc14a6f8fc162d65c"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz= input(" Bozulan Döviz Türü: ") #USD
alinan_doviz= input(" Alınan Döviz Türü: ") #TRY
miktar= float(input(f"Ne Kadar {bozulan_doviz} Buzdurmak İstiyorsunuz! : ")) #Ne kadar USD

sonuc= requests.get(api_url+bozulan_doviz)
sonuc_json= json.loads(sonuc.text)

print("{1} {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))



