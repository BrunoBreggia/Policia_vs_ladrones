# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:00:22 2022

"""

from abc import ABC, abstractmethod
import numpy as np
from constantes import * 


class Persona(ABC):
    
    def __init__(self):
        self.campo_de_vision = 0
        self.energia = 0
        self.posicion = [0, 0]
        self.posiciones_relativas = {
            0:[-1,0], 
            1:[-1,1],
            2:[0,1],
            3:[1,1],
            4:[1,0],
            5:[1,-1],
            6:[0,-1],
            7:[-1,-1]
            }
    
    def set_posicion(self, nueva_pos):
        self.posicion = nueva_pos
    
    @abstractmethod
    def mover(self):
        pass


class Civil(Persona):
    
    def __init__(self):
        super().__init__()
        
    def mover(self):
        posicion_valida = False
        while not posicion_valida:
            indice = np.random(0,8)
            pos_rel = self.posiciones_relativas[indice]
            pf = self.posicion[0]+ pos_rel
            pc = self.posicion[1]+ pos_rel
            if (0 <= pf < FILAS_BARRIO) and (0 <= pc < COLUMNAS_BARRIO):
               posicion_valida = True
               self.posicion = [ self.posicion[0]+pos_rel[0],
                             self.posicion[1]+pos_rel[1] ]
             
            
class Policia(Persona):
    pass

class Criminal(Persona):
    pass


