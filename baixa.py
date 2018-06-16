##
# Supermercado boa esperanca
# Programa: Copias carga para Visual Mix
# Analista Jacson Milomem
# 11-09-2017
# OBS:
# Compartilhamentos:
# f = \\192.168.0.4\consinco
# p = \\192.168.0.22\lj000001
# q = \\192.168.0.22\lj000002
# r = \\192.168.0.22\lj000003

import os
from datetime import date
import urllib
import shutil
import telepot

now = date.today()

# monta o bot telegran
bot = telepot.Bot("360506330:AAFsuPhXVnpfASrG-2yUaA0o7nlqoXmyduM")

def valida_arquivo(arquivo):
    valor = ''
    for lin in open(arquivo,"r"):
        if 'Error code 404' in lin:
            valor = valor + 'Erro'
    return valor

##
# funcao para baixar o arquivo
#
def baixa_arquivo(url, arquivo ):
    try:
    	urllib.urlretrieve(url, arquivo )
    except IOError as e:
        return "Erro"
    else:
        return "OK"

##
# Altera o Header do arquivo
#
def altera_arquivo(arquivo, chave1, chave2):
    try:
        log = open(arquivo,"r")
        conteudo = log.read()
        log.close()
    except IOError as e:
        return "Erro"
    else:
        try:
            linha = conteudo.replace(chave1,chave2)
            log = open(arquivo,"w")
            log.write(linha)
            log.close()
        except IOError as e:
            return "Erro"
        else:
            return "OK"
##
# Variaveis
#
dia = '{:0>2}'.format(str(now.day))
mes = '{:0>2}'.format(str(now.month))
ano = '{:0>4}'.format(str(now.year))

arqLoja1 = "SAT" + dia + mes + ".001"
arqLoja2 = "SAT" + dia + mes + ".002"
arqLoja3 = "SAT" + dia + mes + ".003"

arqLoja1Novo = "SAT" + dia + mes + ".001"
arqLoja2Novo = "SAT" + dia + mes + ".003"
arqLoja3Novo = "SAT" + dia + mes + ".005"

endLoja1 = "lj000001/vmix/exportacao/"
endLoja2 = "lj000002/vmix/exportacao/"
endLoja3 = "lj000003/vmix/exportacao/"

destLoja1 = "f:\\loja1\\vmix\\retorno"
destLoja2 = "f:\\loja2\\vmix\\retorno"
destLoja3 = "f:\\loja2\\vmix\\retorno"

url = "http://192.168.0.22:8000/"

#arqLog = "LOG" + dia + mes + ".txt"

##
# Abre arquivo de log
#
#arq = open( arqLog , "w")
bot.sendMessage(253633141,"LOG dia "+dia+"-"+mes+"-"+ano)
######################################################
# LOJA 1
######################################################
bot.sendMessage(253633141,"LOJA 1\n -----------------------------------------------\n")

##
# Baixando arquivo Loja 1
#
baixa = baixa_arquivo(url+endLoja1+arqLoja1, arqLoja1Novo)

if baixa == 'Erro':
    bot.sendMessage(253633141,"Erro ao baixar o arquivio loja 1\n")
else:
    bot.sendMessage(253633141,"Arquivo loja 1 baixado\n")

## Verifica se arquivo e valido
valida = valida_arquivo(arqLoja1Novo)
if valida == 'Erro':
    os.remove(arqLoja1Novo)
    bot.sendMessage(253633141,"Arquivio invalido loja 1\n")
else:
    ##
    # Alterando HEADER do arquivo
    #
    """
    alterar = altera_arquivo(arqLoja2Novo, "H"+dia+mes+ano+"00002", "H"+dia+mes+ano+"00003")
    if alterar == "Erro":
        bot.sendMessage(253633141,"Erro ao alterar o arquivio loja 1\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 1 Alterado\n")
    """
    ##
    # Copiando arquivo para pasta
    #
    try:
        shutil.move(arqLoja1Novo, destLoja1)
    except shutil.Error as e:
        bot.sendMessage(253633141,"Erro ao mover o arquivio loja 1\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 1 movido\n")

bot.sendMessage(253633141,"-----------------------------------------------\n")

######################################################
# LOJA 2
######################################################
bot.sendMessage(253633141,"LOJA 2\n -----------------------------------------------\n")

##
# Baixando arquivo Loja 2
#
baixa = baixa_arquivo(url+endLoja2+arqLoja2, arqLoja2Novo)

if baixa == 'Erro':
    bot.sendMessage(253633141,"Erro ao baixar o arquivio loja 2\n")
else:
    bot.sendMessage(253633141,"Arquivo loja 2 baixado\n")

## Verifica se arquivo e valido
valida = valida_arquivo(arqLoja2Novo)
if valida == 'Erro':
    os.remove(arqLoja2Novo)
    bot.sendMessage(253633141,"Arquivio invalido loja 2\n")
else:
    ##
    # Alterando HEADER do arquivo
    #

    alterar = altera_arquivo(arqLoja2Novo, "H"+dia+mes+ano+"00002", "H"+dia+mes+ano+"00003")
    if alterar == "Erro":
        bot.sendMessage(253633141,"Erro ao alterar o arquivio loja 2\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 2 Alterado\n")

    ##
    # Copiando arquivo para pasta
    #
    try:
        shutil.move(arqLoja2Novo, destLoja2)
    except shutil.Error as e:
        bot.sendMessage(253633141,"Erro ao mover o arquivio loja 2\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 2 movido\n")

bot.sendMessage(253633141,"-----------------------------------------------\n")

######################################################
# LOJA 3
######################################################
bot.sendMessage(253633141,"LOJA 3\n -----------------------------------------------\n")

##
# Baixando arquivo Loja 3
#
baixa = baixa_arquivo(url+endLoja3+arqLoja3, arqLoja3Novo)

if baixa == 'Erro':
    bot.sendMessage(253633141,"Erro ao baixar o arquivio loja 3\n")
else:
    bot.sendMessage(253633141,"Arquivo loja 3 baixado\n")

## Verifica se arquivo e valido
valida = valida_arquivo(arqLoja3Novo)
if valida == 'Erro':
    os.remove(arqLoja3Novo)
    bot.sendMessage(253633141,"Arquivio invalido loja 3\n")
else:
    ##
    # Alterando HEADER do arquivo
    #
    alterar = altera_arquivo(arqLoja2Novo, "H"+dia+mes+ano+"00003", "H"+dia+mes+ano+"00005")
    if alterar == "Erro":
        bot.sendMessage(253633141,"Erro ao alterar o arquivio loja 3\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 3 Alterado\n")

    ##
    # Copiando arquivo para pasta
    #
    try:
        shutil.move(arqLoja3Novo, destLoja3)
    except shutil.Error as e:
        bot.sendMessage(253633141,"Erro ao mover o arquivio loja 3\n")
    else:
        bot.sendMessage(253633141,"Arquivo loja 3 movido\n")

bot.sendMessage(253633141,"-----------------------------------------------\n")

##
# fecha arquivo de LOG
#
#arq.close()

"""print now.year
print now.month
print now.day
print arqLoja1
print arqLoja2
print arqLoja3
"""
