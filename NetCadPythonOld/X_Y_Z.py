'''
ÚÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄ¿
³ NoktaNo ³    Y     ³     X     ³
ÃÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄ´
³1        ³ 497042.25³ 4499064.93³
³3        ³ 497043.94³ 4499093.86³
³5        ³ 497050.70³ 4499130.18³
³7        ³ 497061.47³ 4499134.56³
³9        ³ 497092.73³ 4499139.84³
³11       ³ 497091.50³ 4499072.93³
³13       ³ 497116.03³ 4499055.48³
³15       ³ 497140.21³ 4499054.81³
³17       ³ 497135.43³ 4499030.54³
³19       ³ 497151.66³ 4499001.89³
³21       ³ 497086.42³ 4498973.73³
³23       ³ 497054.62³ 4498955.74³
³25       ³ 497035.11³ 4498977.16³
³27       ³ 497016.37³ 4498989.62³
³29       ³ 497017.43³ 4498998.82³
³31       ³ 497031.17³ 4499023.53³
³33       ³ 497041.90³ 4499058.96³
³35       ³ 497059.90³ 4499105.92³
³37       ³ 497077.90³ 4499065.74³
ÀÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÙ
'''

DotFileText = []

table = ''

main = ''

title = '''
ÚÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄ¿
³ NoktaNo ³    Y     ³     X     ³    Z    ³
ÃÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄ´
'''

feed = '''ÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÙ
                    made by TanerSB
'''


def makeATablo():

    def readDotFile():
        global main
        global textLeng
        with open('nokta.NCN', 'r') as f:
            DotFileText = f.readlines()
            print(DotFileText)
            textLeng = len(DotFileText)
            for i in range(textLeng):
                line = DotFileText[i]
                if '\n' in line:
                    line = line.replace('\n','')
                if '"' in line:
                    line = line.replace('"', '')
                if ',' in line:
                    line = line.replace(',', '.')

                lineNumber= line.split(' ')[0]
                if len(lineNumber) == 1:
                    lineNumber += '      '
                elif len(lineNumber) == 2:
                    lineNumber += '     '
                elif len(lineNumber) == 3:
                    lineNumber += '    '
                elif len(lineNumber) == 4:
                    lineNumber += '   '
                elif len(lineNumber) == 5:
                    lineNumber += '  '
                else:
                    print('Numara hane olarak çok büyük.')
                lineNumber = '³  ' + lineNumber + '³'

                lineY = line.split(' ')[1]
                if ' ' in lineY:
                    lineY = lineY.replace(' ','')
                if len(lineY) == 1:
                    lineY += '        '
                elif len(lineY) == 2:
                    lineY += '       '
                elif len(lineY) == 3:
                    lineY += '      '
                elif len(lineY) == 4:
                    lineY += '     '
                elif len(lineY) == 5:
                    lineY += '    '
                elif len(lineY) == 6:
                    lineY += '   '
                elif len(lineY) == 7:
                    lineY += '  '
                elif len(lineY) == 8:
                    lineY += ' '
                elif len(lineY) == 9:
                    lineY += ''
                else:
                    print('Numara Y hane olarak çok büyük.')
                lineY = ' ' + lineY + '³'

                lineX = line.split(' ')[2]
                if ' ' in lineX:
                    lineX = lineX.replace(' ','')
                if len(lineX) == 1:
                    lineX += '        '
                elif len(lineX) == 2:
                    lineX += '       '
                elif len(lineX) == 3:
                    lineX += '      '
                elif len(lineX) == 4:
                    lineX += '     '
                elif len(lineX) == 5:
                    lineX += '    '
                elif len(lineX) == 6:
                    lineX += '   '
                elif len(lineX) == 7:
                    lineX += '  '
                elif len(lineX) == 8:
                    lineX += ' '
                elif len(lineX) == 9:
                    lineX += ''
                else:
                    print('Numara X hane olarak çok büyük.')
                lineX = ' ' + lineX + '³'

                lineZ = line.split(' ')[3]

                if ' ' in lineZ:
                    lineZ = lineZ.replace(' ','')
                if len(lineZ) == 1:
                    lineZ += '        '
                elif len(lineZ) == 2:
                    lineZ += '       '
                elif len(lineZ) == 3:
                    lineZ += '      '
                elif len(lineZ) == 4:
                    lineZ += '     '
                elif len(lineZ) == 5:
                    lineZ += '   '
                elif len(lineZ) == 6:
                    lineZ += '   '
                elif len(lineZ) == 7:
                    lineZ += '  '
                elif len(lineZ) == 8:
                    lineZ += ' '
                else:
                    print('Numara Z hane olarak çok büyük.')
                lineZ = ' ' + lineZ + '³'

                main += lineNumber + lineY + lineX + lineZ + '\n'
                #print(line)

            with open(f'{textLeng}_Number_Of_Table_tanersb.CKS','w') as f:

                table = title + main + feed
                f.write(table)
                print(table)

    readDotFile()

makeATablo()



