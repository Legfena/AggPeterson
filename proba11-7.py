elso = input('Add meg a számot')
elso = int(elso)
print('A beadott szám:', elso)
if (elso%7!=0) and (elso%11!=0):
    print('A szám nem osztható sem 7-tel sem 1l-gyel')
if (elso%7==0):
    print('A szám osztható 3-mal.')
if (elso%11==0):
    print('Az szám osztható 2-vel.')
