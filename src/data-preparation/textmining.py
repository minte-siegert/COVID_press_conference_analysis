import pandas as pd
from textblob import TextBlob
import os
from googletrans import Translator
from pattern3.nl import sentiment

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t')
 
# add sentiment score    
cnt_1 = 0 
for i, j in data.iterrows():
    cnt_1 += 1
    print ("1/3: ", cnt_1)
    try:
        text = (j['text'])
        data.loc[i, 'sentiment'] = sentiment(text)

    except:
        data.loc[i, 'sentiment'] = '0'

# split up sentiment scores in polarity and subjectivity
cnt_2 = 0 
for i, j in data.iterrows():
    cnt_2 += 1
    print ("2/3: ", cnt_2)
    try:
        data.loc[i, 'polarity'] = (j['sentiment'][0])
        data.loc[i, 'subjectivity'] = (j['sentiment'][1])
    except:
        data.loc[i, 'polarity'] = 0
        data.loc[i, 'subjectivity'] = 0

# categorize the scores
def sentiment_category(sentiment_score):
    predictedSentiment = 'neutral'
    if sentiment_score > 0.2:
        predictedSentiment = 'positive'
    elif sentiment_score < -0.2:
        predictedSentiment = 'negative'
    return predictedSentiment

cnt_3 = 0 
for i, j in data.iterrows():
    cnt_3 += 1
    print ("3/3: ", cnt_3)
    try:
        sentiment_score = j['polarity']
        data.loc[i, 'sentiment_category'] = sentiment_category(sentiment_score)

    except:
        data.loc[i, 'sentiment_category'] = 'neutral'

# adding time stamps
# Extracting time from 'created_at', and transferring them to dutch time by adding two hours.
for i, line in data.iterrows():
    time = (line[1][10:16])
    time_h = (line[1][10:13])
    time_h_2 = int(time_h) + 2
    time_m = (line[1][13:16])
    data.loc[i,'time_stamps'] = str(time_h_2) + str(time_m)

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done.')
