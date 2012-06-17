#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012

@author: Carlos Palma Nº 5608
Data da entrega 17 junho 2012
Class ArvoreRedBlack
'''
from ArvorePesquisaBinaria import *

#class ArvoreRedBlack
class ArvoreRedBlack(ArvorePesquisaBinaria):
    def __init__(self):
        super(ArvoreRedBlack, self).__init__()
        pass
    #Metodo left_Rotate, faz a rotaçao a esquerda
    #da arvore, consoante o no que recebe
    def left_Rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
            pass
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
            pass
        elif x == x.parent.left:
            x.parent.left = y
            pass
        else:
            x.parent.right = y
            pass
        y.left = x
        x.parent = y
        pass
    
    #Metodo right_Rotate, faz a rotaçao a direita
    #da arvore, consoante o no que recebe
    def right_Rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
            pass
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
            pass
        elif x == x.parent.right:
            x.parent.right = y
            pass
        else:
            x.parent.left = y
            pass
        y.right = x
        x.parent = y
        pass
    
    #Metodo rb_insert_fixup
    def rb_insert_fixup(self, z):
        while z.parent.cor == self.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.cor == self.RED:
                    z.parent.cor = self.BLACK
                    y.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    z = z.parent.parent
                    pass
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_Rotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.right_Rotate(z.parent.parent)
                pass
            else:
                y = z.parent.parent.left
                if y.cor == self.RED:
                    z.parent.cor = self.BLACK
                    y.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_Rotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.left_Rotate(z.parent.parent)
                pass
            pass
        self.root.cor = self.BLACK
        pass
    
    #Metodo insert
    #Inser os nos na arvore Red Black
    #recebe como parametro o no a 
    #inserir, de referir que faz o insert
    #consoante as cores red e black utilizando 
    #para isso o metodo rb_insert_fixup
    def insert(self, z):
        super(ArvoreRedBlack, self).insert(z)
        z.cor = self.RED
        self.rb_insert_fixup(z)
        pass
    
    #Medoto RB_transplant, 
    #faz a reconstruçao da arvore
    #apos ser eleminado um nó
    #da arvore, recebe dois nós
    def RB_Transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
            pass
        elif u == u.parent.left:
            u.parent.left = v
            pass
        else: 
            u.parent.right = v
            pass
        v.parent = u.parent
        pass
    
    #Metodo RB_Delete_fixup
    def RB_Delete_fixup(self, x):
        while x != self.root and x.cor == self.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.cor == self.RED:
                    w.cor = self.BLACK
                    x.parent.cor = self.RED
                    self.left_Rotate(x.parent)
                    w = x.parent.right
                    pass
                if w.left.cor == self.BLACK and w.right.cor == self.BLACK:
                    w.cor = self.RED
                    x = x.parent
                    pass
                else:
                    if w.right.cor == self.BLACK:
                        w.left.cor = self.BLACK
                        w.cor = self.RED
                        self.right_Rotate(w)
                        w = x.parent.right
                        pass
                    w.cor = x.parent.cor
                    x.parent.cor = self.BLACK
                    w.right.color = self.BLACK
                    self.left_Rotate(x.parent)
                    x = self.root
                    pass
            else:
                w = x.parent.left
                if w.cor == self.RED:
                    w.cor = self.BLACK
                    x.parent.cor = self.RED
                    self.right_Rotate(x.parent)
                    w = x.parent.left
                    pass
                if w.left.cor == self.BLACK and w.right.cor == self.BLACK:
                    w.cor = self.RED
                    x = x.parent
                    pass
                else:
                    if w.left.cor == self.BLACK:
                        w.right.cor = self.BLACK
                        w.cor = self.RED
                        self.left_Rotate(w)
                        w = x.parent.left
                        pass
                    w.cor = x.parent.cor
                    x.parent.cor = self.BLACK
                    w.left.cor = self.BLACK
                    self.right_Rotate(x.parent)
                    x = self.root
                    pass
                pass
            x.cor = self.BLACK
            pass
        
    #Metodo RB_Delete
    #Elimina os nos na arvore Red Black
    #recebe como parametro o no a 
    #eliminar, de referir que faz o delete
    #consoante as cores red e black utilizando 
    #para isso o metodo RB_Delete_fixup    
    def RB_Delete(self, z):
        y = z
        ##
        yColor = y.cor
        if z.left == self.nil:
            x = z.right
            self.RB_Transplant(z, z.right)
            pass
        elif z.right == self.nil:
            x = z.left
            self.RB_Transplant(z, z.left)
            pass
        else:
            y = self.minimum(z.right)
            yColor = y.cor
            x = y.right
            if y.parent == z:
                x.parent = y
                pass
            else:
                self.RB_Transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                pass
            self.RB_Transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.cor
            pass
        if yColor == self.BLACK:
            self.RB_Delete_fixup(x)
            pass
        pass
    
    pass
#fim da class