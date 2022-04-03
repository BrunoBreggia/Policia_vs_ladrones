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


def actualizar(data):
    mat.set_data(data)
    return mat

def data_gen():
    barrio = Barrio()
    fils, cols = FILAS_BARRIO, COLUMNAS_BARRIO
    matriz = np.zeros( (fils, cols, 3), np.float32 )
    while True:
        matriz *= 0
        # Lo civiles se mostraran en blanco
        for civil in barrio.civiles:
            fil, col = civil.posicion
            matriz[fil, col, :] = [1,1,1]
        # Los policias se veran en azul
        for pol in barrio.policias:
            fil, col = pol.posicion
            matriz[fil, col, :] = [0.3, 0.3, 1]
        # Los criminales se veran en rojo
        for criminal in barrio.criminales:
            fil, col = criminal.posicion
            matriz[fil, col, :] = [1,0,0]
        # # avanzo epoca
        barrio.vivir()
        # mundo.escribir_archivo("mini_evolucion.txt")
        # entrego matriz actual
        yield matriz

fig, ax = plt.subplots()
mat = ax.matshow(np.zeros((FILAS_BARRIO, COLUMNAS_BARRIO, 3), np.float32))
ani = animation.FuncAnimation(fig, actualizar, data_gen, interval=50,
                              save_count=50)
plt.show()

