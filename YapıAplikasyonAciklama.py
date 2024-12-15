# Kullanıcıdan bilgileri al
yapi_tipi = input("Yapı Tipi: ")
bagimsiz_bolum = input("Bağımsız Bölüm Sayısı: ")
zeminalti_kat = input("Zemin Kat Altı Kat Sayısı: ")
zeminustu_kat = input("Zemin Kat Üstü Kat Sayısı: ")
imardurum_tarih = input("İmar Durumu Tarihi: ")
imardurum_no = input("İmar Durumu No: ")
imarplan_durum = input("İmar Planındaki Durumu: ")
taban_alan = input("Yapı Taban Alanı (m2): ")
gun = input("Gün: ")
ay = input("Ay: ")
yil = input("Yıl: ")
sayili = input("Sayılı: ")

# Metni formatla ve ekrana yazdır
formatted_text = f"""
Yapı Tipi: {yapi_tipi}
Bağımsız Bölüm Sayısı: {bagimsiz_bolum}
Zemin Kat Altı Kat Sayısı: {zeminalti_kat}
Zemin Kat Üstü Kat Sayısı: {zeminustu_kat}
İmar Durumu Tarihi: {imardurum_tarih}
İmar Durumu No: {imardurum_no}
İmar Planındaki Durumu: {imarplan_durum}
Yapı Taban Alanı : {taban_alan} m2
Yapı aplikasyon projesi; mimari proje
ve LİHKAB tarafından verilen
{gun}/{ay}/{yil} tarih, {sayili} sayılı arsa
aplikasyonuna göre düzenlenmiştir.
"""

print(formatted_text)

with open("yapi_bilgileri.cks", "w") as file:
    file.write(formatted_text)

print("Bilgiler 'yapi_bilgileri.txt' adlı dosyaya kaydedildi.")
