#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012
@author: Carlos Palma Nº 5608
Data da entrega 17 junho 2012
class No
'''

#Ĉlass No
class No(object):
    def __init__(self, key, valor):
        self.key = key
        self.valor = valor

        self.parent = None
        self.left   = None
        self.right  = None
        pass
    
    #Metodo __str__ para imprimir um No
    #retorna uma string com o No
    def __str__(self):
        s = str(self.key) + ' : ' + str(self.valor)
        s += '('
        if self.parent == None:
            s += 'None'  + ', ' 
        else:
            s += str(self.parent.key) + ', ' 

        if self.left == None:
            s += 'None'  + ', ' 
        else:
            s += str(self.left.key) + ', ' 

        if self.right == None:
            s += 'None' + ')' 
        else:
            s += str(self.right.key) + ')' 
        return s
    
    #Metodo de __cmp__, para utilizar no sort, 
    #fazendo a ordenaçao pela chave
    def __cmp__(self, x):
        if self.key > x :
            return 1
            pass
        elif self.key ==  x:
            return 0
            pass
        else:
            return -1
            pass
        pass
    pass
#fim da class No