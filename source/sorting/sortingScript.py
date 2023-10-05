#Importing neccesary packages.
import os, time, sys
from time import sleep
#Early Terminal setup.
cmd = 'mode 67,17'
os.system(cmd)
cmd= 'color 03'
os.system(cmd)
#Main variables, accessable from anywhere as global variables.
ints = []
mainList = []
argValue = None
freshInject = ''
preOrderType = None
questionInject = False
doValuesCheck =  True
doAppend = None
#Asking the user that which option do he/she want's to choose.
def getOrder():
    global preOrderType
    preOrderType = str(input('[SORTER]> Welcome! Tell me which option do you want to choose?\n          Ascending or Descending order? [1/2]> '))
#Opening the file, spliting, and placing into the main list.
def readFile():
    global mainList
    #Reading file.
    with open("ki.txt", 'r') as f:
        mainList = f.read().removesuffix(";").split(";")
#Just to make it look better...
os.system('cls')
logo = """ 
 _____         _           
|   __|___ ___| |_ ___ ___ 
|__   | . |  _|  _| -_|  _|
|_____|___|_| |_| |___|_|  --------> S O R T E R | Made by: Nikke

"""
for char in logo:
    sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()
#Displaying newly readed values.
print('[SORTER]> Readed values: ', open("ki.txt", 'r').read())
#Checking values, converting string numbers to ints.
def valuesCheck():
    #Local variables.
    doAgain = True
    #Global variables.
    global ints
    global mainList
    global argValue
    global doAppend
    ints.clear()
    #I dun wanna duplicate every item in the list...
    if doAgain:
        #Checking the file, strings or ints.
        argValue = all(ele.isdigit() for ele in mainList)
        #If the file contains ints, then we need to convert them from string numbers to integers.
        if argValue:
            for element in mainList:
                ints.append(int(element))
            if doAppend:
                ints.append(int(freshInject))
                doAppend = False
#Method for quick ascending sorting. (Only int.)
def fastOrderAscending(readableList):
    small = []
    equals = []
    bigger = []
    mainList.clear()
    small.clear()
    equals.clear()
    bigger.clear()
    size = len(readableList)

    if size <= 1:
        return readableList

    pivot = readableList[size-1]
    for num in readableList:
        if num < pivot:
            small.append(num)
        if num == pivot:
            equals.append(num)
        if num > pivot:
            bigger.append(num)
    return fastOrderAscending(small) + equals + fastOrderAscending(bigger)

#Method for bubble ascending sorting. (Only String.)
def bubbleSortStringAscent(s):
	chars = list(s)
	n = len(chars)
	for i in range(n):
		for j in range(0, n-i-1):
			if chars[j] > chars[j+1]:
				chars[j], chars[j+1] = chars[j+1], chars[j]
	return ''.join(chars)

#There is no need to reverse the main sorting definitions. Only eating space.
def reverseStringValues(x):
    #Reversing the value, so ascent result will be descent result.
    return x[::-1]

def appendingNewInject():
    #Globals here.
    global mainList
    global questionInject
    global freshInject
    global ints
    #Creating the half reseted enviorment to work with the newly injected item!
    mainList.clear()
    ints.clear()
    readFile()
    mainList.append(freshInject)
    valuesCheck() 
    questionInject = False
    doValuesCheck = False

#Main part of the code, processing every order, as the user wanted.
def processOrders():
    #Define global values.
    global ints
    global preOrderType
    global doAppend
    global mainList
    global argValue
    global questionInject
    global freshInject
    global doValuesCheck
   #Read this! There are 2 types of orders in this code: the Quick type, and the Bubble method.
   #Qucik sorting used for ints, it's easier for them, and Bubble for only strings.
   #So there is one mentioned sorting type, and one that's did'nt mentioned.
   #After sorting, the program will ask that do you want to inject one more item.
    if questionInject:
        if input("[SORTER]> Would you like to inject one more item? [y/n]: ") == 'y':    
            if argValue == False: 
                #Asking for new item into the list.
                freshInject = input("[SORTER]> Please type a new item: ")
                appendingNewInject()
                print(f'[SORTER]> Added one more item! [{freshInject}]<-----')
                doValuesCheck = False
                doAppend = True
                processOrders()
            else:
                #Asking for new item into the list.
                freshInject = input("[SORTER]> Please type a new item: ")
                appendingNewInject()
                print(f'[SORTER]> Added one more item! [{freshInject}]<-----')
                doValuesCheck = False
                doAppend = True
                processOrders()
        else:
            #Reseting the UI, and list.
            questionInject = False
            ints.clear()
            mainList.clear()
            getOrder()
            readFile()
            processOrders()
    #Ascending or Descending orders are processed.
    valuesCheck()
    if preOrderType == '1':
        #Fast order process.
        if argValue is True:
            print(mainList)
            print('[SORTER]> Ascending order with Quick Sort method:\n         ', fastOrderAscending(ints))
            questionInject = True
            processOrders()
        #Bubble order process.
        elif argValue is False:
            print('[SORTER]> Ascending order with Bubble Sort method:\n         ', bubbleSortStringAscent(mainList))
            questionInject = True
            processOrders()
    elif preOrderType == '2':
        #Bubble order process.
        valuesCheck()
        if argValue is False:
            print('[SORTER]> Descending order with Bubble Sort method:\n         ', reverseStringValues(bubbleSortStringAscent(mainList)))
            questionInject = True
            processOrders()
        #Fast order process.
        elif argValue is True:
            print(mainList)
            print('[SORTER]> Descending order with Quick Sort method:\n         ', reverseStringValues(fastOrderAscending(ints)))
            questionInject = True
            processOrders()
    else: print(f'Wrong parameter! [{preOrderType}]<----'), getOrder()
#Initializing definitions.
#----------------------------------------->
readFile()
getOrder()
processOrders()
#   Debug sections:
#       reverseStringValues(*debuglisthere*)
#----------------------------------------->
