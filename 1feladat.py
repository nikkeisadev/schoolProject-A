import random, string

prefix = 'RANDOM> '
numList=[]
strList=""
saveList=""

def generatingValues(darabszam, darabbetu, hatarszam1, hatarszam2):
    for i in range(darabszam):
        x=random.randint(hatarszam1,hatarszam2)
        numList.append(x)

    for i in range(darabbetu):
        global strList
        szam=random.randint(1,21)
        for i in range(szam):
            strList=strList+random.choice(string.ascii_letters)
        strList=strList+';\n'

def savingValues():
    global saveList
    with open("ki.txt", "w") as f:
        for index in range (len(numList)):
            f.write(str(numList[index])+";")
            saveList=saveList+str(numList[index])+";"
        f.write("\n") 
        saveList=saveList+"\n"
        f.write(strList)
        saveList=saveList+strList

def checkingSave():
    with open("ki.txt", "r") as f:
        file=f.read()   
        if saveList==file:
            print(f"{prefix}A megadott paraméter megfelelő a feltételeknek.")
        else:
            print(f"{prefix}Nem megfelelő paramétert adott meg.")

darabszam=int(input(f"{prefix}Add meg a számok generálásának darabszámát: "))
darabbetu=int(input(f"{prefix}Add meg a betűk generálásának darabszámát: "))
hatarszam1=int(input(f"{prefix}Add meg a kisebbik határt: "))
hatarszam2=int(input(f"{prefix}Add meg a nagyobbik határt: "))

generatingValues(darabszam, darabbetu, hatarszam1, hatarszam2)
savingValues()
checkingSave()