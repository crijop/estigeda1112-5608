#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ArvoreRedBlack import *
from NoRedBlack import *

#class KdTree
class KdTree(ArvorePesquisaBinaria):
    def __init__(self, tamanhoChave):
        super(KdTree, self).__init__()
        self.tamanhoChave = tamanhoChave
        self.listaNos = []
        self.nos = [ No(0, '') for k in range(6)]
        #self.no = NoRedBlack(self.tamanhoChave, '', None)
        pass
    
    #Metodo insert
    #Inser os nos na arvore binaria
    #recebe como parametro o no a 
    #inserir
    #de referir que este metodo foi criado 
    #apartir do metodo que ja existia na class
    #ArvorePesquisaBinaria 
    def insert_kdTree(self, z):
        super(KdTree, self).insert(z)
        pass
    
    #Metodo delete, elemina nó da
    #arvore, recebe o nó a ser
    #eleminado na arvore
    #de referir que este metodo foi criado 
    #apartir do metodo que ja existia na class
    #ArvorePesquisaBinaria
    def delete_kdTree(self, z):
        super(KdTree, self).delete(z)
        pass
    
    #Metodo search, procura um nó, que
    #recebe como parametro, neste caso k
    #e ainda recebe x, que vai ser onde
    #vai começar a pesquisa
    #de referir que este metodo foi criado 
    #apartir do metodo que ja existia na class
    #ArvorePesquisaBinaria
    def search_kdTree(self, x, k):
        super(KdTree, self).search(x, k)
        pass
    
    #Metodo procuraVizinhos, recebe 
    #como parametro o no que se quer
    #procurar os vizinhos (k) e ainda 
    #recebe x, que vais ser onde 
    #vai começar a pesquisa
    #de referir que este metodo foi criado 
    #apartir do metodo que ja existia na class
    #ArvorePesquisaBinaria
    def procurarVizinhos_kdTree(self, x, k):
        super(KdTree, self).procurarVizinhos(x, k)
        pass
    
    #Metodo inorder_Walk, faz com que a arvore 
    #seja ordenada numa lista para ser imprimida
    #Recebe o no apartir do qual se quer começar 
    # a ordenar e a lista, onde vai ser a arvore 
    #ordenada, de referir que este metodo foi criado 
    #apartir do metodo que ja existia na class
    #ArvorePesquisaBinaria
    def inorder_walk_kdTree(self, x, lista):
        super(KdTree, self).inorder_walk(x, lista)
        pass
    
    #criaçao da arvore kd apartir de uma
    #lista de dados,
    #recebe como parametro a lista e a profundidade
    #em que a arvore vai iniciar a sua criaçao
    def KdArvore(self, lKey, depth = 0 ):
        
        if not lKey:
            return None
        
        k = len(lKey[0])
        axis = depth % k
        
        lKey.sort(key = lambda point: point[axis])
        median = len(lKey) // 2
        no = No(0, '')
        no.key = lKey[median]
        no.left = self.KdArvore(lKey[:median], depth + 1)
        no.right = self.KdArvore(lKey[median + 1:], depth + 1)
        self.listaNos.append(no)
        self.listaNos.sort()
    
        return no
        pass
    
    pass

#Metodo Main
def Main():
    
    NUMERO_NOS = 6
    nos = [None for k in range(NUMERO_NOS)]
    #lista de chaves retiradas dos nos
    listaChaves = []
    
    nos[0] = No((2, 3), "Benfica")
    nos[1] = No((5, 4), "Sporting")
    nos[2] = No((9, 6), "Porto")
    nos[3] = No((4, 7), "Academica")
    nos[4] = No((8, 1), "Braga")
    nos[5] = No((7, 2), "Olhanense")
    
    NR_CHAVES = len(nos[0].key)
    kd = KdTree(NR_CHAVES)

    #retirar chaves dos nos e meter na lista de chaves
    for k in range(NUMERO_NOS):
        listaChaves.append(nos[k].key)
    #fazer a arvore kd apartir da lista de chaves
    kd.KdArvore(listaChaves)
    
    #imprimir a lista de Nos que contem a arvore kd 
    #ja com a ordenaçao correcta   
    for k in range(NUMERO_NOS):
        print kd.listaNos[k]
    
    
    
#Main()