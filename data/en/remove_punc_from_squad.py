import os
import string
output = open("squad-v1.1.json_train.txt","w")
for i,line in enumerate(open("squad-v1.1.json_train_cleaned_backup.txt")):
    if "?" in line:
        output.write(line)
    else:
        line = line.translate(None, string.punctuation)
        output.write(line)
print("done")
