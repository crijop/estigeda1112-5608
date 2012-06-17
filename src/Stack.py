#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Carlos Rijo Palma Nº 5608 
@data: 28/06/2012
Data da entrega 17 junho 2012
'''


#Class Stack
class Stack:
    def __init__(self, N):
        self.top = - 1
        self.S = [0 for k in range(N)]
        pass
    
    #Medoto stack_Empty
    #retorna verdadeiro ou falso, 
    #consonte a pilha estiver ou nao vazia
    def stack_Empty(self):
        if self.top == 0:
            return True
            pass
        else:
            return False
            pass
        pass
    
    #Metodo Push
    def Push(self, x):
        self.top += 1
        self.S[self.top] = x
        pass
    
    #Metodo Pop
    def Pop(self):
        if self.stack_Empty():
            return "underflow"
            pass
        else:
            self.top -= 1
            return self.S[self.top + 1]
            
            pass
        pass
    
    #Metodo _str_, retorna uma string com a Stack    
    def __str__(self):
        s = ""
        s += str(self.top + 1) + ": "
        for k in range(0, self.top + 1):
            s += '  ' + str(self.S[k])
        return s
        pass
    pass
