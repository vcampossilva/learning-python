from chapter_08 import *
arquivo = None
try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split(':')
    Perfil(*valores)
    print('arquivo foi aberto')
    arquivo.close()
except IOError as erro: # except (IOError, TypeError) as erro:
    print('Deu IOError')
except TypeError as erro:
    print('Deu TypeError')
finally:
        if(arquivo is not None):
            print('fechando arquivo')
            arquivo.close()
