import os

def alt_dizinleri_bul(dizin):
    alt_dizinler = [d for d in os.listdir(dizin) if os.path.isdir(os.path.join(dizin, d))]
    return alt_dizinler

def alt_dizinleri_txt_ile_kaydet(dizin, txt_dosya):
    alt_dizinler = alt_dizinleri_bul(dizin)

    with open(txt_dosya, 'w') as dosya:
        for alt_dizin in alt_dizinler:
            dosya.write(alt_dizin + '\n')

if __name__ == "__main__":
    dizin = os.getcwd()  # İlgili dizini kendi dizininizle değiştirin
    txt_dosya = 'alt_dizinler.txt'     # Alt dizinleri kaydetmek için kullanılacak txt dosyasının adını belirtin
    alt_dizinleri_txt_ile_kaydet(dizin, txt_dosya)
