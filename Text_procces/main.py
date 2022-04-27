import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

txt = open('tale.txt','r')

tokens = word_tokenize(txt.read())

tokens=[word.lower() for word in tokens]

stop_words = set(stopwords.words('danish'))
tokens = [w for w in tokens if not w in stop_words]

words = ' '.join(tokens)

wordcloud = WordCloud().generate(words)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()