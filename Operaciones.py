import numpy as np
import math as mt


class Operaciones():
    
    def __init__(self):
        pass
    #Atributos
    AlpIz = mt.pi/2
    AlpDe = -mt.pi/2
    BetIz = mt.pi
    BetDe = 0
    l = 0.08
    rIz = 0.035
    rDe = 0.035
    #metodos
    def Multiplicar_matrices(self,M1,M2):
        if len(M1[0])==len(M2):
            M3 = []
            for i in range(len(M1)):
                M3.append([])
                for j in range(len(M2[0])):
                    M3[i].append(0)
            
            for i in range(len(M1)):
                for j in range(len(M2[0])):
                    for k in range(len(M1[0])):
                        M3[i][j]+=M1[i][k]*M2[k][j]
            return M3
        else:
            return None

    
    def Vel_cartM1(self,M,i):     #matriz velocidades cartesianas
        Ar=np.array(M)
        Ar1 = [[mt.cos(np.radians(Ar[i][1])),mt.sin(np.radians(Ar[i][1]))],[-mt.sin(np.radians(Ar[i][1])),mt.cos(np.radians(Ar[i][1]))],[0,1]]
        Ar2 = [[Ar[i][2]/1000],[Ar[i][3]]]
        Ar3 = np.dot(Ar1,Ar2)
        return Ar3
    
    def Vel_cartM2(self,M,i):
        Ar=np.array(M)
        Ar4 = [[mt.cos(np.radians(Ar[i][1])),-mt.sin(np.radians(Ar[i][1])),0],[-mt.sin(np.radians(Ar[i][1])),mt.cos(np.radians(Ar[i][1])),0],[0,0,1]]
        return Ar4

    def Jac1(self):
        J1 = [[mt.sin(self.AlpIz+self.BetIz),-mt.cos(self.AlpIz+self.BetIz),-self.l*mt.cos(self.BetIz)],[mt.sin(self.AlpDe+self.BetDe),-mt.cos(self.AlpDe+self.BetDe),-self.l*mt.cos(self.BetDe)]]
        return J1

    def Jac2(self):
        J2 = [[1/self.rIz,0],[0,1/self.rDe]]
        return J2

    def tiempos(self,M0):
        Ar=[]
        MN=np.array(M0)
        for i in range(len(MN)):
            Ar.append(MN[i][0])
        return Ar
    
    def VRIz(self,M0):
        MN=np.array(M0)
        Ar=[]
        for i in range(len(MN)):
            Ar.append(MN[i][1])
        return Ar
    
    def VRDe(self,M0):
        MN=np.array(M0)
        Ar=[]
        for i in range(len(MN)):
            Ar.append(MN[i][2])
        return Ar

    #def graficar(self,Ar1,Ar2):
        #plt.plot(Ar1,Ar2)
