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
preOrderType = None
questionInject = False

#Asking the user that which option do he/she want's to choose.
def getOrder():
    global preOrderType
    preOrderType = str(input('[SORTER]> Welcome! Tell me which option do you want to choose?\n          Descending, or Ascending order? [1/2]> '))

#Opening the file, spliting, and placing into the main list.
def readFile():
    global mainList
    global argValue
    #Reading file.
    with open("ki.txt", 'r') as f:
        mainList = f.read().split(";")
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
    print('[SORTER]> Readed values: ', mainList)

#Checking values, converting string numbers to ints.
def valuesCheck():
    #Global variables.
    global ints
    global mainList
    global argValue
    #Checking the file, strings or ints.
    argValue = all(ele.isdigit() for ele in mainList)
    #If the file contains ints, then we need to convert them from string numbers to integers.
    if argValue:
        for element in mainList:
            ints.append(int(element))

#Method for quick ascending sorting. (Only int.)
def fastOrderAscending(readableList):
    small = []
    equals = []
    biger = []
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
            biger.append(num)

    return fastOrderAscending(small) + equals + fastOrderAscending(biger)

#Method for quick descending sorting. (Only int.)
def fastOrderDescending():
    global mainList
    fastOrderAscending(mainList)
    mainList.reverse()

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

#Shutdown animation
def shutDown():
    os.system('cls')
    shutdownScreen = '''   



                     _____             __           
                    / ___/____  ______/ / ____ _____
                    \__ \/ __ \/  ___/ __/ _ \/ ___/
                    __/ / /_/  / /  / /_/  __/ /    
                  /____/\____ /_/   \__/\___/_/     
    


    '''
    for char in shutdownScreen:
        sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    os.system('cls')
    exit()
#Main part of the code, processing every order, as the user wanted.
def processOrders():
    #Define global values.
    global ints
    global preOrderType
    global mainList
    global argValue
    global questionInject
   #Read this! There are 2 types of orders in this code: the Quick type, and the Bubble method.
   #Qucik sorting used for ints, it's easier for them, and Bubble for only strings.
   #So there is one mentioned sorting type, and one that's did'nt mentioned.
   #After sorting, the program will ask that do you want to inject one more item.
    if questionInject:
        if input("[SORTER]> Would you like to inject one more item? [y/n]: ") == 'y':    
            if argValue == False: 
                #Asking for new item into the list.
                freshInject = input("[SORTER]> Please type a new item: ")
                mainlist.delete()
                readFile()
                mainList.append(freshInject)

                valuesCheck() 
                questionInject = False
            else:
                #Asking for new item into the list.
                freshInject = input("[SORTER]> Please type a new item: ")
                mainlist.delete()
                readFile()
                mainList.append(freshInject)

                valuesCheck() 
                questionInject = False
        else:
            #Exiting if the user chooses no, or press anything else.
            shutDown()
    
    #Ascending or Descending orders are processed here.
    if preOrderType == '1':
        #Fast order process.
        valuesCheck()
        print('[SORTER]> Ascending selected!')
        if argValue is True:
            print('[SORTER]> Ascending order with Quick Sort method:  ', fastOrderAscending(ints))
            questionInject = True
            processOrders()
        #Bubble order process.
        elif argValue is False:
            print('[SORTER]> Ascending order with Bubble Sort method:  ', bubbleSortStringAscent(mainList))
            questionInject = True
            processOrders()
    elif preOrderType == '2':
        #Bubble order process.
        valuesCheck()
        print('[SORTER]> Descending selected!')
        if argValue is False:
            print('[SORTER]> Descending order with Bubble Sort method: ', reverseStringValues(bubbleSortStringAscent(mainList)))
            questionInject = True
            processOrders()
        #Fast order process.
        elif argValue is True:
            print('[SORTER]> Descending order with Quick Sort method:', reverseStringValues(fastOrderAscending(ints)))
            questionInject = True
            processOrders()
    else: print(f'Wrong parameter! [{preOrderType}]<----'), getOrder()

#Initilazing definitions.
#----------------------------------------->
readFile()
getOrder()
processOrders()
#   Debug sections:
#       reverseStringValues(*debuglisthere*)
#----------------------------------------->
