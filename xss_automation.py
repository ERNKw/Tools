#xss_automation.py
#Author: Runknaw
#Date: 21/11/2022
#Description: esse script tem como executar a sequência de comandos: cat urls.txt | gauplus | kxss 
# fazer a filtragem do kxss e jogar para um arquivo de texto
# depois rodar o script de xss para fazer a verificação de cada url
#Usage: python3 xss_automation.py

import os
import sys
import time

#abre o arquivo de urls e executa os comandos para cada url
file = open("urls.txt", "r")
for line in file:
    line = line.strip()
    os.system("echo " + line + " | gauplus | kxss | grep -Eo '(http|https)://[a-zA-Z0-9./?=_-]*' | uniq -u >> kxss.txt")

#faz a filtragem do arquivo kxss.txt com o re - regex
os.system("dalfox file kxss.txt -S -w 200")
