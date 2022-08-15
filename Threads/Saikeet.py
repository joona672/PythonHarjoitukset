import threading
import time

aloitus = time.time()

def tee_jutut(viive):
    print("Homma alkaa")
    print("Torku", viive,"sekuntia")
    time.sleep(viive)
    print("Torkut ohi")
    
    
viive = 2

# tee_jutut()
# tee_jutut()

t1 = threading.Thread(target=tee_jutut, args=[3])
t2 = threading.Thread(target=tee_jutut, args=[3])
t1.start()
t2.start()
t1.join()
t2.join()

lopetus = time.time()

print(f'Suorittaminen kesti {round(lopetus-aloitus,2)} sekuntia')
