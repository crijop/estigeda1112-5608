#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ArvoreRedBlack import *
from NoRedBlack import *
from Stack import *
from No import *

#class KdTree
class KdTree(ArvorePesquisaBinaria):
    def __init__(self, tamanhoChave, N):
        super(KdTree, self).__init__()
        
        self.apontador_memoria = Stack(N)
        for k in range(0, N):
            self.apontador_memoria.Push(k)
            pass
        self.N = N
        self.nos = [ No(0, '') for k in range(N)]
        self.NIL = None
        self.ROOT = None
        
        self.tamanhoChave = tamanhoChave
        self.listaNos = []
        #self.nos = [ No(0, '') for k in range(6)]
        #self.no = NoRedBlack(self.tamanhoChave, '', None)
        pass
    
    #Metodo _str_, retorna uma string com a Arvore binaria
    def __str__(self):
        t = '\nArvore Binaria, com listas ligadas'
        t += '\n'
        for k in xrange(self.N):
            t += str(k) + ':' +" key: " + str(self.nos[k].key) + " p: " +\
                 str(self.nos[k].parent) + " valor: " +\
                 str(self.nos[k].valor) + " left: " +\
                 str(self.nos[k].left) + " right: " + \
                 str(self.nos[k].right) + '\n'
        return t
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
    
    #Metodo tree_insert
    def tree_insert(self, z, depth = 0):
        y = self.NIL
        x = self.ROOT
        k = len(self.nos[z].key)
        
        axis = depth % k
        
        while( x != self.NIL ):
            axis = depth % k
            y = x
            if self.nos[z].key[axis] < self.nos[x].key[axis]:
                x = self.nos[x].left
                depth += 1
            else:
                x = self.nos[x].right
                depth += 1
                pass
            pass
        self.nos[z].parent = y
        if y == self.NIL:
            self.ROOT = z
        elif self.nos[z].key[axis] < self.nos[y].key[axis]:
            self.nos[y].left = z
        else:
            self.nos[y].right = z
            pass
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
    
    nos[0] = No((7, 2), "Benfica")
    nos[1] = No((5, 4), "Sporting")
    nos[2] = No((9, 6), "Porto")
    nos[3] = No((2, 3), "Academica")
    nos[4] = No((4, 7), "Braga")
    nos[5] = No((8, 1), "Olhanense")
    
    
    NR_CHAVES = len(nos[0].key)
    N = 7
    kd = KdTree(NR_CHAVES, N)

    #retirar chaves dos nos e meter na lista de chaves
    for k in range(NUMERO_NOS):
        listaChaves.append(nos[k].key)
    #fazer a arvore kd apartir da lista de chaves
    kd.KdArvore(listaChaves)
    
    #imprimir a lista de Nos que contem a arvore kd 
    #ja com a ordenaçao correcta 
    print "Imprimir a arvore kd-Tree"  
    for k in range(NUMERO_NOS):
        print kd.listaNos[k]
    
    for i in range(6):
        x = kd.malloc()
        kd.nos[x] = nos[i]
        kd.tree_insert(x)
        pass
    
    print kd
    
    print "Eliminar nó com listas ligadas"
    
    # valor da posição da lista de nós
    # que pretendemos eleminar
    noFree = 3
    x = kd.tree_delete(noFree)
    kd.free(x)
    print kd
    pass
    
    
    
    #criar arvore sem ser sobre uma representaçao de memoria
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
    
    #inserir nós na arvore
    kd.insert_kdTree(nos[0])
    kd.insert_kdTree(nos[1])
    kd.insert_kdTree(nos[2])
    kd.insert_kdTree(nos[3])
    kd.insert_kdTree(nos[4])
    kd.insert_kdTree(nos[5])
    kd.insert_kdTree(nos[6])
    kd.insert_kdTree(nos[7])
    kd.insert_kdTree(nos[8])
    kd.insert_kdTree(nos[9])
    
    #imprimir a arvore, ja ordenada
    print
    print "INORDER"
    lista = []
    kd.inorder_walk(kd.root, lista)
    for x in lista:
        print x
    
    #eleminar nó a arvore RedBlack
    print
    print "Del"
    kd.delete_kdTree(nos[3])    
    #voltar a imprimir a arvore ja com o 
    #nó eliminado
    print "INORDER"
    lista = []
    kd.inorder_walk(kd.root, lista)
    for x in lista:
        print x
        
    #Fazer a pesquisa do nó
    print "PESQUISA"
    print kd.search(kd.root, 5)
    pass
    
    #procurar vizinhos do nó
    print "PESQUISA_Vizinhos "
    print kd.procurarVizinhos(kd.root, 5)
    pass
    
    
    
#Main()