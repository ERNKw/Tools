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

#executa o gauplus para pegar as urls e jogar no arquivo gau.txt
os.system("cat urls.txt | gauplus > gau.txt")

#executa o kxss e filtra com sed para pegar apenas as urls e jogar no arquivo kxss.txt
os.system("cat gau.txt | kxss | sed 's/.*http/http/' >> kxss.txt")
#executa o script de xss para cada url
os.system("cat kxss.txt | dalfox pipe -S --mining-dict | tee  dalfox.txt")
