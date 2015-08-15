# -*- coding: UTF-8 -*-

import re #regex

resultado = re.match('Py', 'Python')
print resultado
print resultado.group()

resultado = re.match('py', 'Python')
#print resultado.group() #retorna NoneType
#type(resultado) #mostra o tipo

resultado = re.match('[pP]y', 'Python')
print resultado.group()

resultado = re.match('[A-Za-z]y', 'Python')
print resultado.group()

resultado = re.match('[A-Za-z]y', 'Python ou jython')
print resultado.group()

resultados = re.findall('[A-Za-z]y', 'Python ou jython') #para retornar mais de uma ocorrencia
print resultados

resultados = re.findall('[A-Za-z]y[A-Za-z]+', 'Python ou jython') # + tudo o que vier depois
print resultados

resultados = re.findall('\wy\w+', 'Python ou jython') # outra forma, desconsidera acento
print resultados

resultados = re.findall('\wy\w+\d', 'Python ou jython2 ou Pypy')
print resultados

resultados = re.findall('[A-Za-z]+\d?', 'Python ou jython2 ou Pypy ou Pypy44')
print resultados

#r'[A-Z]+' raw string
resultados = re.findall('([fF]\w+)', 'Vinicius Fernando Carlos Fernanda')
print resultados

resultados = re.findall(r'[vV]\w{7}', 'Vinicius Fernando Carlos Fernanda')
print resultados

resultado = re.match(r'^#', '#comentarios começam com tralha') #verificar inicio da string
print resultado.group()

resultado = re.match(r'.*io$', 'http://vcampossilva.github.io') #verificar fim da string
print resultado.group()
