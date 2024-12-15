#import request
import webbrowser
import os
import time

os.system("title " + "Parsel Sorgu byTanerSB")
resize_command = "mode con: cols=50 lines=35"
os.system(resize_command)

mahalleler = {
    "aksığın": 169261,
    "altınkent": 206475,
    "atakent": 206485,
    "aydınkent": 206489,
    "bahçecik": 148272,
    "barbaros": 206476,
    "camidüzü": 169259,
    "damlar": 206469,
    "doğantepe": 169254,
    "döngel": 146443,
    "fatih": 206490,
    "havuzlubahçe": 206470,
    "karadenizliler": 206477,
    "karşiyaka": 206486,
    "kazandere": 169268,
    "kiliçarslan": 206471,
    "kullar": 202585,
    "kullar_tepecik": 206481,
    "kullar_yakacik": 206483,
    "mahmutpaşa": 206478,
    "mehmetağa": 206479,
    "ovacik": 206480,
    "paşadağ": 206494,
    "rahmiye": 204393,
    "ş.yuvacık": 169264,
    "ş.bahçecik": 181645,
    "ş.döngel": 181643,
    "ş.kullar": 181642,
    "ş.yeniköy": 181644,
    "şehitekrem": 206473,
    "sepetlipinar": 206487,
    "serdar": 206493,
    "serindere": 169271,
    "servetiye_cami": 169260,
    "servetiye_karşi": 169257,
    "seymen": 206472,
    "tepecik": 169262,
    "vezirçiftliği": 206482,
    "yaylacik": 206484,
    "yeniköy": 145312,
    "yeniköy_merkez": 206488,
    "yeşilkent": 206474,
    "yeşilyurt": 206492,
    "yuvacık": 169258,
    "yuvacik_yakacik": 206491,
    



    "akçakoca": 148263,
    "akmeşe": 146440,
    "akmeşe_atatürk": 207013,
    "akmeşe_cumhuriyet": 207014,
    "akpinar": 206495,
    "alikahya_atatürk": 206502,
    "alikahya_cumhuriyet": 206503,
    "alikahya_fatih": 206504,
    "alikahya_merkez": 206505,
    "ambarci": 144484,
    "arizli": 147789,
    "arpalikihsaniye": 149467,
    "bağlica": 145896,
    "balören": 149826,
    "bayraktar": 169252,
    "biberoğlu": 181336,
    "böğürgen": 146727,
    "bulduk": 148373,
    "çağirgan": 181211,
    "çavuşoğlu": 204934,
    "çayirköy": 148439,
    "cedit": 147839,
    "çubuklu_bala": 146569,
    "çubuklu_osmaniye": 149672,
    "çukurbağ": 146421,
    "cumhuriyet": 207604,
    "dağköy": 169247,
    "deretepe": 144656,
    "düğmeciler": 207015,
    "durhasan": 169263,
    "emirhan": 146731,
    "eseler": 122338,
    "fethiye": 146730,
    "fevziçakmak": 206506,
    "gedikli": 146583,
    "gökçeviran": 146076,
    "gülbahçe_kadriye": 146444,
    "gündoğdu": 148035,
    "güvercinlik": 207022,
    "haci_hizir": 148376,
    "hacihasan": 147659,
    "hakaniye": 148149,
    "hasanciklar": 207017,
    "hatipköy": 169248,
    "kabaoğlu": 148386,
    "kadiköy": 148425,
    "karaabdulbaki": 147353,
    "karabaş": 146589,
    "karadenizliler": 206507,
    "kaynarca": 146566,
    "kemalpaşa": 144444,
    "kisalar": 144828,
    "körfez": 148833,
    "kozluca": 201506,
    "kozluk": 149510,
    "kulfalli": 206496,
    "izmitkullar": 147677,
    "kulmahmut": 146239,
    "kurtdere": 147678,
    "kuruçeşme_fatih": 207603,
    "malta": 207020,
    "mecidiye": 148190,
    "mehmetalipaşa": 146582,
    "nebihoca": 146901,
    "ömerağa": 147086,
    "orhan": 148228,
    "orhaniye": 147919,
    "ortaburun": 144614,
    "ş.durhasan": 169266,
    "ş.arizli": 181201,
    "ş.çayirköy": 181202,
    "ş.deretepe": 181212,
    "ş.gündoğdu": 181204,
    "ş.hatip": 181205,
    "ş.kadiköy": 181214,
    "ş.karabaş": 181215,
    "ş.körfez": 181213,
    "şahinler": 146711,
    "sanayi": 207606,
    "sapakpinar": 145864,
    "sarişeyh": 144466,
    "sekbanli": 206500,
    "sepetçi": 206498,
    "serdar": 206497,
    "şirintepe": 204823,
    "süleymaniye": 146035,
    "sultaniye": 149671,
    "süverler": 207016,
    "tepecik": 147798,
    "tepeköy": 206501,
    "terzi bayiri": 207605,
    "turgut": 148221,
    "tüysüzler": 206510,
    "uzunbeykumla": 204932,
    "veliahmet": 146228,
    "yahyakaptan": 206508,
    "yassibağ": 147928,
    "yenice": 146774,
    "yenidoğan": 146565,
    "yenimahalle": 149778,
    "yenişehir": 206509,
    "yeşilova": 206499,
    "zabitan": 207602,
    "zeytinburnu": 146595,


    "acisu": 202715,
    "arslanbey": 202710,
    "ataevler": 204318,
    "ataşehir": 204316,
    "avluburun_köyü": 202720,
    "balaban_köyü": 202703,
    "çepni": 206511,
    "çiftlik": 202719,
    "derbent": 202714,
    "dumlupinar": 204317,
    "emekevler": 204321,
    "ertuğrulgazi": 204319,
    "eskieşme": 145315,
    "eşme_ahmediye_köyü": 146409,
    "fatih_sultan_mehmet": 204326,
    "ibrikdere": 201287,
    "ifraziye": 202722,
    "istasyon": 204325,
    "karatepe_köyü": 202706,
    "ketenciler_köyü": 201288,
    "köseköy": 202721,
    "kartepekullar": 202725,
    "maşukiye": 202717,
    "nusretiye_köyü": 202705,
    "pazarçayiri_köyü": 202708,
    "rahmiye": 202724,
    "ş.acisu": 202726,
    "ş.arslanbey": 202727,
    "ş.çiftlik": 202728,
    "ş.derbent": 202729,
    "ş.köseköy": 202730,
    "ş.sarimeşe": 202732,
    "ş.suadiye": 202733,
    "ş.uzunbey": 202734,
    "ş.uzunbey_kumlaçiftliği": 202731,
    "sarimeşe": 202718,
    "serinlik_köyü": 202709,
    "şevkatiye": 202723,
    "şirinsulhiye_köyü": 202711,
    "suadiye": 202704,
    "sultaniye_köyü": 202707,
    "tepetarla": 202716,
    "uzunbey": 202712,
    "uzunbey_kumlaçiftliği": 202713,
    "uzunçiftlik": 204320,
    "uzuntarla": 146387,
    "yenieşme": 147665,


    "bağlarbaşi": 205833,
    "bayramoğlu": 205834,
    "cami": 205835,
    "darica": 181361,
    "darica_ş.": 181655,
    "fevziçakmak": 205838,
    "istasyon": 181362,
    "pirireis": 205836,
    "yali": 205841,
    "yeni": 205837,
    "zincirlikuyu": 205839,

    "çavuşlu": 23707,
    "çenedağ": 147315,
    "çınarlı": 148245,
    "deniz": 147854,
    "dumlupınar": 147838,
    "geredeli": 22956,
    "karagöllü": 23470,
    "kaşıkçı": 22821,
    "sırrıpaşa": 147536,
    "sopalı": 148357,
    "tahtalı": 23354,
    "terziler": 22834,
    "toylar": 170590,
    
}

SorguTimer = 1

while True:
    print("----------------------")
    
    print(f"Sorgu Sayısı = {SorguTimer}")


    ilce_kodu = input("İlçe Mahallesi: ")

    ilce_kodu = ilce_kodu.lower()


    # Mahalle adına karşılık gelen ilçe kodunu al
    if ilce_kodu in mahalleler:
        ilce_kodu_mahalle = mahalleler[ilce_kodu]
        SorguTimer += 1
        break
    else:
        print("Belirtilen mahalle bulunamadı.")

ada = input("Ada: ")
parsel = input("Parsel: ")
link = f"https://parselsorgu.tkgm.gov.tr/#ara/idari/{ilce_kodu_mahalle}/{ada}/{parsel}/"
webbrowser.open(link)
print("Uygulama Kapanıyor 3s")
time.sleep(3)
