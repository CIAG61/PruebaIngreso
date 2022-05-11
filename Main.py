import threading
import time
import datetime
import logging
import numpy as np
import matplotlib.pyplot as plt

from Hilo1 import Hilo1
from Hilo2 import Hilo2

t1 = Hilo1("Hilo_1")
t1.start()
t1.join()
Data=t1.MtIn
t2 = Hilo2("Hilo_2",Data)
t2.start()
t2.join()
Mat_Out=t2.Ma_VC
print(Mat_Out)
np.savetxt("resultado.txt",Mat_Out,fmt='%.6f',delimiter=',')
plt.plot(t2.t,t2.VAIz,t2.VADe)
plt.xlabel('tiempo (t)')
plt.ylabel('Velocidad angular')
plt.show()
#Tiempo_total=datetime.datetime.now()