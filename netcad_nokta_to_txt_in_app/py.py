koordineözet = '''
ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄ¿
³ NoktaNo    ³    Y     ³     X     ³ NoktaNo    ³    Y     ³     X     ³
ÃÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄ´
³1           ³ 497042.25³ 4499064.93³ 2          ³ 497043.12³ 4499079.91³
³3           ³ 497043.94³ 4499093.86³ 4          ³ 497045.35³ 4499105.82³
³5           ³ 497050.70³ 4499130.18³ 6          ³ 497054.04³ 4499132.63³
³7           ³ 497061.47³ 4499134.56³ 8          ³ 497072.39³ 4499136.40³
³9           ³ 497092.73³ 4499139.84³ 10         ³ 497111.83³ 4499110.54³
³11          ³ 497091.50³ 4499072.93³ 12         ³ 497100.87³ 4499066.27³
³13          ³ 497116.03³ 4499055.48³ 14         ³ 497127.95³ 4499052.20³
³15          ³ 497140.21³ 4499054.81³ 16         ³ 497149.44³ 4499054.72³
³17          ³ 497135.43³ 4499030.54³ 18         ³ 497139.17³ 4499023.94³
³19          ³ 497151.66³ 4499001.89³ 20         ³ 497152.02³ 4499001.24³
³21          ³ 497086.42³ 4498973.73³ 22         ³ 497063.82³ 4498974.88³
³23          ³ 497054.62³ 4498955.74³ 24         ³ 497048.50³ 4498963.93³
³25          ³ 497035.11³ 4498977.16³ 26         ³ 497024.27³ 4498984.11³
³27          ³ 497016.37³ 4498989.62³ 28         ³ 497014.90³ 4498994.27³
³29          ³ 497017.43³ 4498998.82³ 30         ³ 497030.00³ 4499021.44³
³31          ³ 497031.17³ 4499023.53³ 32         ³ 497035.70³ 4499036.08³
³33          ³ 497041.90³ 4499058.96³ 34         ³ 497060.83³ 4499065.35³
³35          ³ 497059.90³ 4499105.92³ 36         ³ 497073.89³ 4499113.03³
³37          ³ 497077.90³ 4499065.74³ 38         ³ 497077.37³ 4499089.18³
ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÙ
'''


numara = '1'  # 12 haneli ilk 1 hensi zaten boş olacak

numaraY = '497091.50'

numaraX = '4499055.40'

def numaraCheck(numara):
    if len(numara) == 1:
        numara += '          '# 10
    elif len(numara) == 2:
        numara += '         '# 9
    elif len(numara) == 3:
        numara += '        '# 8
    elif len(numara) == 4:
        numara += '       '# 7
    elif len(numara) == 5:
        numara += '      '# 6
    elif len(numara) == 6:
        numara += '     '# 5
    elif len(numara) == 7:
        numara += '    '# 4
    elif len(numara) == 8:
        numara += '   '# 3
    elif len(numara) == 9:
        numara += '  '# 2
    elif len(numara) == 10:
        numara += ' '# 1
    else:
        print('Numara hane olarak çok büyük.')
    numara = ' ' + numara
    print(numara)
    return numara

def numaraYCheck(numaraY):
    numaraY = ' ' + str(numaraY) + ' '
    print(numaraY)
    return numaraY

def numaraXCheck(numaraX):
    numaraX = ' ' + str(numaraX) + ' '
    print(numaraX)
    return numaraX


közzet=f'''
ÚÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄ¿
³ NoktaNo    ³    Y      ³     X      ³ 
ÃÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄ´
³{numaraCheck(numara)}³{numaraYCheck(numaraY)}³{numaraXCheck(numaraX)}³
'''

print(közzet)

with open('cıktı.cks' , 'w') as f:
    f.write(közzet)


def readDotFile():
    with open('Nokta.CKS' , 'r') as f:
        DotFileText = f.read()
        print(DotFileText)



readDotFile()