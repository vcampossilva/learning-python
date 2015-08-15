def processa_convite(nome):
    nome_formatado = gera_nome_convite(nome)
    envia_convite(nome_formatado)

def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial : posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_formatado):
    print 'Enviando convite para %s' % (nome_formatado)
