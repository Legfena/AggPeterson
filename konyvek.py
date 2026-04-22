class konyvek:
    def __init__(self, cim, ar):
        self.cim = cim
        self.ar = int(ar)

konyv_lista = []

with open("konyvek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adat = sor.strip().split()
        cim = adat[0]
        ar = adat[1]
        k = konyvek(cim, ar)
        konyv_lista.append(k)

print("A beolvasott könyvek adatai:")
for k in konyv_lista:
    print(f"{k.cim} {k.ar} Ft")

osszeg = sum(k.ar for k in konyv_lista)
atlag = osszeg / len(konyv_lista)
print(f"A könyvek átlagos ára: {int(atlag)} Ft")


legdragabb = max(konyv_lista, key=lambda x: x.ar)
print(f"A legdrágább áru adatai: {legdragabb.cim} {legdragabb.ar} Ft")


with open("legdragabb.txt", "w", encoding="utf-8") as f:
    f.write(f"{legdragabb.cim} {legdragabb.ar} Ft")
