#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012

@author: Carlos Palma Nº 5608

Class Main
'''

from NoRedBlack import *
from ArvoreRedBlack import *
from Stack import *
from ArvoreBinariaLinkedList import *
import ArvoreBinariaLinkedList
import KdTree

#Metodo Main
if __name__ == '__main__':
    
    #lista de nos
    nos = [None for k in range(10)]
    
    #inicializaçao da lista de nós
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
        
    arv = ArvoreRedBlack()
    
    print "NIL"
    print arv.nil
    
    #inserir nós na arvoreRedBlack
    arv.insert(nos[0])
    arv.insert(nos[1])
    arv.insert(nos[2])
    arv.insert(nos[3])
    arv.insert(nos[4])
    arv.insert(nos[5])
    arv.insert(nos[6])
    arv.insert(nos[7])
    arv.insert(nos[8])
    arv.insert(nos[9])
    
    #imprimir a arvoreRedBlack, ja ordenada
    print
    print "INORDER"
    lista = []
    arv.inorder_walk(arv.root, lista)
    for x in lista:
        print x
    
    #eleminar nó a arvore RedBlack
    print
    print "Del"
    arv.RB_Delete(nos[0])
    
    #voltar a imprimir a arvore ja com o 
    #nó eliminado
    print "INORDER"
    lista = []
    arv.inorder_walk(arv.root, lista)
    for x in lista:
        print x
    
    #Fazer a pesquisa do nó
    print "PESQUISA"
    print arv.search(arv.root, 5)
    pass
    
    #procurar vizinhos do nó
    print "PESQUISA_Vizinhos "
    print arv.procurarVizinhos(arv.root, 5)
    pass
    
    
    '''
    Class kd tree
    '''
    print '\nConstruçao da arvore apartir da lista de dados'
    KdTree.Main()
    
    
    '''
    Testes Estudo Experimental
    '''
    
    
    
    
    
    