# Translucency vs. Transparency
This project investigates whether transparency scores correlate with translucency scores. Many ASL signs are said to be iconic with respect to their lexical meaning. The sign CAT, for instance, is signed by tracing the outline of whiskers. Non-signers will agree that the sign CAT looks like its meaning when presented with its English equivalent, but are less likely to accurately name the sign without the translation (Klima & Bellugi, DATE). We replicate this finding by asking non-signers to label verbs that vary with respect to their translucency (these measures were obtained from ASL-LEX.org). However, instead of scoring '1' HIT and '0' MISS, we use a measure of the semantic similarity (REF). Preliminary results are dichotomous, with items with low and medium translucency scores having very low transparency scores, and items with high translucency scores having high transparency scores.

#translucency.py
Five verb labels for 15 ASL lexical verbs were obtained from non-signer participants via Amazon Mechanical Turk (AMT). The verbs were chosen according to their lexical iconicity scores from ASL-LEX. 5 have low iconicity ratings (M = 1.453), 5 have median iconicity ratings (M = 3.102), and 5 have high iconicity ratings (M = 6.784). Results from the experiment were scrubbed (e.g., spell-checked) and are contained in the file data-scrubed.csv. translucency.py computes semantic similiarity scores between (a) all of the participant labels ("intra" similarity score) and (b) between each participant label and the sign's gloss ("inter" similarity score). The function additionally (a) computes the pearson correlation between similarity scores and iconicity scores and (b) plots similarity score as a function of iconicity score.

#translucency-live-action.py
30 - 31 sentence labels for 80 live actions were obtained from participants via AMT. The script identifies and isolates the first verb of each sentence label. For each action, the script computes the similarity score between each of the 30 - 31 verbs and averages the scores together. 
