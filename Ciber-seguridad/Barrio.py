# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:47:59 2022

@author: Andres Venialgo
"""
from constantes import * 
class Barrio:
    
    def __init__(self):
        self.civiles = [Civil() for i in range(CIVILES_INICIALES)]
        self.policias = [Policia() for i in range(POLICIAS_INICIALES)]
        self.criminales = [Criminales() for i in range(CRIMINASLES_INICIALES)]
        
