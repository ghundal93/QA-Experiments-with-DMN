import re
import os

#output = open("cleaned_squad_test.txt","w")
for i,line in enumerate(open("cleaned_squad_train.txt")):
    if("?" in line):
        idx = line.find('?')
        tmp = line[idx+1:].split('\t')
        if len(tmp) <=1:
            print(line)
#            output.write(line)
#        else:
#            output.write(line)
#    else:
#        output.write(line)
#output.close()
print("da da")
