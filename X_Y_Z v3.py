'''
ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄ¿
³    Nokta No    ³       Y       ³       X       ³    Z     ³
ÃÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄ´
³ 1              ³          17.10³          -2.32³      0.00³
³ 2              ³          13.68³         -15.19³      0.00³
³ 3              ³          28.87³         -24.72³      0.00³
³ 4              ³          84.71³         -15.27³      0.00³
³ 5              ³          80.86³          -2.98³      0.00³
³ 6              ³          82.90³         -33.44³      0.00³
³ 7              ³          46.83³           6.62³      0.00³
³ 8              ³          18.40³         -35.26³      0.00³
³ 9              ³          95.11³          -7.78³      0.00³
³ 10             ³          53.89³         -31.55³      0.00³
³ 11             ³          40.14³          -4.50³      0.00³
ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÙ
'''

DotFileText = []

table = ''

main = ''

title = '''
ÚÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄÄÄÄÄÂÄÄÄÄÄÄÄ¿
³ NoktaNo ³     Y    ³     X     ³   Z   ³
ÃÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄÄÄÄÄÅÄÄÄÄÄÄÄ´
'''

feed = '''ÀÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÄÄÄÄÁÄÄÄÄÄÄÄÙ
                    made.by.TanerSB
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
                    lineZ += '     '
                elif len(lineZ) == 2:
                    lineZ += '    '
                elif len(lineZ) == 3:
                    lineZ += '   '
                elif len(lineZ) == 4:
                    lineZ += '  '
                elif len(lineZ) == 5:
                    lineZ += ' '
                elif len(lineZ) == 6:
                    lineZ += ''
                elif len(lineZ) == 7:
                    lineZ += ''
                elif len(lineZ) == 8:
                    lineZ += ''
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



