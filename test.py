data = SentimentintensityAnalyzer()
labels = []
scores = []
for text in df['stemming_data']:
    sentiment_scores = data.polarity_scores (text)
    compound_score = sentiment_scores [ 'compound']
    scores.append(compound_score)
    if compound_score > 0:
        label = 'positif'
    elif compound_score < 0:
        label = 'negatif'
    else:
        label = 'netral'
    labels.append(label)

df['sentiment_score'] = scores
df['sentiment'] = labels

data = ['stemming_data', 'sentiment_score', 'sentiment']
data=df[data]

data.head(5)