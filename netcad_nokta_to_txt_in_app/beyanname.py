'''
pafta = input('pafta: ')

ada = input('ada: ')

parsel = input('parsel: ')

bölüm = input('kaça bölündü: ')

cinsi = input('cinsi: ')

maliki = input('maliki: ')

kütükNo = input('kütükNo: ')

'''

kütükNo = '1/80'

maliki = 'mehmet çelik ve hiss'

cinsi = 'Arsa'

bölüm = '5'




def YeniParseller(bölüm):
    bölümler = int(bölüm)
    alfabe= 'ABCDEFGHIJKLMNOPRSTUVYZ'
    harfler= ''
    for i in range(bölümler):
        harfler += alfabe[i] + ' '

        print(harfler)
    return harfler



YeniParseller(bölüm)



pafta = 'asdsad'

ada = '123'

parsel = '123'

düşünceler = f'{ada} ADA {parsel} PARSEL İFRAZ OLDU, {YeniParseller(bölüm)}PARSELLERİ OLUŞTURULDU'


text =f'''
{kütükNo}  {pafta}  {ada}  {parsel}         {cinsi}  {maliki}  {düşünceler}

'''

print(text)