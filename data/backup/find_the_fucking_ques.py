import re
import os
import sys

mode = sys.argv[1]
output = open("cleaned_squad_"+mode+".txt","w")
for i,line in enumerate(open("squad-v1.1.json_"+mode+"_backup.txt")):
    if("?" in line):
        idx = line.find('?')
        tmp = line[idx+1:].split('\t')
        if len(tmp) <=1:
            print("here cleaning")
            line = line.replace("?","")
            output.write(line)
        else:
            output.write(line)
    else:
        output.write(line)
output.close()
print("da da")
