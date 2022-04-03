# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:47:59 2022

@author: Andres Venialgo
"""

from constantes import * 
from main import *

class Barrio:
    
    def __init__(self):
        self.civiles = [Civil() for i in range(CIVILES_INICIALES)]
        self.policias = [Policia() for i in range(POLICIAS_INICIALES)]
        self.criminales = [Criminal() for i in range(CRIMINALES_INICIALES)]
        self.gameover = False
        
    def vivir(self):
        if self.gameover:
            return
        
        for civil in self.civiles:
            civil.mover()
        for criminal in self.criminales:
            criminal.mover(self.civiles)
        for policia in self.policias:
            policia.mover(self.criminales)
        
        if self.civiles == []:
            print("GAME OVER: criminales ganan")
            self.gameover = True
            
        if self.criminales == []:
            print("GAME OVER: policias ganan")
            self.gameover = True
            
            