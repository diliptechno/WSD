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
from nltk.stem import WordNetLemmatizer
import nltk

training_file = sys.argv[1]
train = open("line-train.XML", "r")
print (train)

test_file = sys.argv[2]
print(test_file)
# sense = []
# for line in train:
#     sense.append(line)
# str1 = ''.join(sense).lower()
# sense1 = []
# pattern = re.compile(r'senseid="(.*)"')
# matches = pattern.finditer(str1)
# for match in matches:
#     sense1.append(match.group(1))
#
#
# fdist_sense1 = FreqDist(sense1)
#
# sense2 = []
# pattern1 = re.compile(r'<head>(.*)</head>')
# matches1 = pattern1.finditer(str1)
# for match1 in matches1:
#     sense2.append(match1.group(1))
#
# feat = []
# pattern2 = re.compile(r'<head>(.*)</head>(.*)')
# matches2 = pattern2.finditer(str1)
# for match2 in matches2:
#     feat.append(match2.group(2))
#
# x = []
# for line in feat:
#     x.append(re.sub(r'(<s>|<\/s>)','',line))
#
#
# x4 = []
# lemmatizer = WordNetLemmatizer()
# for line in x:
#         y3 = lemmatizer.lemmatize(line)
#         x4.append(y3)
#
# # future for word after removing punctuation and using lemma
# x5 = []
# tokenizer = RegexpTokenizer(r'\w+')
# for line in x4:
#         y4 = tokenizer.tokenize(line)
#         x5.append(y4)
#
#
# #feat1 the part before the head -- list
# feat1 = []
# pattern3 = re.compile(r'(.*)<head>(.*)</head>')
# matches3 = pattern3.finditer(str1)
# for match3 in matches3:
#     feat1.append(match3.group(1))
#
#
# #x1
# #after removing the <s> from feat1
# x1 = []
# for line in feat1:
#     x1.append(re.sub(r'(<s>|<\/s>)','',line))
#
# x3 = []
# lemmatizer = WordNetLemmatizer()
# for line in x1:
#         y2 = lemmatizer.lemmatize(line)
#         x3.append(y2)
#
# x2 = []
# tokenizer = RegexpTokenizer(r'\w+')
# for line in x1:
#         y1 = tokenizer.tokenize(line)
#         x2.append(y1)
#
# past2 = []
# for line in x2:
#     past2.append(line[-10:])
#
# fut2 = []
# for line in x5:
#     fut2.append(line[:10])
#
# combined = [x+y for x,y in zip(past2,fut2)]
#
#
#
