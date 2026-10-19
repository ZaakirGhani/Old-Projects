import threading
import time
import matplotlib.pyplot as plt

flag = False

def man():
    global flag
    print('Man')
    time.sleep(1)
    if flag:
        time.sleep(10)
        return
    
    

def terra():
    global flag
    time.sleep(8)
        
    print('terra')

def iggy():
    global flag
    flag =True
    time.sleep(10)
    print('iggy')
    

mans = threading.Thread(target=man)
terras = threading.Thread(target=terra)
iggie = threading.Thread(target=iggy)

mans.start()
terras.start()
iggie.start()

flag = True
mans.join()



