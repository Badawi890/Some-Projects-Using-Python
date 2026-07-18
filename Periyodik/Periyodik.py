# ==========================================================
# Ödev: Periyodik Cetvel Kullanarak İsim Yazdırma Programı
# Ad Soyad   : LAITH BADAWİ
# Öğrenci No: 258051043
# ==========================================================

"""
Bu program, girilen element Sayı(ları) ya da Sembol(ları) ya da Ad(ları)
periyodik cetvelde bulunan TÜM element sembollerini
kullanarak yazmaya çalışır.

- Birden fazla olası yazımı bulur
- En iyi (en az sembollü) çözümü seçer
- Renkli terminal çıktısı verir
- Kullanıcıdan girdi alır
- Pandas kütüphanesini kullanarak element verilerini okur
- Element verileri CSV dosyasından yüklenir
- Element sayısı, sembolü, adı ve atomik ağırlığı içerir
- Birden fazla girdi için virgülle ayırma desteği vardır
- While döngüsü ile programı tekrar tekrar çalıştırma imkanı sunar ve sonlandırma seçeneği sunar.
Önemli Not: Element sayları ya da sembolleri ya da adları virgülle ayrılmış şekilde girilebilir.
(Örneğin: '1,2,3' veya 'Si,Li,N' veya 'Hydrogen,Helium,Lithium' gibi).
"""

# ----------------------------------------------------------
# TÜM PERİYODİK CETVEL VERİLERİNİ OKUMA
# ----------------------------------------------------------
import pandas as pd


ELEMENTS= pd.read_csv("C:/CSV/Periyodik_Cetvel.csv")
ELEMENTS_No = ELEMENTS['ELEMENTS No'].tolist()
ELEMENTS_Sembols = ELEMENTS['SYMBOL'].tolist()
ELEMENTS_Name = ELEMENTS['NAME'].tolist()
ELEMENTS_Atomic_Weight = ELEMENTS['ATOMIC WEIGHT'].tolist()
# ----------------------------------------------------------
# RENKLER
# ----------------------------------------------------------
GREEN="\033[92m"; RED="\033[91m"; BLUE="\033[96m"; YELLOW="\033[93m"; RESET="\033[0m"

# ----------------------------------------------------------
# Element Sembollerini Bul - Giriş Türüne Göre (Çoklu Girdi Destekler)
# ----------------------------------------------------------
def find_elements(user_input):
    """
    Kullanıcı girişine göre elementleri bul (çoklu girdileri destekler)
    Sembol, element adı, sayı veya atomik ağırlık olabilir
    Virgülle ayrılmış girdileri işler: '1,2,3' veya 'Si,Li,N'
    """
    results = []
    
    # Virgülle ayrılmış girdileri işle
    inputs = [x.strip() for x in str(user_input).split(',')]
    
    for single_input in inputs:
        if not single_input:
            continue
            
        # Tüm sütunlarda ara
        found = False
        for idx, row in ELEMENTS.iterrows():
            if (str(row['SYMBOL']).lower() == single_input.lower() or
                str(row['NAME']).lower() == single_input.lower() or
                str(int(row['ELEMENTS No'])) == single_input):
                results.append({
                    'symbol': row['SYMBOL'],
                    'name': row['NAME'],
                    'number': int(row['ELEMENTS No']),
                    'weight': row['ATOMIC WEIGHT']
                })
                found = True
                break
        
        if not found:
            # Element bulunamadı, tüm girdilerin kombinasyonunu dene
            pass
    
    return results

# ----------------------------------------------------------
# İSİM YAZDIRMA FONKSİYONU (DİNAMİK PROGRAMLAMA)
# ----------------------------------------------------------
def write_name_with_elements(name):
    """
    Girilen ismi periyodik cetvel element sembolleri
    kullanarak yazıp, tüm olası çözümleri bulur.
    En az sembol kullananı (en iyi) seçer.
    """
    name = name[0].upper() + name[1:].lower()  # İlk harf büyük, diğerleri küçük
    name = name.lower()  # Karşılaştırma için küçük harf
    n = len(name)
    
    # dp[i] = i. karaktere kadar yazabildiği en iyi çözüm
    dp = [None] * (n + 1)
    dp[0] = []  # Boş string için boş çözüm
    
    for i in range(1, n + 1):
        # Maksimum 3 karakterli sembol için kontrol et (en uzun: Uuo, Uus, Uup vb)
        for j in range(max(0, i - 3), i):
            segment = name[j:i]
            # Segment'i büyük harfle (1. harf büyük, diğerleri küçük)
            segment_formatted = segment[0].upper() + segment[1:].lower()
            
            # Segment elementi listede ve önceki pozisyon çözülebilir ise
            if segment_formatted in ELEMENTS_Sembols and dp[j] is not None:
                candidate = dp[j] + [segment_formatted]
                # Daha iyi çözüm varsa güncelle
                if dp[i] is None or len(candidate) < len(dp[i]):
                    dp[i] = candidate
    
    return dp[n]

