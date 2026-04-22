a = 5
f = open('hello1.txt', 'w')
f.write('A változó értéke: {}\n'.format(a))
print('A változó értéke:',a,file=f)

f.close()
