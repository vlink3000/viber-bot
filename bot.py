import pyautogui, time

# print(pyautogui.position())

import random

from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

for mciNumbers in range(0,100):

	# genarate phone number
    phoneNumber = '+38098' + str(random_with_N_digits(7))
    
    time.sleep(1)

    #clear search bar
    pyautogui.click(x=236, y=161)
    print ("Почистил поиск")

    time.sleep(1)

    #click on search bar
    pyautogui.click(x=115, y=155)
    print ("Я кликнул на поиск")

	#show generated number
    print("Я сгенерировал номер: " + phoneNumber)
    time.sleep(0.5)

    #type phone number	
    pyautogui.typewrite(phoneNumber)
    print("Я ввёл номер: " + phoneNumber)

    time.sleep(1)

    #press enter
    pyautogui.keyDown('enter')
    print("Я нажал Enter")

    time.sleep(1)

    #try to click search result
    pyautogui.click(x=72, y=222)
    print("Кликаю на найденый контакт")
 
    time.sleep(1)

    #click on message input
    pyautogui.click(x=603, y=708)
    print("Кликаю в поле отправки сообщения")
   
    time.sleep(1)

    #type message
    message = random.choice(list(open('viber0.txt')))
    pyautogui.typewrite(message)
    print("Попробовал написать сообщение")

    time.sleep(0.3)

    #send a message
    pyautogui.click(x=1210, y=704)
    print("Попробовал отправить сообщение. Повторяю алгоритм!")
    print("==================================================")    
    
