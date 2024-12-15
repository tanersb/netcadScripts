import time

nokta_list=[
'100209.03	104093.33',
'100213.25	104090.21',
'100218,41	104056.10',
]
nokta_numara_list=[]
noktalar=(
"""
100209.03	104093.33
100213.25	104090.21
100218,41	104056.10
100215.72	104052.63
100144,11	104043.62
100139.29	104047.31
100137.10	104061.62
100133.54	104084.82
100137.85	104085.31
100215.35	104076.33
""")


def virgulToNokta(noktalar):
    noktalar=noktalar.replace(',','.')
    print(noktalar)

    return noktalar

def listToString(noktalar):
    global nokta_string
    nokta_string=''
    for sutun in noktalar:
        nokta_string= nokta_string + sutun

    return nokta_string

def stringToList(noktalar):
    nokta_listesi=noktalar.split('\n')
    for index, satir in enumerate(nokta_listesi):
        satir.strip()
        if satir == '':
            pass
        else:
            nokta_list.append(satir.strip())

    return nokta_list

def noktaNumarasi(noktalar):
    for index, sutun in enumerate(noktalar,start=1):
        nokta_numara_list.append(str(index) + '\t' + sutun)

    return nokta_numara_list


def numaraGir():
    global chose
    print("""
[1] * Virgülleri Nokta Yap.
[2] * Listeyi String Yap.
[3] * Stringi Liste Yap.
[4] * Nokta Numarası Ekle.
    """)
    try:
        chose = int(input('Numara Girin:'))
        dogruNumara(chose)
    except:
        print('Lütfen sadece numara giriniz..')
        time.sleep(.5)
        numaraGir()
    return chose


def dogruNumara(chose):
    if type(chose) == int:
        if chose == 1:
            virgulToNokta(noktalar)
            time.sleep(.5)
            print('Virgüller Nokta Oldu.')
        elif chose == 2:
            listToString(noktalar)
            print('Liste String Oldu.')
            time.sleep(.5)
            print(nokta_string)
        elif chose == 3:
            stringToList(noktalar)
            print('String Liste Oldu.')
            time.sleep(.5)
            print(nokta_list)
        elif chose == 4:
            noktaNumarasi(nokta_list)
            print('Nokta Numarası Eklendi.')
            time.sleep(.5)
            print(nokta_numara_list)
        else:
            print(f'Sayınız {chose}. Lütfen 1\'den 4\'e kadar giriniz.')
            time.sleep(2)
            numaraGir()
    else:
        numaraGir()


numaraGir()
