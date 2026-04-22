def m(cm):
    m = cm // 100
    cm = cm - m*100
    return str(m) + "meter" + str(cm) + "centimeter"

for i in range(3):
    név = input("Add meg a játékos nevét ")
    magasság = int(input ("Milyen Magas a játékos? "))
    print(név, m(magasság), 'magas')
    
