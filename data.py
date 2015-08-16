# -*- coding: UTF-8 -*-
# data.py

class Data(object):
    'Classe para gerenciar a data'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print '%s/%s/%s' % (self.dia, self.mes, self.ano)
