import os
import string
import sys

mode = sys.argv[1]

output = open("data/en/squad-v1.1.json_"+str(mode)+".txt","w")
for i,line in enumerate(open("data/en/punc_removed_"+str(mode)+".txt")):
    if "?" in line:
        output.write(line)
    else:
        #print("before:",line)
        line = line.strip("\n")+"."+"\n"
        #print("after:",line)
        output.write(line)
print("done")
