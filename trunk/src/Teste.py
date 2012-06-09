#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ArvoreRedBlack import *
from NoRedBlack import *

class KdTree(ArvoreRedBlack):
    def __init__(self, tamanhoChave):
        super(KdTree, self).__init__()
        self.tamanhoChave = tamanhoChave
        self.listaNos = []
        self.nos = [ NoRedBlack(0, '', 1) for k in range(6)]
        #self.no = NoRedBlack(self.tamanhoChave, '', None)
        pass
     
    def insert_kdTree(self, z):
        super(KdTree, self).insert(z)
        pass
    
    def delelte_kdTree(self):
        pass
    
    def search_kdTree(self, x, k):
        super(KdTree, self).search(x, k)
        pass
    
    def procurarVizinhos_kdTree(self, x, k):
        super(KdTree, self).procurarVizinhos(x, k)
        pass
    
    def maximum_kdTree(self, x):
        pass
    
    def minimum_kdTree(self, x):
        pass
    
    def sucessor_kdTree(self, x):
        pass
    
    def inorder_walk_kdTree(self, x, lista):
        super(KdTree, self).inorder_walk(x, lista)
        pass
    
    '''    
    
    def kdTreeInsert(self, lKey, depth = 0 ):
        
        if not lKey:
            return None
        
        k = len(lKey[0].key)
        axis = depth % k
        print axis
        #lKey.key[0].sort(key = lambda point: point[axis])
        lKey.sort()
        
        median = len(lKey) // 2
        
        #no = No((0, 0), '')
        for k in range(6):
            self.nos[k].key = lKey[median]
            
            self.nos[k].left = self.kdTreeInsert(lKey[:median], depth + 1)
            self.nos[k].right = self.kdTreeInsert(lKey[median + 1:], depth + 1)
            break
        #self.listaNos.append(no)
        
        #self.listaNos.sort()
        self.nos.append(self.nos)
        return self.nos
        pass

    '''    
    
    

    
    def kdTreeInsert(self, lKey, depth = 0 ):
        
        if not lKey:
            return None
        
        k = len(lKey[0])
        axis = depth % k
        lKey.sort(key = lambda point: point[axis])
        median = len(lKey) // 2
    
        no = No(0, '')
        no.key = lKey[median]
        no.left = self.kdTreeInsert(lKey[:median], depth + 1)
        no.right = self.kdTreeInsert(lKey[median + 1:], depth + 1)
        self.listaNos.append(no)
        self.listaNos.sort()
    
        return no
        pass
    
    pass

def Main():
    
    NUMERO_NOS = 6
    nos = [None for k in range(NUMERO_NOS)]
    listaChaves = []
    
    nos[0] = NoRedBlack((2, 3), "Benfica", None)
    nos[1] = NoRedBlack((5, 4), "Sporting", None)
    nos[2] = NoRedBlack((9, 6), "Porto", None)
    nos[3] = NoRedBlack((4, 7), "Academica", None)
    nos[4] = NoRedBlack((8, 1), "Braga", None)
    nos[5] = NoRedBlack((7, 2), "Olhanense", None)

    '''
    nos[6] = NoRedBlack((1, 3), "Portimonense", None)
    nos[7] = NoRedBlack((10, 4), "Setubal", None)
    nos[8] = NoRedBlack((14, 6), "Nacional", None)
    nos[9] = NoRedBlack((15, 7), "Guimaraes", None)
    '''

    NR_CHAVES = len(nos[0].key)
    kd = KdTree(NR_CHAVES)
    
    for k in range(NUMERO_NOS):
        listaChaves.append(nos[k].key)
        
    kd.kdTreeInsert(listaChaves)
    
    for k in range(NUMERO_NOS):
        print kd.listaNos[k]
        
    
     
Main()



    
    