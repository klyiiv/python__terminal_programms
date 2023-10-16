import threading
import time
def sleep(hours):
    time.sleep(5 - hours ** 2)
    print (hours, end="")

sleep1 = threading.Thread(target=sleep, args= (0,))
sleep2 = threading.Thread(target=sleep, args= (2,))
sleep3 = threading.Thread(target=sleep, args=(-1,))
           
sleep2.start()
sleep1.start()
sleep3.start()

sleep1.join()
sleep3.join()
sleep2.join()


def multiply():
    return [lambda x : i * x for i in range (3)]
for multiplier in multiply():
    print (multiplier (3), end=' ')
