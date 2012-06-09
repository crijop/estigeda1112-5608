#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012

@author: Carlos Palma Nº 5608


'''
from NoRedBlack import *

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

    def search(self, x, k):
        if x == self.nil or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
        pass
    
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
    
    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
        pass

    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x
        pass

    def sucessor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y
        pass

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

    def inorder_walk(self, x, lista):
        if x != self.nil:
            self.inorder_walk(x.left, lista)
            lista.append( x )
            self.inorder_walk(x.right, lista)
            pass
        pass
    
    pass