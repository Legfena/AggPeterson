elso = input('Adj meg a számot! ')
elso = int(elso)
print('A beadott szám:', elso)
if (elso%2!=0) and (elso%7!=0):
    print('A szám nem osztható sem 2-vel sem 7-tel.')
if (elso%2==0):
    print('A szám osztható 2-vel.')
if (elso%7==0):
    print('Az szám osztható 7-tel.')
