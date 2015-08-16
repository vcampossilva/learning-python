# -*- coding: UTF-8 -*-
# pessoa.py

class Pessoa(object):
    'Classe para calcular IMC'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime_imc(self):
        imc = self.peso / (self.altura * self.altura)
        print 'IMC de %s: %s' % (self.nome, imc)       
