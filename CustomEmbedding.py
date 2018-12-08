#!/usr/bin/env python
# coding: utf-8

# In[14]:


from gensim.models import Word2Vec
from os import listdir
from os.path import isfile, join
import string
import sys

# In[15]:


mypath = "data/en/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

dim = sys.argv[1]

# In[16]:


# train_files = [x for x in onlyfiles if "test" not in x]
# print(train_files)


# In[26]:


def extract_info(filename):  
    print "==> Embedding from from %s" % filename
    sentences = []
    for i, line in enumerate(open(filename)):
        line = line.strip()
        line = line.replace('.', ' . ')
        line = line[line.find(' ')+1:]
        if line.find('?') == -1:
            sentences.append(line)
        else:
            idx = line.find('?')
            tmp = line[idx+1:].split('\t')
            ques = line[:idx]
            ans = tmp[1].strip()
            sentences.append(ques)
            sentences.append(ans)

    return sentences


# In[27]:


sentences = []
for filename in onlyfiles:
#    print(mypath+filename)
    fact_stories = extract_info(mypath+filename)
    sentences += fact_stories
#filename = "data/squad1.1/train-v1.1.json_train.txt"
#sentences += extract_info(filename)
#sentences.append(['unk','eos','pad'])


# In[28]:


sentences[-10:]


# In[29]:


model = Word2Vec(sentences, min_count=1,size=int(dim),window=3)


# In[31]:


words = list(model.wv.vocab)
# words.append('unk')
# words.append('eos')
# words.append('pad')
#print(len(words))
#print(words.index('unk'))


# In[32]:


print(model['gray'])


# In[33]:


model.save('data/custom/model' + str(dim) + 'd.bin')


# In[39]:


word = model.wv.similar_by_word("lion",topn=1)
print(word)


# In[ ]:




