#keyboard input

nome = raw_input()
print nome
ano = raw_input()

#date function
#from datetime import date
#date.today().year
from datetime import date

print 2015 - int(ano)
print int(date.today().year) - int(ano)

print 'Dia -> ' + str(date.today().day)
print 'Mes -> ' + str(date.today().month)
print 'Ano -> ' + str(date.today().year)
