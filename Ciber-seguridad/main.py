# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:00:22 2022

"""

from abc import ABC, abstractmethod
import numpy as np
from constantes import * 


class Persona(ABC):
    
    def __init__(self):
        self.campo_de_vision = 50
        self.energia = 0
        # self.posicion = [49, 49]
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
 
    def mover_aleatorio(self):
        posicion_valida = False
        while not posicion_valida:
            indice = np.random.randint(0,8)
            pos_rel = self.posiciones_relativas[indice]
            pf = self.posicion[0] + pos_rel[0]
            pc = self.posicion[1] + pos_rel[1]
            if (0 <= pf < FILAS_BARRIO) and (0 <= pc < COLUMNAS_BARRIO):
               posicion_valida = True
               self.posicion = [ self.posicion[0]+pos_rel[0],
                             self.posicion[1]+pos_rel[1] ]
               
    
    def matar(self, p_civiles):
        for indice, civil in enumerate(p_civiles):
            if civil.posicion == self.posicion:
                p_civiles.pop(indice)
                print(f"¡{type(civil).__name__} asesinado!")
                break
        
    def buscar(self,p_civiles):
        respuesta = None
        pos_x = self.posicion[0]
        pos_y = self.posicion[1]
        civil_mas_cercano_x = np.inf
        civil_mas_cercano_y = np.inf
        for civil in p_civiles:
            pf = civil.posicion[0]
            pc = civil.posicion[1]
            dx = self.posicion[0] - pf
            dy = self.posicion[1] - pc
            
            if self.campo_de_vision >= abs(dx) and self.campo_de_vision >= abs(dy):
                
                if abs(dx) < abs(civil_mas_cercano_x) and abs(dy) < abs(civil_mas_cercano_y):
                    if abs(dx) > abs(dy):
                        # print ("dx es mayor a dy")
                        pos_x = self.posicion[0] - int(dx/abs(dx))
                        pos_y = self.posicion[1]

                    elif abs(dx) < abs(dy):
                        # print ("dy es mayor a dx")
                        pos_x = self.posicion[0]
                        pos_y = self.posicion[1] - int(dy/abs(dy))
                    elif abs(dx)==abs(dy) and dx == 0 :
                        continue
                    else:
                        # print ("dx==dy")
                        pos_x = self.posicion[0] - int (dx/abs(dx))
                        pos_y = self.posicion[1] - int (dy/abs(dy))
                        
                    civil_mas_cercano_x = dx
                    civil_mas_cercano_y = dy
                    # if pos_x==FILAS_BARRIO or pos_y== COLUMNAS_BARRIO:
                    #     print("ffffffffff")
                    respuesta = [pos_x,pos_y]
                
        return respuesta
    
    # def mover(self, pos_x, pos_y):
    #     self.posicion=[pos_x,pos_y]

class Civil(Persona):
    
    def __init__(self):
        super().__init__()
        self.posicion = [np.random.randint(0,FILAS_BARRIO),
                          np.random.randint(0,COLUMNAS_BARRIO)]
    
    def mover(self):
        self.mover_aleatorio()

            
class Policia(Persona):
    def __init__(self):
        super().__init__()
        self.posicion = [np.random.randint(0,FILAS_BARRIO),
                         np.random.randint(0,COLUMNAS_BARRIO)]        
        
    # def buscar(self):
    #     pass

    def mover(self, p_civiles):
        busqueda = self.buscar(p_civiles)
        if busqueda == None:
            self.mover_aleatorio()
        #     print ("mover aleatorio")
        else:
            self.posicion = busqueda
            
        self.matar(p_civiles)
        

class Criminal(Persona):
    def __init__(self):
        super().__init__()
        self.posicion = [np.random.randint(0,FILAS_BARRIO),
                          np.random.randint(0,COLUMNAS_BARRIO)]
        
    def mover(self, p_civiles):
        busqueda = self.buscar(p_civiles)
        if busqueda == None:
            self.mover_aleatorio()
        #     print ("mover aleatorio")
        else:
            self.posicion = busqueda
            
        self.matar(p_civiles)
        
    # def matar(self, p_civiles):
    #     for indice, civil in enumerate(p_civiles):
    #         if civil.posicion == self.posicion:
    #             p_civiles.pop(indice)
    #             print("[!] Civil asesinado")
    #             break
        
    # def buscar(self,p_civiles):
    #     respuesta = None
    #     pos_x = self.posicion[0]
    #     pos_y = self.posicion[1]
    #     civil_mas_cercano_x = np.inf
    #     civil_mas_cercano_y = np.inf
    #     for civil in p_civiles:
    #         pf = civil.posicion[0]
    #         pc = civil.posicion[1]
    #         dx = self.posicion[0] - pf
    #         dy = self.posicion[1] - pc
            
    #         if self.campo_de_vision >= abs(dx) and self.campo_de_vision >= abs(dy):
                
    #             if abs(dx) < abs(civil_mas_cercano_x) and abs(dy) < abs(civil_mas_cercano_y):
    #                 if abs(dx) > abs(dy):
    #                     # print ("dx es mayor a dy")
    #                     pos_x = self.posicion[0] - int(dx/abs(dx))
    #                     pos_y = self.posicion[1]

    #                 elif abs(dx) < abs(dy):
    #                     # print ("dy es mayor a dx")
    #                     pos_x = self.posicion[0]
    #                     pos_y = self.posicion[1] - int(dy/abs(dy))
    #                 elif abs(dx)==abs(dy) and dx == 0 :
    #                     continue
    #                 else:
    #                     # print ("dx==dy")
    #                     pos_x = self.posicion[0] - int (dx/abs(dx))
    #                     pos_y = self.posicion[1] - int (dy/abs(dy))
                        
    #                 civil_mas_cercano_x = dx
    #                 civil_mas_cercano_y = dy
    #                 # if pos_x==FILAS_BARRIO or pos_y== COLUMNAS_BARRIO:
    #                 #     print("ffffffffff")
    #                 respuesta = [pos_x,pos_y]
                
    #     return respuesta
                    
                   
            
            
            
        
        

