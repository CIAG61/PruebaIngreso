import threading
import time
import logging
from tkinter import Tk          # importar tkinter para busqueda de archivo
from tkinter.filedialog import askopenfilename
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s](%(threadName)-s) %(message)s')

class Hilo1(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name, target=Hilo1.run)
        self.name = name
    
    def run(self):
        self.consultar()

    def consultar(self):
        return None
    def consultar(self):
        Tk().withdraw()                 # abre la ventana para buscar el archivo
        filename = askopenfilename(
                title='Abrir archivo',
                filetypes=(
                ('text files', '*.txt'),
                ('All files', '*.*')
            ))
            # se selecciona el nombre del archivo abierto
        self.MtIn = pd.read_csv(filename,sep=",")
        #print(self.MtIn)

