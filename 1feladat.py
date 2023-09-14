import random
import string

darabszam=int(input("Add meg a darabszámot: "))
hatarszam1=int(input("Add meg a kisebb határt: "))
hatarszam2=int(input("Add meg a nagyobb határt: "))
szamok=[]
betuk=""
ellenorzes=""

darabbetu=int(input("Add meg a darabszámot: "))

for i in range(darabszam):
    x=random.randint(hatarszam1,hatarszam2)
    szamok.append(x)
print(szamok)

for i in range(darabbetu):
    szam=random.randint(1,21)
    for i in range(szam):
        betuk=betuk+random.choice(string.ascii_letters)
    betuk=betuk+';\n'
print(betuk)

with open("ki.txt", "w")as f:
    f.close()
with open("ki.txt", "a") as f:
    for index in range (len(szamok)):
        f.write(str(szamok[index])+";")
        ellenorzes=ellenorzes+str(szamok[index])+";"
    f.write("\n") 

with open("ki.txt", "a")as f:
    f.write(betuk)
    ellenorzes=ellenorzes+betuk
with open("ki.txt", "r") as f:
    file=f.read()   
    if ellenorzes==file:
        print("A megadott paraméter megfelelő a feltételeknek.")
    else:
        print("Nem megfelelő paramétert adott meg.")

