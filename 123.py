def percms(masodperc):
    perc = masodperc // 60
    ms = masodperc % 60
    return str(perc) + ' perc ' + str(ms) + ' másodperc'

for i in range(3):
    cím = input('Add meg egy zene címét! ')
    hossz = int(input('Hány másodperces a zene? '))
    print('A(z)', cím, 'című zene', percms(hossz), 'hosszú.')
