# -*- coding: utf-8 -*-
'''
Created on 12 de junho de 2012

@author: Carlos Palma Nº 5608

Grafico da relaçao entre o tempo
que leva a criar a arvore, e o numero de nos a 
inserir na arvore
'''
import matplotlib.pyplot as plt
import pickle

ficheiro = open("dados.dat", "r")

listaNumNos = pickle.load(ficheiro)
listaTempos = pickle.load(ficheiro)
ficheiro.close()

plt.xlabel("Numero de Nos a inserir na arvore kd")
plt.ylabel("Tempo que leva a cirar a arvore kd")
plt.title("Relacao entre o tempo(criacao da arvore)/numero de nos da arvore")

grafico = plt.plot(listaNumNos, listaTempos, 'Dg')
plt.grid(True)
plt.savefig('NumeroDocentes200.png')
plt.show()