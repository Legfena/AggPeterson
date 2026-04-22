def deka(gramm):
    dkg = gramm // 10      
    g = gramm % 10         
    return str(dkg) + ' dekagramm ' + str(g) + ' gramm'

for i in range(3):
    nev = input('Add meg a zöldség nevét! ')
    suly = int(input('Mennyi a súlya? '))
    atszamitva = deka(suly)
    print('A(z)', nev, atszamitva, 'súlyú.')
