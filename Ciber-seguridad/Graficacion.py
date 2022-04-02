# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:59:01 2022

@author: Windows
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from Barrio import Barrio
from constantes import *

def data_gen():
    barrio = Barrio()
    fils, cols = FILAS_BARRIO, COLUMNAS_BARRIO
    matriz = np.zeros( (fils, cols, 3), np.float32 )
    while True:
        matriz *= 0
        # Lo civiles se mostraran en blanco
        for civil in barrio.civiles:
            fil, col = civil.posicion
            matriz[fil, col, :] = [0,0,1]
        # Los mos se veran en tonalidades de rojo
        for mo in mundo.mos:
            if not mo.esta_muerto:
                fil, col = mo.posicion
                color = mo.energia/ENERGIA_MAX_MO
                matriz[fil, col, :] = [color, 0, 0]
        # avanzo epoca
        mundo.vivir()
        # mundo.escribir_archivo("mini_evolucion.txt")
        # entrego matriz actual
        yield matriz

fig, ax = plt.subplots()
mat = ax.matshow(np.zeros((TAM_MUNDO, TAM_MUNDO, 3), np.float32))
ani = animation.FuncAnimation(fig, actualizar, data_gen, interval=10,
                              save_count=50)
plt.show()

