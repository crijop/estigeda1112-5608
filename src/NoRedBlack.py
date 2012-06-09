#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 de Mai de 2012

@author: Carlos Palma Nº 5608

Class NoRedBlack
'''
from No import *


'''
class No da Arvore RED BLACK,
recebe como parametro a Class No
'''
class NoRedBlack(No):
    def __init__(self, key, valor, cor):
        super(NoRedBlack, self).__init__(key, valor)
        self.cor = cor
        pass
    
    def __str__(self):
        return super(NoRedBlack, self).__str__() + '-> ' + str(self.cor)
        pass
    pass