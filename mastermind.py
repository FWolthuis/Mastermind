from time import sleep
from termcolor import colored
import math
import os

Red = (colored('0', 'red'))
Yellow = (colored('0', 'yellow'))
Green = (colored('0', 'green'))
Cyan = (colored('0', 'cyan'))
Blue = (colored('0', 'blue'))
Magenta = (colored('0', 'magenta'))

Gray = (colored('><', 'grey'))
White = (colored('<>', 'white'))

Choice1 = None
Choice2 = None
Choice3 = None
Choice4 = None

Solution = [Choice1, Choice2, Choice3, Choice4]

Row1 = [Choice1, Choice2, Choice3, Choice4]
Row2 = [Choice1, Choice2, Choice3, Choice4]
Row3 = [Choice1, Choice2, Choice3, Choice4]
Row4 = [Choice1, Choice2, Choice3, Choice4]
Row5 = [Choice1, Choice2, Choice3, Choice4]
Row6 = [Choice1, Choice2, Choice3, Choice4]
Row7 = [Choice1, Choice2, Choice3, Choice4]
Row8 = [Choice1, Choice2, Choice3, Choice4]
Row9 = [Choice1, Choice2, Choice3, Choice4]
Row10 = [Choice1, Choice2, Choice3, Choice4]
Row11 = [Choice1, Choice2, Choice3, Choice4]
Row12 = [Choice1, Choice2, Choice3, Choice4]

clear = lambda: os.system('cls')


def startscreen():
    
    #print(Red, Yellow, Green, Cyan, Blue, Magenta, Gray, White)
    
    print('----------------------')
    print('hello')
    print('----------------------')

def screen():
    print(Solution)
    
def Choices():
    global Choice1
    global Choice2
    global Choice3
    global Choice4
    
    Input1 = input('Colour nr.1 is: ')
    if Input1 == 'red':
        Choice1 = Red
        Solution.append(Choice1)

    elif Input1 == 'yellow':
        Choice1 = Yellow
        Solution.append(Choice1)
    
    elif Input1 == 'green':
        Choice1 = Green
        Solution.append(Choice1)
        
    elif Input1 == 'cyan':
        Choice1 = Cyan
        Solution.append(Choice1)
        
    elif Input1 == 'blue':
        Choice1 = Blue
        Solution.append(Choice1)
        
    elif Input1 == 'magenta':
        Choice1 = Magenta
        Solution.append(Choice1)
    
    Input2 = input('Colour nr.2 is: ')
    if Input2 == 'red':
        Choice2 = Red
        Solution.append(Choice2)

    elif Input2 == 'yellow':
        Choice2 = Yellow
        Solution.append(Choice2)
    
    elif Input2 == 'green':
        Choice2 = Green
        Solution.append(Choice2)
        
    elif Input2 == 'cyan':
        Choice2 = Cyan
        Solution.append(Choice2)
        
    elif Input2 == 'blue':
        Choice2 = Blue
        Solution.append(Choice2)
        
    elif Input2 == 'magenta':
        Choice2 = Magenta
        Solution.append(Choice2)
    
    Input3 = input('Colour nr.3 is: ')
    if Input3 == 'red':
        Choice3 = Red
        Solution.append(Choice3)

    elif Input3 == 'yellow':
        Choice3 = Yellow
        Solution.append(Choice3)
    
    elif Input3 == 'green':
        Choice3 = Green
        Solution.append(Choice3)
        
    elif Input3 == 'cyan':
        Choice3 = Cyan
        Solution.append(Choice3)
        
    elif Input3 == 'blue':
        Choice3 = Blue
        Solution.append(Choice3)
        
    elif Input3 == 'magenta':
        Choice3 = Magenta
        Solution.append(Choice3)
    
    Input4 = input('Colour nr.4 is: ')
    if Input4 == 'red':
        Choice4 = Red
        Solution.append(Choice4)

    elif Input4 == 'yellow':
        Choice4 = Yellow
        Solution.append(Choice4)
    
    elif Input4 == 'green':
        Choice4 = Green
        Solution.append(Choice4)
        
    elif Input4 == 'cyan':
        Choice4 = Cyan
        Solution.append(Choice4)
        
    elif Input4 == 'blue':
        Choice4 = Blue
        Solution.append(Choice4)
        
    elif Input4 == 'magenta':
        Choice4 = Magenta
        Solution.append(Choice4)
    
    clear()
    screen()





clear()
sleep(1)
startscreen()
Choices()




