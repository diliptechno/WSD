
# coding: utf-8

# In[87]:


import sys
import re
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from random import random
import numpy as np
import pandas as pd
import csv
from xml.dom import minidom
import xml.etree.ElementTree as et
import os


# In[88]:


train = open("line-train.XML", "r")


# In[89]:


sense = []
for line in train:
    sense.append(line)


# In[ ]:


sense


# In[90]:


str1 = ''.join(sense)
sense1 = []
pattern = re.compile(r'senseid="(.*)"')
matches = pattern.finditer(str1)
for match in matches:
    sense1.append(match.group(1))


# In[ ]:


sense1


# In[91]:


sense2 = []
pattern1 = re.compile(r'<head>(.*)</head>')
matches1 = pattern1.finditer(str1)
for match1 in matches1:
    sense2.append(match1.group(1))


# In[ ]:


sense2


# In[92]:


feat = []
pattern2 = re.compile(r'<head>(.*)</head>(.*)')
matches2 = pattern2.finditer(str1)
for match2 in matches2:
    feat.append(match2.group(2))


# In[103]:


feat


# In[93]:


feat1 = []
pattern3 = re.compile(r'(.*)<head>(.*)</head>')
matches3 = pattern3.finditer(str1)
for match3 in matches3:
    feat1.append(match3.group(1))


# In[125]:


x1 = []
for line in feat1:
    x = re.sub(r'(<s>|<\/s>)','',line)
    x = re.sub(r'(\.)',' . ',x)
    x1.append(re.sub(r'(<s>|<\/s>)','',x))
    


# In[126]:


x1


# In[127]:


# for line in feat1:
#     pat = re.compile(r'(([^\s>]+) [\S]+ )$')
#     mat = pat.search(line)
#     x =mat.group(1)
#     print(x)
past2 = []
for line in x1:
    past2.append(line.split()[-2:])


# In[128]:


# type(past2[1])
past2


# In[117]:


# str2 = ''.join(feat1)
# past2 = []
# pattern4 = re.compile(r'<\/s><s>([^<]*)')
# matches4 = pattern4.finditer(str2)
# for match4 in matches4:
#     past2.append(match4.group(1))
fut2 = []
for line in feat:
    fut2.append(line.rstrip('</s>').split()[-2:])


# In[118]:


fut2


# In[31]:


str2


# In[ ]:


df = pd.DataFrame(
    {'sense': sense1,
     'target_word': sense2
    })


# In[34]:


len(df)


# In[ ]:


df.to_csv("trainsense.csv")


# In[ ]:


fdist_sense = FreqDist(df["sense"])
fdist_sense


# In[ ]:


fdist_target = FreqDist(df["target_word"])
fdist_target


# In[ ]:


sense_target=df.groupby(["sense","target_word"]).size()


# In[ ]:


sense_target