# ----------------------------------------------------------
# ANA PROGRAM
# ----------------------------------------------------------
while True:

    print(GREEN + "="*60 + RESET)
    print(GREEN + "Program Başladı..." + RESET)
    print(GREEN +"Öğrenci Adı ve Soyadı: LAITH BADAWİ" + RESET)
    print(GREEN + "Öğrenci Numarası: 258051043" + RESET)
    print(GREEN + "="*60 + RESET)
    print(BLUE + "Önemli Notlar:" + RESET)
    print(BLUE + "Çoklu girdiler için virgülle ayırın(Örneğin: '1,2,3' veya 'Si,Li,N' veya 'Hydrogen,Helium,Lithium' gibi)." + RESET)
    print(BLUE  + "="*60 + RESET)

    if __name__ == "__main__":

        user_input = input(YELLOW +"İstediğiniz Element Sayı(ları) ya da Sembol(ları) ya da Ad(ları) Giriş yapın: ").strip()

        if not user_input:
            print(RED + "Hata: Lütfen bir giriş yapın!" + RESET)
        else:
            # Önce element veritabanında ara
            found_elements = find_elements(user_input)

            if found_elements:
                print(f"\n{GREEN}Bulunan Elementler:{RESET}")
                print(f"{GREEN}{'-'*60}{RESET}")

                combined_symbols = []
                for elem in found_elements:
                    print(f"  Sembol: {BLUE}{elem['symbol']:>2}{RESET}  | "
                          f"Ad: {BLUE}{elem['name']:<20}{RESET}  | "
                          f"Sayı: {BLUE}{elem['number']:<3}{RESET}  | "
                          f"Ağ.: {BLUE}{elem['weight']:<8}{RESET}")
                    combined_symbols.append(elem['symbol'])

                print(f"{GREEN}{'-'*60}{RESET}")

                # Tüm sembolleri isim yazı dönüştürmesi için kullan
                combined_name = ''.join(combined_symbols)
                result = write_name_with_elements(combined_name)

                if result:
                    output = ' - '.join(result)
                    print(f"\n{GREEN}İsim Yazı Dönüştürmesi:{RESET}")
                    print(f"{BLUE}{output}{RESET}")
                    print(f"{GREEN}Toplam Sembol Sayısı: {len(result)}{RESET}")
                else:
                    print(RED + f"'{combined_name}'Bu isim periyodik cetveldeki element sembolleriyle oluşturulamıyor." + RESET)
            else:
                # Eğer element bulunamadıysa, tüm girdileri isim yazı dönüştürmesi yap
                result = write_name_with_elements(user_input)

                if result:
                    output = ' - '.join(result)
                    print(f"\n{GREEN}İsim '{user_input}' periyodik cetvel elemanları ile yazıldı:{RESET}")
                    print(f"{BLUE}{output}{RESET}")
                    print(f"{GREEN}Toplam Sembol Sayısı: {len(result)}{RESET}")
                else:
                    print(RED + f"\n'{user_input}' Bu isim periyodik cetveldeki element sembolleriyle oluşturulamıyor." + RESET)
        # Kullanıcıya programı devam ettirmek isteyip istemediğini sor
        choice = input(YELLOW + "\nProgramı devam ettirmek istiyorsanız Evet => 'E' yazın, sonlandırmak istiyorsanız Hayır => 'H' yazın: ").strip()
        if choice == 'H':
            print(RED + "Program sonlandırdı." + RESET)
            break
        elif choice == 'E':
            # Döngü başa döner ve program devam eder
            continue
        else:
            print(RED + "Geçersiz seçim!!!\n Program sonlandırılıyor." + RESET)
            break
# ----------------------------------------------------------

