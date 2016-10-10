from bs4 import BeautifulSoup
#import urllib.request
import urllib
from django.core.files import File
import csv
import re
#from importlib import reload
import codecs

from mainfile import dictionary, tweet_file, sentiment_location, wc_location, url_sentiment
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
    print(".............URL Sentiment Analysis........")
    print(".............This might take a while.......")

    with open(dictionary) as f:
        myf = File(f)
        lines=myf.readline()
        while(lines!=''):
            lines=f.readline()
            line=lines.split('\t')
            if(len(line) >= 2):
                scores=line[1]
                dic[line[0]]=int(scores)
        print("__done with dictionary__")


    with codecs.open(tweet_file, 'r', encoding='utf8') as f:
            print("Opened___" + tweet_file + "___")
            #myf = File(f)
            for line in f:
                #try:
                    print("__TRY TO TRY__")
                    #Checks each line for anything with https
                    tlink = re.search('(?P<url>https?://[^\s]+)', line)
                    if tlink is None:
                        print("NONE NONE NONE")
                    else:
                        tlink = tlink.group("url")
                    print("_____Tlink____", tlink)
                    if (tlink != None):
                        if (len(tlink)==23):
                            print("__if is working__")
                            soup = BeautifulSoup(urllib.urlopen(tlink.encode(encoding='utf8')).read(),'html.parser')
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
                            print("__tup__", tup)
                            if(len(tup)>=1):
                                print("URL SENTIMENT IS HERE--------" + url_sentiment)
                                with codecs.open(url_sentiment, 'a+', encoding='utf8') as f:
                                    for x in (tup):
                                        if x in dic:
                                            scores=scores + dic[x]
                                    if scores > 0:
                                        wlink = tlink + " " + str(scores) + " Positive"
                                        f.write(wlink)
                                        f.write('\n')
                                        print("pos")
                                    elif scores < 0:
                                        wlink = tlink + " " + str(scores) + " Negative"
                                        f.write(wlink)
                                        f.write('\n')
                                        print("neg")
                                    else:
                                        wlink = tlink + " " + str(scores) + " Neutral"
                                        f.write(wlink)
                                        f.write('\n')
                                        print("neu")
                #except:
                    #print("!!!EXEPT!!!")
                    #tlink = None
#urlssentiment()