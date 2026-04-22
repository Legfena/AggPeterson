with open('hello.txt') as f:
    elso = f.readline()
    print('A fájl első sora:', elso)
    for line in f:
        print('Egy sor:', line)

