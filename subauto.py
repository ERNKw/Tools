import os

with open ('scopo.txt') as f:
    lines = f.readlines()
    for line in lines:
        os.system('sublist3r -o results.txt -d ' + line)
