'''
Created on 7 de Jun de 2012

@author: admin1
'''

from ArvoreRedBlack import *
from NoRedBlack import *

class KdTree(ArvoreRedBlack):
    def __init__(self, tamanhoChave):
        super(KdTree, self).__init__()
        self.tamanhoChave = tamanhoChave
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
    
    pass

def Main():
    
    kd = KdTree(2)
    nos = [None for k in range(10)]
    
    
    nos[0] = NoRedBlack(11, "Renoir", None)
    nos[1] = NoRedBlack(2, "van Gogh", None)
    nos[2] = NoRedBlack(14, "Picasso", None)
    nos[3] = NoRedBlack(1, "Manet", None)
    nos[4] = NoRedBlack(7, "da Vinci", None)
    nos[5] = NoRedBlack(15, "Miguel Angelo", None)
    nos[6] = NoRedBlack(5, "Rafael", None)
    nos[7] = NoRedBlack(8, "Goya", None)
    nos[8] = NoRedBlack(4, "Turner", None)
    nos[9] = NoRedBlack(6, "Tuqqwrner", None)
    
        
    
    
    print "NIL"
    print kd.nil
    
    kd.insert(nos[0])
    kd.insert(nos[1])
    kd.insert(nos[2])
    kd.insert(nos[3])
    kd.insert(nos[4])
    kd.insert(nos[5])
    kd.insert(nos[6])
    kd.insert(nos[7])
    kd.insert(nos[8])
    kd.insert(nos[9])
    
    
    print
    print "INORDER"
    lista = []
    kd.inorder_walk_kdTree(kd.root, lista)
    for x in lista:
        print x
    pass

Main()