from bs4 import BeautifulSoup
#import urllib.request
import urllib
from django.core.files import File
import csv
import re
#from importlib import reload
import codecs

from mainfile import dictionary, tweet_file, sentiment_location, wc_location
#from mainfile import change_loc, change

#query = change()
#query_location = change_loc()

#print("................URL Sentiment Analysis........")
#print("................This might take a while.......")
#open(url_sentiment, "w")

def urlssentiment():
    dic={}
    x=0
    url_list=[]
    print("................URL Sentiment Analysis........")
    print("................This might take a while.......")

    with open(dictionary) as f:
        myurl = File(f)
        lines=myurl.readline()
        while(lines!=''):
            lines=f.readline()
            line=lines.split('\t')
            if(len(line) >= 2):
                scores=line[1]
                dic[line[0]]=int(scores)
        myurl.closed
        f.closed


    with codecs.open(tweet_file, 'w+', encoding='utf8') as f:
            myf = File(f)
            for line in myf:
                try:
                    #Checks each line for anything with https
                    tlink = re.search("(?P<url>https?://[^\s]+)", line).group("url")
                    if (len(tlink)==23):
                        soup = BeautifulSoup(urllib.request.urlopen(tlink).read(),'html.parser')
                        # kill all script and style elements
                        for script in soup(["script", "style"]):
                            script.extract()    # rip it out
                        text = soup.get_text()
                        lines = (line.strip() for line in text.splitlines())
                        # break multi-headlines into a line each
                        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                        # drop blank lines
                        text = '\n'.join(chunk for chunk in chunks if chunk)
                        scores=0
                        tup=text.split(" ")
                        if(len(tup)>=1):
                            for x in (tup):
                                if x in dic:
                                    scores=scores + dic[x]
                            if scores > 0:
                                with codecs.open(url_sentiment, 'a', encoding='utf8') as ff:
                                    myff = File(ff)
                                    myff.write(tlink, scores, "Positive")
                                    #print(tlink,scores,"Positive", file=f)
                                    print("pos")
                            elif scores < 0:
                                with codecs.open(url_sentiment, 'a', encoding='utf8') as ff:
                                    myff = File(ff)
                                    myff.write(tlink, scores, "Negative")
                                    #print(tlink,scores,"Positive", file=f)
                                    print("neg")
                            else:
                                with codecs.open(url_sentiment, 'a', encoding='utf8') as ff:
                                    myff = File(ff)
                                    myff.write(tlink, scores, "Neutral")
                                    #print(tlink,scores,"Positive", file=f)
                                    print("neu")
                except:
                    tlink = None
#urlssentiment()