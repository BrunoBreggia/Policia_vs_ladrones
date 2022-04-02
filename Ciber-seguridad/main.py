# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:00:22 2022

"""

from abc import ABC, abstractmethod
import numpy as np

class Persona(ABC):
    
    def __init__(self):
        self.campo_de_vision = 0
        self.energia = 0
        self.posicion = [0, 0]
    
    def set_posicion(self, nueva_pos):
        self.posicion = nueva_pos
    
    @abstractmethod
    def mover(self):
        pass


class Civil(Persona):
    
    def __init__(self):
        super().__init__()
        
    def mover(self):
        
    

class Policia:
    pass

class Criminal:
    pass


