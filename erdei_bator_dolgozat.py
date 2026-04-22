def dekagramm(gramm):
    dkg = gramm // 10
    g = gramm
    return str(dkg) + '  dekagramm ' + str(g) + ' gramm '

for i in range(4):
    név = input ('Add meg a hús nevét ')
    súly = int(input('mennyi a súlya? '))
    print ('A(z) ', név, dekagramm(súly), 'súlyú ')
