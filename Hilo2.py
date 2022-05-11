import threading
import time
import logging
from Operaciones import *
import pandas as pd
import numpy as np

Op = Operaciones()

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s](%(threadName)-s) %(message)s')

class Hilo2(threading.Thread):
    def __init__(self,name,Mat):
        threading.Thread.__init__(self,name=name, target=Hilo2.run)
        self.name = name
        self.Mat0 = Mat

    def run(self):
        self.calculo(self.Mat0)

    def calculo(self,M):
        self.Ma_VC=[]
        for i in range(len(M)):
            self.Mat1=Op.Vel_cartM1(M,i)
            self.Mat2=Op.Vel_cartM2(M,i)
            self.t=Op.tiempos(M)
            self.Mat3=np.dot(self.Mat2, self.Mat1)      
            self.Jac1 = Op.Jac1()
            self.Jac2 = Op.Jac2()
            self.Mat_tem = np.dot(self.Jac1,self.Mat3)
            self.Mat_res = np.dot(self.Jac2,self.Mat_tem)
            self.Ma_VC.append([])
            for J in range(3):
                self.Ma_VC[i].append(0)
            self.Ma_VC[i][0]=float(self.t[i])
            self.Ma_VC[i][1]=float(self.Mat_res[0])
            self.Ma_VC[i][2]=float(self.Mat_res[1])
            #self.Ma_VC = self.Ma_temp
        self.VAIz=Op.VRIz(self.Ma_VC)
        self.VADe=Op.VRDe(self.Ma_VC)







    

    