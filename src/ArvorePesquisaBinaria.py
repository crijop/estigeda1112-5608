#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012
@author: Carlos Palma Nº 5608
'''
from NoRedBlack import *

#class ArvorePesquisaBinaria
class ArvorePesquisaBinaria(object):
    def __init__(self):
        self.BLACK = 0
        self.RED = 1
        self.nil = NoRedBlack(0, "", self.BLACK)
        self.parent = self.nil
        self.left = self.nil
        self.right = self.nil
        self.root = self.nil
        pass

    #Metodo insert
    #Inser os nos na arvore binaria
    #recebe como parametro o no a 
    #inserir
    def insert(self, z):
        z.parent = self.nil
        z.left = self.nil
        z.right = self.nil
        
        y = self.nil
        x = self.root
        
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        pass

    #Metodo search, procura um nó, que
    #recebe como parametro, neste caso k
    #e ainda recebe x, que vai ser onde
    #vai começar a pesquisa
    def search(self, x, k):
        if x == self.nil or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
        pass
    
    #Metodo procuraVizinhos, recebe 
    #como parametro o no que se quer
    #procurar os vizinhos (k) e ainda 
    #recebe x, que vais ser onde 
    #vai começar a pesquisa
    def procurarVizinhos(self, x, k):
        if x == self.nil or k == x.key:
            if x.left != self.nil:
                return x.left
            elif x.right != self.nil:
                return x.right
            else:
                return x.parent
        if k < x.key:
            return self.procurarVizinhos(x.left, k)
        else:
            return self.procurarVizinhos(x.right, k)
        pass
    
    #Metodo minimum, devolve 
    #o no minimo da arvore,
    #ou seja o no que fica mais a
    #esquerda na arvore
    #recebe o no, onde se vai começar
    #a pesquisar
    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
        pass

    #Metodo maximum, devolve
    #o no maxido da arvore,
    #ou seja, o no que fica mais 
    #direita na arvore
    #recebe o nó, onde se vai começar
    #a pesquisar
    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x
        pass

    #Metodo sucessor, vai devolver 
    #o sucessor do nó, que recebe 
    #como parametro
    def sucessor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y
        pass

    #Medoto transplant, 
    #faz a reconstruçao da arvore
    #apos ser eleminado um nó
    #da arvore, recebe dois nós
    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
        pass

    #Metodo delete, elemina nó da
    #arvore, recebe o nó a ser
    #eleminado na arvore
    def delete(self, z):
        if z.left == self.nil:
            self.transplant(z, z.right)
        elif z.right == self.nil:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
        pass
    
    #Metodo inorder_Walk, faz com que a arvore 
    #seja ordenada numa lista para ser imprimida
    #Recebe o no apartir do qual se quer começar 
    # a ordenar e a lista, onde vai ser a arvore 
    #ordenada
    def inorder_walk(self, x, lista):
        if x != self.nil:
            self.inorder_walk(x.left, lista)
            lista.append( x )
            self.inorder_walk(x.right, lista)
            pass
        pass
    
    pass
    #fim da class