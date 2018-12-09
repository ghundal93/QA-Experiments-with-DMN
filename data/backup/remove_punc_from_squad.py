import os
import string
import sys

mode = sys.argv[1]

output = open("punc_removed_"+str(mode)+".txt","w")
for i,line in enumerate(open("cleaned_squad_"+str(mode)+".txt")):
    if "?" in line:
        idx = line.find('?')
        tmp = line[idx+1:].split('\t')
        q = line[:idx+1]
        a = tmp[1].strip()
        a = a.replace(","," ")
        a = a.translate(None, string.punctuation)
        q = q.translate(None, string.punctuation)
        q = q+"?"
        output_line = q + "\t" + a
        for i in range(2,len(tmp)):
            output_line += "\t"+tmp[i]
        output.write(output_line)
    else:
        line = line.translate(None, string.punctuation)
        output.write(line)
print("done")
