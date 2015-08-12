#tuple

tipos_convite = ['vip', 'normal', 'meia', 'cortesia']

print tipos_convite

tipos_convite.append('penetra')

print tipos_convite

tipos_convite = ('vip', 'normal', 'meia', 'cortesia')

#dictionary

convites = ('vip', 60, 'normal', 40, 'meia', 30, 'cortesia', 0)

print convites

print convites[0:2]

convites_com_valor = {'vip': 60, 'normal' : 40, 'meia' : 30, 'cortesia' : 0}

print convites_com_valor

print convites_com_valor['vip']

print convites_com_valor.keys()

print convites_com_valor.values()

status_civil = ('casado','solteiro') + ('divorciado',)

print status_civil

#verify type

print type(convites_com_valor)
print type(status_civil)

#sum tuple, list

nome = ['Vinicius', 'Rodrigo'] + ['Felipe', 'Pedro']

print nome
print type(nome)

#sum tuple + list
#estados = ('RJ','SP') + ['MG','ES'] -> generate a TypeError: can only concatenate list (not "tuple") to list

#fixing
estados = ('RJ', 'SP') + tuple(['MG', 'ES'])
print estados
print type(estados)

#max/min number
print max([10, 5, 7])
print min([10, 5, 7])

#sorted
nomes = ['Vinicius', 'Rodrigo', 'Felipe', 'Pedro']
print sorted(nomes)

print 'exercicio'
materias_com_peso = {'Equacoes Diofantinas' : 3, 'Algebra Relacional' : 2, 'Portugues instrumental' : 4}
pesos = tuple(materias_com_peso.values())
pesos.append(1)
print pesos
