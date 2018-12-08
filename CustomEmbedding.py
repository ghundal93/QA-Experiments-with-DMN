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
        
    fact_story = [] 
    fact_stories = []
    questions = []
    answers = []
    fact_idx = 0
    print("opening:",filename)
    file = open(filename,'r')
    for line in file.readlines(): 
        
        flag_end_story = 0 
        line = line.lower() 
        if '? ' in line:
            #q for question, a for answer.
            flag_end_story=1
            qa = line.strip().split('\t')
#             if "squad" in filename:
#                 print(qa)
            q = qa[0]
            a = qa[1]
            #q = q.translate(None, string.punctuation)
            #a = a.translate(None, string.punctuation)
            q = ' '.join(q.split())
            a = ' '.join(a.split())
            q = q.strip().split(' ')
            a = a.strip().split(' ')
            q = q[1:]
            fact_stories.append(q)
            fact_stories.append(a)
            
        else: 
            line = line.translate(None, string.punctuation)
            fact = line.strip().split()
            fact_idx += 1
            fact = fact[1:]
            fact_stories.append(fact)

        if flag_end_story == 1: 
#             fact_stories.append(fact_story)
            fact_idx = 0
            
    file.close()
        
    return fact_stories


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




