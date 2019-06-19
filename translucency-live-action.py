import csv
import numpy as np
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer 
from itertools import combinations

csvfile = open("action-label-data.csv", 'rt')
reader = csv.DictReader(csvfile)

data = []
for i, row in enumerate(reader):
    subj = ["Subj_"+str(i+1)]
    toget = []
    together = []
    for j in range(1,41):
        together = [str(row['Input.field_'+str(j)+'_1']), str(row['Answer.Choice'+str(j)])]
        toget.append(together)
    data.append(toget)
data_sorted = [sorted(data[i]) for i in range(0,len(data))]

item_list = []
for x in data_sorted:
    for y in x:
        item_list.append(y[0])
item_list = list(sorted(set(item_list)))

sent_sort = []
for x in item_list:
    temp = []
    for y in data_sorted:
        for z in y:
            if z[0] == x:
                temp.append(z[1])
    sent_sort.append([x,temp])

sent_scores = []
for sent in sent_sort:
    word_list = []
    for x in sent[1]:
        text = word_tokenize(x)
        pos = pos_tag(text)
        for y in pos:
            if "V" in y[1]:
                word_list.append(y[0])
    lemmatizer = WordNetLemmatizer()
    word_list_synsets = []
    for x in word_list:
        w1 = lemmatizer.lemmatize(x,pos='v')
        #print(x,w1)
        w2 = wn.synsets(w1,pos="v")
        for x in w2:
            if w1 in str(x):
                #print("yes",w1,w2)
                word_list_synsets.append(x)
                break
    iters = list(combinations(range(len(word_list_synsets)),2))
    sim_scores = []
    for x in iters:
        sim_scores.append(word_list_synsets[x[0]].path_similarity(word_list_synsets[x[1]])) 
    sent_scores.append([sent[0],np.mean(sim_scores)])

#summary stats
print(np.mean([y[1] for y in sent_scores]))
print(min([y[1] for y in sent_scores]),max([y[1] for y in sent_scores]))
print(np.percentile([y[1] for y in sent_scores], [25, 50, 75]))
