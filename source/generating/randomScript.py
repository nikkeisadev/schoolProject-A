import random, string

prefix = 'RANDOM> '
numList=[]
strList=""
saveList=""
dontes = None
print("""

----> R A N D O M
Varga Máté, Python  <----
""")

def generatingValues(darabszam, hatarszam1, hatarszam2):
    for i in range(darabszam):
        x=random.randint(hatarszam1,hatarszam2)
        numList.append(x)
def generatingBetu( darabbetu):
    for i in range(darabbetu):
        global strList
        szam=random.randint(1,21)
        for i in range(szam):
            strList=strList+random.choice(string.ascii_letters)
        strList=strList+';\n'

def savingValues():
    global saveList
    with open("data/ki.txt", "w") as f:
        for index in range (len(numList)):
            f.write(str(numList[index])+";")
            saveList=saveList+str(numList[index])+";"
        f.write("\n") 
        saveList=saveList+"\n"
        f.write(strList)
        saveList=saveList+strList

def checkingSave():
    with open("data/ki.txt", "r") as f:
        file=f.read()   
        if saveList==file:
            print(f"{prefix}A megadott paraméter megfelelő a feltételeknek.")
        else:
            print(f"{prefix}Nem megfelelő paramétert adott meg.")
def bekeres():
    global dontes
    global darabbetu
    global darabszam
    global hatarszam1
    global hatarszam2
    dontes=int(input("Add meg hogy mit generáljunk(1-szám, 2-betű): "))
    if dontes ==1: 
        darabszam=int(input(f"{prefix}Add meg a számok generálásának darabszámát: "))  
        hatarszam1=int(input(f"{prefix}Add meg a kisebbik határt: "))
        hatarszam2=int(input(f"{prefix}Add meg a nagyobbik határt: "))
    else:
        darabbetu=int(input(f"{prefix}Add meg a betűk generálásának darabszámát: "))
try:
    bekeres()
except:
    bekeres()
if dontes == 1:
    generatingValues(darabszam, hatarszam1, hatarszam2)
else:
    generatingBetu( darabbetu)

savingValues()
checkingSave()
