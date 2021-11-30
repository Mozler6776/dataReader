import os
import dataReader_functions

print("""
      _       _        _____                _           
     | |     | |      |  __ \              | |          
   __| | __ _| |_ __ _| |__) |___  __ _  __| | ___ _ __ 
  / _` |/ _` | __/ _` |  _  // _ \/ _` |/ _` |/ _ \ '__|
 | (_| | (_| | || (_| | | \ \  __/ (_| | (_| |  __/ |   
  \__,_|\__,_|\__\__,_|_|  \_\___|\__,_|\__,_|\___|_|   
                                                                                                         
+-----------------------------------------------+
| Author: Mehmet Özler ÇELİK                    |
| Twitter: twitter.com/mozler6776               |
| LinkedIn: linkedin.com/in/mehmetozlercelik/   |
| website: mehmetozlercelik.com                 |
| Github: github.com/mozler6776                 |
+-----------------------------------------------+
 
1) TR   -   Türkçe
2) EN   -   English

""")

veri = [""]

while True:
    lang = input("Language / Dil: ")
    if lang == "1":
        
        veri_dosyasi_adi = input("[?] Arama yapacağınız dosyayı girin (Örnek => data_file.txt): ")

        while True:
            anahtar_kelime_sayisi = int(input("[?] Kaç tane anahtar kelime gireceksin? (1-2): "))
            if(not(anahtar_kelime_sayisi == 1 or anahtar_kelime_sayisi == 2)):
                print("\n[-] Geçersiz değer girdiniz. Lütfen 1 veya 2 girin.\n")
                continue
            break

        j = 1
        while( j <= anahtar_kelime_sayisi):
            veri.append(input("[" + str(j) + ".] Anahtar kelime: "))
            j += 1

        veri_dosyasi = open(veri_dosyasi_adi, "r", encoding='utf8')
        cikti_dosyasi = open(veri[1] + "_output.txt", "a", encoding='utf8')


        dataReader_functions.TR(veri_dosyasi, anahtar_kelime_sayisi, cikti_dosyasi, veri)

        break

    elif lang == "2":

        veri_dosyasi_adi = input("[?] Enter the file you are searching for (Example => data_file.txt): ")

        while True:
            anahtar_kelime_sayisi = int(input("[?] How many keywords will you enter? (1-2): "))
            if(not(anahtar_kelime_sayisi == 1 or anahtar_kelime_sayisi == 2)):
                print("\n[-] You entered an invalid value. Please enter 1 or 2.\n")
                continue
            break

        j = 1
        while( j <= anahtar_kelime_sayisi):
            veri.append(input("[" + str(j) + ".] keyword: "))
            j += 1

        veri_dosyasi = open(veri_dosyasi_adi, "r", encoding='utf8')
        cikti_dosyasi = open(veri[1] + "_output.txt", "a", encoding='utf8')

        dataReader_functions.EN(veri_dosyasi, anahtar_kelime_sayisi, cikti_dosyasi, veri)
        break

    else:
        print("Error value: 1 or 2 / Hatalı değer: 1 ya da 2")
        continue
