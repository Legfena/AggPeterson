import operator

class filmek:
    def __init__(self,cím,ar):
        self.cím=cím
        self.ar=int(ar)

dvdk=[]
szum=0
fbe=open('dvdar.txt','r')
print('A fájl tartalma:')
for sor in fbe:
    sor=sor.strip().split(' ')
    dvdk.append(filmek(sor[0],sor[1]))
    print(sor[0],sor[1],'Ft',sep=' ')
    szum=szum+int(sor[1])
fbe.close()

print('Az átlagos DVD ár: ',round(szum/len(dvdk),1),'Ft')

dvdk.sort(key=operator.attrgetter('ar'))

print('A legolcsóbb DVD adatai:',dvdk[0].cím,dvdk[0].ar,'Ft')

fki=open('legolcsobbdvd.txt','w')
print('A legolcsóbb DVD adatai:',dvdk[0].cím,dvdk[0].ar,'Ft',file=fki)
fki.close()
