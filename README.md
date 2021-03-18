# Translucency vs. Transparency
This project investigates whether transparency scores correlate with translucency scores. Many signs in American Sign Language (ASL) are said to be iconic with respect to their lexical meaning. The sign CAT, for instance, is signed by tracing the outline of whiskers. Non-signers will agree that the sign CAT looks like its meaning when presented with its equivalent English word, but are less likely to accurately name the sign without the translation (Klima & Bellugi, 1979). A sign is said to be translucent if non-signers agree that it looks like what it means with the translation. A sign is said to be transparent if non-signers can accurately name the sign without translation.

<img src="https://github.com/C-huck/C-huck.github.io/raw/master/images/cat-translucent.png" width="495" height="auto"> <img src="https://github.com/C-huck/C-huck.github.io/raw/master/images/cat-transparent.png" width="495" height="auto">


We replicate this finding by asking non-signers to label verbs that vary with respect to their translucency (these measures were obtained from ASL-LEX.org), selecting 15 verbs that have low, medium, and high iconicity scores (5 at each level). However, instead of scoring '1' HIT and '0' MISS, we use a measure of the semantic similarity (obtained from wordnet). Preliminary results are dichotomous, with items with low and medium translucency scores having very low transparency scores, and items with high translucency scores having high transparency scores. 

## translucency.py

Five verb labels for 15 ASL lexical verbs were obtained from non-signer participants via Amazon Mechanical Turk (AMT). The verbs were chosen according to their lexical iconicity scores from ASL-LEX. 5 have low iconicity ratings (M = 1.453), 5 have median iconicity ratings (M = 3.102), and 5 have high iconicity ratings (M = 6.784). By a two-sample t-test, mean iconicity scores from each group are significantly different at p<<0.001 (uncorrected). Results from the experiment were scrubbed (e.g., spell-checked) and are contained in the file data-scrubed.csv. translucency.py computes semantic similiarity scores between (a) all of the participant labels ("intra" similarity score) and (b) between each participant label and the sign's gloss ("inter" similarity score). The function additionally (a) computes the pearson correlation between similarity scores and iconicity scores and (b) plots similarity score as a function of iconicity score.

## translucency-live-action.py

It is hard to interpret the translucency scores on their own. A reasonable baseline might be how "translucent" live actions are. To that end, we conducted a small experiment in which 30 - 31 sentence labels for 80 live actions were obtained from participants via AMT. The script identifies and isolates the first verb of each sentence label. The verb is then lemmatized. For each action, the script computes the similarity score between each pair of verbs (406 comparisons) and averages the scores together. 

## comparisons

We compared the 15 mean similarity scores from the ASL transparency experiment with the 80 mean similarity scores from the live-action transparency experiment and found no significant difference. The results are difficult to interpret considering the sample sizes, but they indicate (so far) that people are no better at consistently labeling live actions as they are ASL lexical verbs. This suggests that ASL lexical verbs are more translucent than previously thought. 
Mean semantic similarity score for ASL lexical verbs was: 0.3818 
Mean semantic similarity score for live actions was: 0.4804
2-sample t-test w/ unequal var. (Welch's t-test): t = 1.122, p = 0.2787

## input files

1. data-scrubbed.csv contains English translations of the ASL videos participants watched and participant labels. File was scraped of personally identifying information (PII) before upload. 
2. action-label-scrubbed.csv contains file descriptions of the videos participants watched and participant response sentences. PII was scraped before upload. 
