from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import openpyxl
import nltk

#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

## Set range of dates and topic
googlenews=GoogleNews(start='10/01/2020',end='10/28/2020')
googlenews.search('Russia')

## Get first page of results
result=googlenews.result()
df=pd.DataFrame(result)
print(df.head())
print(df.shape)

## Get remaining pages of results (max 20)
for i in range(2,20):
    googlenews.getpage(i)
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(i)
    print(df.head())
    print(df.shape)
list=[]

## Download article texts with newspaper package
for ind in df.index:
    try:
        print(ind)
        dict={}
        article = Article(df['link'][ind],config=config)
        article.download()
        article.parse()
        article.nlp()
        dict['Date']=df['date'][ind]
        dict['Media']=df['media'][ind]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        list.append(dict)
    except:
        pass

## Save result into xlsx
news_df=pd.DataFrame(list)
news_df.to_excel("articles.xlsx")
