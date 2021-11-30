
import os

def TR(veri_dosyasi, anahtar_kelime_sayisi, cikti_dosyasi, veri):

    i = 0
    j = 1
    for satir in veri_dosyasi:
        yardimci = veri[j]
        if(yardimci.lower() in satir.lower()):
            if(anahtar_kelime_sayisi == 2):
                yardimci = veri[j+1]
                if(yardimci.lower() in satir.lower()):
                    cikti_dosyasi.write(satir) 
                    i += 1
            else:
                cikti_dosyasi.write(satir)
                i += 1
                
    if(i == 0):
        print("[-] Aradığınız kriterlerde hiçbir sonuç bulunamadı.")
        cikti_dosyasi.close()
        os.remove(veri[1] + "_output.txt")
    else:
        print("[!] " + str(i) + " adet sonuç bulundu.")
        print("[+] Sonuçlar '" + veri[1] + "_output.txt' dosyasına yazıldı.")

    veri_dosyasi.close()
    cikti_dosyasi.close()

def EN(veri_dosyasi, anahtar_kelime_sayisi, cikti_dosyasi, veri):

    i = 0
    j = 1
    for satir in veri_dosyasi:
        yardimci = veri[j]
        if(yardimci.lower() in satir.lower()):
            if(anahtar_kelime_sayisi == 2):
                yardimci = veri[j+1]
                if(yardimci.lower() in satir.lower()):
                    cikti_dosyasi.write(satir) 
                    i += 1
            else:
                cikti_dosyasi.write(satir)
                i += 1
                
    if(i == 0):
        print("[-] The data you were looking for was not found.")
        cikti_dosyasi.close()
        os.remove(veri[1] + "_output.txt")
    else:
        print("[!] " + str(i) + " number of results found.")
        print("[+] Result written to '" + veri[1] + "_output.txt' file")

    veri_dosyasi.close()
    cikti_dosyasi.close()