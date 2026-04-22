elso = input('Adj meg a számot! ')
elso = int(elso)
print('A beadott szám:', elso)
if (elso%3!=0) and (elso%2!=0):
    print('A szám nem osztható sem 2-vel sem 3-mal.')
if (elso%3==0):
    print('A szám osztható 3-mal.')
if (elso%2==0):
    print('Az szám osztható 2-vel.')
