import pandas as pd
import numpy as np
from scipy import stats
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer 
from itertools import combinations

def sem_score(df):
  items = list(set(dat['EntryID'])) 
  scores = []
  for x in items:
      temp = list(raw_dat.loc[raw_dat['EntryID'] == x, 'Answer.summary'])
      temp = [pp.lower() for pp in temp]
      if x == "tear": #manual fix so synsets doesn't select 'tear' as in 'rip'
          x = "cry"
      lemmatizer = WordNetLemmatizer()
      word_list_synsets = []
      for xx in temp:
          w1 = lemmatizer.lemmatize(xx,pos='v')
          w2 = wn.synsets(w1,pos="v")
          for y in w2: #selecting the most frequent sense decreases semantic similarity
              if w1 in str(y):
                  word_list_synsets.append(y)
                  break #item is skipped if not in synset
      iters = list(combinations(range(len(word_list_synsets)),2))
      sim_scores = []
      for z in iters:
          sim_scores.append(word_list_synsets[z[0]].path_similarity(word_list_synsets[z[1]]))          
    gt_scores = []
    gt_synset = False
    ww1 = lemmatizer.lemmatize(x,pos='v')
    ww2 = wn.synsets(x,pos="v")
    for yy in ww2:
        if ww1 in str(yy):
            gt_synset = yy
            break
    if gt_synset:
        for wls in word_list_synsets:
            print(wls,gt_synset)
            gt_scores.append(gt_synset.path_similarity(plo))
    else:
        gt_scores = 0
    scores.append([x,np.mean(sim_scores),np.mean(gt_scores)])
    return scores

##read in AMT data
dat = pd.read_csv("scrubbed-data.csv",usecols=["Input.field_1","Answer.summary"])
dat['EntryID'] = [x[:-4].lower() for x in dat['Input.field_1']]

##read in ASL-LEX data
df_LEX = pd.read_csv("iconicity-scores.csv",usecols=['EntryID','Icon'],header=0)

##Get similarity scores
df_scores = pd.DataFrame(data=sem_score(dat),columns=['EntryID','intra score','inter score'])   

##Merge dfs together
df = pd.merge(df,df_scores,on="EntryID")

##Calculate correlation
from scipy.stats import pearsonr, spearmanr    

print(pearsonr(df['inter score'],df['Icon']))    
print(spearmanr(df['inter score'],df['Icon']))    

##Visualize data
import matplotlib.pyplot as plt    
plt.scatter(df['Icon'],df['inter score'])




