# Pót ZH2

## Feladat megoldása és benyújtás

1. Nyissa meg:
   1. _VCS / Get from Version Control..._ VAGY
   2. _Git / Clone..._
2. A _Get From Version Control_ ablakban adja meg a jelen repository URL-jét: https://github.com/csekok/potZH2.git
3. Kattintson a _Clone_ gombra.
4. Válassza a _Git / GitHub / Share Project on GitHub_ lehetőséget.
5. Kattintson a _Project Is Already on GitHub_ ablakban a _Share Anyway_ gombra.
6. Kattintson a _Share Project On GitHub_ ablakban a _Share_ gombra.
7. A feladat megoldására 3 óra áll rendelkezésre.
8. A feladat befejezésekor, de legkésőbb a 3. óra leteltekor kommitolja fel a megoldást.

# Feladatkiírás

Bizonyára mindenki látott már rendőrjárőrt, aki szolgálata során egy út menti ellenőrző
pontról a forgalmat figyelte. A járőr feladata lehet a szabálytalankodók kiszűrése mellett
az elhaladó járművek szúrópróbaszerű vagy módszeres ellenőrzése. Bizonyos esetekben egy
műszaki ellenőrző állomás is kitelepül, amely alkalmas a kiválasztott járművek műszaki
állapotának felmérésére.
Egy olyan nap adatait kell feldolgoznia, amelyen a rendőri mellett műszaki ellenőrzés is
zajlott egy egyirányú út mentén. Az úton haladó járművek adatait
a _jarmu.txt_ állományban tárolta el a rendőrautó forgalomrögzítő kamerájához
csatlakoztatott gép. Az állomány sorai azonos szerkezetűek, az időt és a rendszámot
tartalmazzák az elhaladás sorrendjében. A rendszám mindig 7 karakter hosszú, az angol ábécé
nagybetűit, kötőjelet és számjegyeket tartalmaz ebben a sorrendben. 

Példa a _jarmu.txt_ fájl első néhány sorára:
<pre>
08 46 51 FD-2717
08 47 11 ZI-2088
08 48 52 EL-8894
08 50 34 SZ-3078
08 50 57 XY-8616
08 51 51 FY-2063
08 52 42 AY-2194
</pre>

A 2. sor mutatja, hogy a ZI-2088 jármű 8 óra 47 perc 11 másodperckor haladt át
az ellenőrző ponton. 

Írjon programot az alábbi feladatok megoldására:
1. Olvassa be a _jarmu.txt_ állományban talált adatokat, s annak felhasználásával oldja meg
a következő feladatokat!
2. Határozza meg, hogy aznap legalább hány óra hosszat dolgoztak az ellenőrzést végzők, ha
munkaidejük egész órakor kezdődik, és pontosan egész órakor végződik! (Minden óra 0
perc 0 másodperckor kezdődik, és 59 perc 59 másodperccel végződik.) Az eredményt
jelenítse meg a képernyőn!
3. A rendszám első karaktere külön jelentéssel bír. Az egyes betűk közül a „B” autóbuszt,
a „K” kamiont, az „M” motort jelöl, a többi rendszámhoz személygépkocsi tartozik.
Jelenítse meg a képernyőn, hogy az egyes kategóriákból hány jármű haladt el az ellenőrző
pont előtt!
4. Mettől meddig tartott a leghosszabb forgalommentes időszak? A választ jelenítse meg
a képernyőn a következő formában: _óó:pp:mm - óó:pp:mm_!
5. A rendőrök egy baleset közelében látott járművet keresnek rendszám alapján.
A szemtanúk csak a rendszám bizonyos karaktereire emlékeztek, így a rendszám
ismeretlen karaktereit a * karakterrel helyettesítve keresik a nyilvántartásban. Kérjen be
a felhasználótól egy ilyen rendszámot, majd jelenítse meg a képernyőn az arra illeszthető
rendszámokat! Ha nincs ilyen rendszámmal jármű, akkor jelenítse meg a _"Nem haladt el ilyen
rendszámmal jármű."_ feliratot!
6. Műszaki ellenőrzésre minden órában egy járművet választanak ki. Azt, amelyik abban az
órában először halad arra. Az ellenőrzés óráját és az ellenőrzött jármű rendszámát írja ki az
_ellenorzes.txt_ állományba a következő formában: _9 óra: GK-3407_! Minden óra adata külön
sorba kerüljön! Csak azon órák adatai kerüljenek kiíratásra, amikor volt ellenőrizhető jármű!

A program az alábbi modulokból kell, hogy álljon:
   1. _ido_: Egyetlen _Ido_ osztályt tartalmaz.</br>Az osztály attribútumai:
      - _ora_: Az idő óra értéke (0-23).
      - _perc_: Az idő perc értéke (0-59).
      - _masodperc_: Az idő másodperc értéke (0-59).
      </br>
      
      Az osztálynak legyenek saját metódusai.
   2. _jarmu_: Egyetlen _Jarmu_ osztályt tartalmaz.</br>Az osztály attribútumai:
      - _ido_: Az az _Ido_ objektum, ami a jármű elhaladásának időpontját tárolja.
      - _rendszam_: A jármű rendszáma.
      - _tipus_: A jármű típusa.
      </br>
      
      Az osztálynak legyenek saját metódusai.
   3. _ellenorzes_: Egyetlen _Ellenorzes_ osztályt tartalmaz.</br>Az osztály attribútumai:
      - _jarmuvek_: A járművek listája.
      </br>

      Az osztálynak legyen legalább 6 saját metódusa a feladatok megoldásával.
   4. _main_: Az _ellenorzes_ modul egyes metódusait hívja meg.

## Megoldás közben ügyeljen az alábbiakra

- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát!
- Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, milyen értéket vár!
- Ellenőrizze a felhasználó által megadott adatok helyességét, érvényességét!

## Minta a szöveges kimenetek kialakításához

A képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat sorszámát sem kiíratnia.

### Teszteset 1

<pre>
1. feladat: A jarmu.txt beolvasása.
2. feladat: Az ellenőrzést végzők legalább 5 órát dolgoztak.
3. feladat: Elhaladt járművek mennyisége típusonként:
	autóbusz: 10
	kamion: 12
	motor: 15
	szemelygépkocsi: 317
4. feladat: A leghosszabb forgalommentes időszak: 08:57:48 - 09:01:06.
5. feladat: Adja meg a keresett rendszámot: **
Nem haladt el ilyen rendszámmal jármű.
6. feladat: Az ellenőrzések adatainak kiíratása.
</pre>

### Teszteset 2

<pre>
1. feladat: A jarmu.txt beolvasása.
2. feladat: Az ellenőrzést végzők legalább 5 órát dolgoztak.
3. feladat: Elhaladt járművek mennyisége típusonként:
	autóbusz: 10
	kamion: 12
	motor: 15
	szemelygépkocsi: 317
4. feladat: A leghosszabb forgalommentes időszak: 08:57:48 - 09:01:06.
5. feladat: Adja meg a keresett rendszámot: **-7525
	YA-7525
6. feladat: Az ellenőrzések adatainak kiíratása.
</pre>

### Példa az _ellenorzes.txt_ fájl első néhány sorára:
<pre>
8 óra: FD-2717
9 óra: GK-3407
10 óra: RQ-8890
11 óra: IN-5066
12 óra: GC-0459
13 óra: CH-1893
</pre>