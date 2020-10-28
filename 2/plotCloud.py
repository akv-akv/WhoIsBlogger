import pandas as pd
from wordcloud import WordCloud
import multidict as multidict
import numpy as np
import os
import re
from PIL import Image
from os import path
import matplotlib.pyplot as plt

def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}
    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


def makeImage(text):
    wc = WordCloud(background_color="white", max_words=50)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Open xlsx and combine text
df =  pd.read_excel('articles.xlsx')
text = ' '.join(df['Article'])
makeImage(getFrequencyDictForText(text))

# Additionaly plot cloud for Title
text = ' '.join(df['Title'])
makeImage(getFrequencyDictForText(text))
