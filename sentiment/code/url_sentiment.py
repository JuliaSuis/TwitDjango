from bs4 import BeautifulSoup
#import urllib.request for Python3 !!!
# in case you use Python3 change line 49 to
#           soup = BeautifulSoup(urllib.request.urlopen(tlink.encode(encoding='utf8')).read(),'html.parser')
#
import urllib #for Python2.7 !!!
from django.core.files import File
import csv
import re
#from importlib import reload
import codecs

from mainfile import dictionary, tweet_file, sentiment_location, wc_location, url_sentiment
#from mainfile import change_loc, change

def urlssentiment():
    dic={}
    x=0
    url_list=[]
    print("URL Sentiment Analysis")
    print("This might take a while")

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
            #myf = File(f)
            for line in f:
                #try:
                    #Checks each line for anything with https
                    tlink = re.search('(?P<url>https?://[^\s]+)', line)
                    #if tlink is None:
                    #    pass
                    #else:

                    if (tlink != None):
                        tlink = tlink.group("url")
                        if (len(tlink)==23):
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
                            if(len(tup)>=1):
                                with codecs.open(url_sentiment, 'a+', encoding='utf8') as f:
                                    for x in (tup):
                                        if x in dic:
                                            scores=scores + dic[x]
                                    if scores > 0:
                                        wlink = tlink + " " + str(scores) + " Positive"
                                        f.write(wlink)
                                        f.write('\n')
                                    elif scores < 0:
                                        wlink = tlink + " " + str(scores) + " Negative"
                                        f.write(wlink)
                                        f.write('\n')
                                    else:
                                        wlink = tlink + " " + str(scores) + " Neutral"
                                        f.write(wlink)
                                        f.write('\n')
    print("url_sentiment.txt was successfully created!")
                #except:
                    #print("!!!EXEPT!!!")
                    #tlink = None
