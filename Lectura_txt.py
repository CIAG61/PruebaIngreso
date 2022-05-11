
class Datos:  
    def __init__(self):                     #lectura de datos
           #from tkinter import Tk          # importar tkinter para busqueda de archivo
            #from tkinter.filedialog import askopenfilename
            #Tk().withdraw()                 # abre la ventana para buscar el archivo
            #filename = askopenfilename()    # se selecciona el nombre del archivo abierto
            #print(filename.title())
            return None
    
    def lectura_datos(self,filename):
        import pandas as pd
        self.MtIn = pd.read_csv(filename,sep=",")
        print(self.MtIn)

    def Vel_cartesiana(self,M):     #matriz velocidades cartesianas
        import numpy as np
        Ar=np.array(M)
        import math as mt
        for i in range(len(M)):
            Ar1 = [[mt.cos(np.radians(Ar[i][1])),mt.sin(np.radians(Ar[i][1]))],[-mt.sin(np.radians(Ar[i][1])),mt.cos(np.radians(Ar[i][1]))],[0,1]]
            Ar2 = [[Ar[i][2]],[Ar[i][3]]]
            Ar3 = Ar1
            print(Ar2)
        return None

    def Multiplicar_matrices(self,M1,M2):
        if len(M1[0])==len(M2):
            m3 = []
            for i in range(len(M1)):
                m3.append([])
                for j in range(len(M2[0])):
                    m3[i].append(0)
            
            for i in range(len(M1)):
                for j in range(len(M2[0])):
                    for k in range(len(M1[0])):
                        m3[i][j]+=M1[i][k]*M2[k][j]
                return m3
        else:
            return None



