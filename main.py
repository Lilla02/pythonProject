print("1. feladat: A jarmu.txt beolvasása.")
fajl = open("jarmu.txt")
ora = []
perc = []
mp = []
rendszam = []
for sor in fajl:
    sor = sor.strip().split()
    ora.append(int(sor[0]))
    perc.append(int(sor[1]))
    mp.append(int(sor[2]))
    rendszam.append(sor[3])
db = len(ora)
fajl.close()


print("2. feladat: Az ellenőrzést végzők legalább ennnyi órát dolgoztak:", ora[db-1] - ora[0] + 1, "óra")


print("3. feladat: Elhaladt járművek mennyisége típusonként:", end="")
busz = 0
kamion = 0
motor = 0
auto = 0
for i in range(db):
    if rendszam[i][0] == "B":
        busz += 1
    elif rendszam[i][0] == "K":
        kamion += 1
    elif rendszam[i][0] == "M":
        motor += 1
    else:
        auto += 1
print("\t" + "Buszok száma:", busz)
print("\t" + "Kamionok száma:", kamion)
print("\t" + "Motorok száma:", motor)
print("\t" + "Autók száma:", auto)
print()


mperc = []
for i in range(db):
    mperc.append(ora[i]* 3600 + perc[i] * 60 + mp[i])
maxx = 0
for i in range(db-1):
    if mperc[i+1] - mperc[i] > maxx:
        maxx = mperc[i+1] - mperc[i]
for i in range(db-1):
    if mperc[i+1] - mperc[i] == maxx:
        print("4. feladat: A leghosszabb forgalommentes időszak: "+str(ora[i])+":"+str(perc[i])+":"+str(mp[i])+" - "+str(ora[i+1])+":"+str(perc[i+1])+":"+str(mp[i+1]))


felismert = input("5. feladat: Adja meg a felismert rendszámot (7 karakter)! ")
egyezes = 0
for i in range(db):
    for j in range(len(rendszam[i])):
        if rendszam[i][j] == felismert[j] or felismert[j] == "*":
            egyezes += 1
    if egyezes == 7:
        print(rendszam[i])
    egyezes = 0


print("6. feladat: Az ellenőrzések adatainak kiíratása. ", end="")
ora_lista = []
ora_rendszam = []
for i in range(db):
    if ora[i] not in ora_lista:
        ora_lista.append(ora[i])
        ora_rendszam.append(rendszam[i])
for j in range(len(ora_lista)):
    print("\t" + str(ora_lista[j]) + ".óra:", ora_rendszam[j])
print()
"""
print(ora[0],"óra:", rendszam[0])
for i in range(db-1):
    if ora[i] != ora[i+1]:
        print(ora[i+1], "óra:", rendszam[i+1])
"""