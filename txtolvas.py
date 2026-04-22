be=open ("eredmenyek_20210109.txt", "r")
adat=[]
for sor in be:
    sor=sor.strip().split(" ")
    ford=sor[0]
    hazai=sor[1]
    hazaiered=int(sor[2])
    vendegered=int(sor[3])
    vendeg=sor[4]
    adat.append([ford, hazai, hazaiered, vendegered, vendeg])
be.close()
print("1. feladat - Fájlok beolvasása.")
print(adat)
