from optparse import OptionParser
import time

option_parser = OptionParser()
option_parser.add_option("-d",dest="domain",help="Domínio")
option,args = option_parser.parse_args()

lista = open('dorks.txt', 'r') # Abre o arquivo dorks.txt
for dork in lista: # Para cada dork no arquivo dorks.txt
    print('[+] site:' + option.domain + ' ' + dork) # Mostra a dork que está sendo gerada
    time.sleep(0.1)
lista.close() # Fecha o arquivo dorks.txt
