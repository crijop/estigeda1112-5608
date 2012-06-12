#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Stack import *
from NoRedBlack import *


#Class ArvoreBinaria
#cria a arvore, com um numero (N) de elementos 
#que a arvore podera conter
class ArvoreBinaria(object):
    def __init__(self, N):
        self.apontador_memoria = Stack(N)
        for k in range(0, N):
            self.apontador_memoria.Push(k)
            pass
        self.N = N
        self.nos = [ NoRedBlack(0, '', 1) for k in range(N)]
        self.NIL = None
        self.root = None
        pass

    #Metodo malloc, 
    #aloca a memoria   
    def malloc(self):
        x = self.apontador_memoria.Pop()
        return x
    
    #metodo free, 
    #liberta a memoria
    def free(self,x):
        self.apontador_memoria.Push(x)
        pass

    #metodo tree_sucessor
    def tree_sucessor(self, x):
        if self.nos[x].right != self.NIL:
            return self.tree_minimum(self.nos[x].right)
        y = self.nos[x].parent
        while y != self.NIL and x == self.nos[y].right:
            x = y
            y = self.nos[y].parent
            pass
        return y
    
    #metodo search
    def search(self, k):
        x = self.nos[k].parent
        while x != None and self.nos[x].key != k:
            x = self.nos[x].right
        return x
        pass

    #metodo tree_minimum
    def tree_minimum(self,x):
        while self.nos[x].left != self.NIL:
            x = self.nos[x].left
            pass
        return x
    
    #metodo tree_delete
    def tree_delete(self, z):
        if self.nos[z].left == self.NIL or self.nos[z].right == self.NIL:
            y = z
        else:
            y = self.tree_sucessor(z)
            pass
        if self.nos[y].left != self.NIL:
            x = self.nos[y].left
        else:
            x = self.nos[y].right
            pass
        if x != self.NIL:
            self.nos[x].parent = self.nos[y].parent
            pass
        if self.nos[y].parent == self.NIL:
            self.root = x
        elif y == self.nos[self.nos[y].parent].left:
            self.nos[self.nos[y].parent].left = x
        else:
            self.nos[self.nos[y].parent].right = x
            pass
        if y != z:
            self.nos[z].key = self.nos[y].key
            pass
        return y
    
    #Metodo tree_insert
    #inserir nó na arvore binaria
    def tree_insert(self, z):
        y = self.NIL
        x = self.root
        while( x != self.NIL ):
            y = x
            if self.nos[z].key < self.nos[x].key:
                x = self.nos[x].left
            else:
                x = self.nos[x].right
                pass
            pass
        self.nos[z].parent = y
        if y == self.NIL:
            self.root = z
        elif self.nos[z].key < self.nos[y].key:
            self.nos[y].left = z
        else:
            self.nos[y].right = z
            pass
        pass
    
    #Metodo _str_, retorna uma string com a Arvore binaria
    def __str__(self):
        t = 'Arvore Binaria'
        t += '\n'
        for k in xrange(self.N):
            t += str(k) + ':' +" key: " + str(self.nos[k].key) + " p: " +\
                 str(self.nos[k].parent) + " valor: " +\
                 str(self.nos[k].valor) + " left: " +\
                 str(self.nos[k].left) + " right: " + \
                 str(self.nos[k].right) + '\n'
        return t
        pass
    pass

#Metodo Main
def Main():
    #Numero de elementos da arvore + 1 
    N = 11
    
    #lista de nós
    nos = [None for k in range(10)]
    nos[0] = NoRedBlack(7, "Benfica", None)
    nos[1] = NoRedBlack(2, "Sporting", None)
    nos[2] = NoRedBlack(11, "Porto", None)
    nos[3] = NoRedBlack(1, "Academica", None)
    nos[4] = NoRedBlack(5, "Braga", None)
    nos[5] = NoRedBlack(8, "Olhanense", None)
    nos[6] = NoRedBlack(14, "Portimonense", None)
    nos[7] = NoRedBlack(4, "Setubal", None)
    nos[8] = NoRedBlack(6, "Nacional", None)
    nos[9] = NoRedBlack(15, "Guimaraes", None)
    
    arvore = ArvoreBinaria(N)
    
    for i in range(10):
        x = arvore.malloc()
        arvore.nos[x] = nos[i]
        arvore.tree_insert(x)
        pass
    
    
    # outra forma de inserir os nós
    '''
    x = arvore.malloc()
    arvore.nos[x] = nos[0]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x]= nos[1]
    arvore.tree_insert(x)
    
    a = arvore.malloc()
    arvore.nos[a] = nos[2] 
    arvore.tree_insert(a)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[3]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[4]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[5]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[6]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[7]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[8]
    arvore.tree_insert(x)
    
    x = arvore.malloc()
    arvore.nos[x] = nos[9]
    arvore.tree_insert(x)
    '''
    
    print arvore
    
    
    #outra forma para imprimir a arvore
    '''
    for k in range(11):
        print '{0} : key: {1} -> {2} parent: {3} left: {4} right: {5}'.format(str(k), 
                                                                str(arvore.nos[k].key),
                                                                str(arvore.nos[k].valor),
                                                                str(arvore.nos[k].parent), 
                                                                str(arvore.nos[k].left), 
                                                                str(arvore.nos[k].right))
    '''
    '''
    print "Eliminar nó"
    
    # valor da posição da lista de nós
    # que pretendemos eleminar
    noFree = 8
    x = arvore.tree_delete(noFree)
    arvore.free(x)
    print arvore
    pass

    #Fim Main
    '''

#Main()


