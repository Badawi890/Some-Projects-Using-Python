print("Wellcome to system")

def ortalama_oku():
    with open("Exem_not.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(satir)

def Not_gir():
    name = input("Log in Student Name:")
    surname = input("Log in Student Surname:")
    vize_no = int(input("Log in Student Vize Not:"))
    Final_no = int(input("Log in Student Final Not:"))
    vize = float(vize_no * 0.4)
    Final = float(Final_no * 0.6)
    ortalama = float(vize + Final)

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "FD"
    else:
        harf = "FF"

    print(f"Ortalama sonucu: {ortalama}%({harf})")
    kayit_satiri = (
        name + " " + surname + ":" +
        "Vize Not:" + str(vize_no) + "|" +
        "Final Not:" + str(Final_no) + "|" +
        "Ortalama Not:" + str(ortalama) + "%" + "\n"
    )

    # Sadece Exem_not.txt dosyasına kaydet
    # ...existing code...
    with open("Exem_not.txt", "a", encoding="utf-8") as auto_file:
        auto_file.write(kayit_satiri)
# ...existing code...

while True:
    islem = input("1.Notları  Oku:\n 2.Not Gir:\n 3.Çıkış:\n *Scelet a Number please!:")

    if islem == "1":
        ortalama_oku()
    elif islem == "2":
        Not_gir()
    elif islem == "3":
        break
    