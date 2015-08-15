# -*- coding: UTF-8 -*-
# app.py
import re

def cadastrar(nomes):
    print 'Digite o nome: '
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def listar(nomes):
    print 'Listando nomes: '
    for nome in nomes:
            print nome

def alterar(nomes):
    print 'Qual nome você deseja alterar?'
    nome = raw_input()
    if(nome in nomes): #verificar existência em uma lista
        print 'Digite um novo nome:'
        novo_nome = raw_input()
        indice = nomes.index(nome) #recuperar indice
        nomes[indice] = novo_nome
        print nomes

def procurar (nomes):
    print 'Qual nome deseja procurar:'
    nome_procurado = raw_input()
    if(nome_procurado in nomes):
        print 'Nome %s encontrado' % (nome_procurado)
    else:
        print 'Desculpe, nome %s não encontrado' % (nome_procurado)

def procurar_por_regex(nomes):
    print 'Digite a rEgex: '
    rEgex = raw_input()
    junta_tudo = ' '.join(nomes)    
    resultados = re.findall(rEgex, junta_tudo)
    print resultados

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: '
        print '1 - para cadastrar'
        print '2 - para listar'
        print '3 - para remover'
        print '4 - para alterar'
        print '5 - para procurar'
        print '6 - para procurar pos rEgex'
        print '0 - para terminar'

        escolha = raw_input()
        if(escolha == '1'): #sempre colocar no fim
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar(nomes)
        if(escolha == '6'):
            procurar_por_regex(nomes)
menu()
