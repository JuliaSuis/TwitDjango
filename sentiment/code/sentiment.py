'''
A script which takes two files as parameters.A file containing LiveTweets file as the first argument and other argument as
a file containing sentiment scores for each term
'''

import sys
import json

#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from importlib import reload
#import mainfile
import codecs
from django.core.files import File
from ..models import Query

#reload(mainfile)
from mainfile import dictionary, tweet_file, sentiment_location, wc_location
from mainfile import change_loc, change

query = change()
query_location = change_loc()

dic = {}

print("Gathering Tweet Sentiment............")


def print_lines():
    x = 0
    with open(dictionary) as f:
        mydict = File(f)
        lines = mydict.readline()
        while (lines != ''):
            lines = f.readline()
            line = lines.split('\t')
            if (len(line) >= 2):
                scores = line[1]
                dic[line[0]] = int(scores)
                mydict.closed
                f.closed


def tweet_sentiment_plot(cou, pos, neg, neu):
    query = change()
    plt.figure()
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Positive', 'Negative', 'Neutral'
    values = [pos, neg, neu]
    sub_title = "Gathered from a set of ", cou, "Tweets"
    plt.pie(values, labels=labels, shadow=True, autopct='%.2f')
    plt.title(query.title() + ' Twitter Sentiment')
    plt.suptitle(sub_title, y=0.99, fontsize=12)
    plt.savefig(sentiment_location)


# Generate a WordCloud

def tweet_wordcloud():
    text = open(tweet_file).read()
    # text = " ".join(tweets['text'].values.astype(str))
    no_urls_no_tags = " ".join([word for word in text.split()
                                if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                                ])
    wc = WordCloud(background_color="white", max_font_size=40, random_state=42, relative_scaling=.5).generate(
        no_urls_no_tags)
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig(wc_location)


def tweet():
    count = 0
    neu = 0
    pos = 0
    neg = 0
    query = Query.objects.all()[len(Query.objects.all()) - 1].tag
    query_location = '/dataset/' + query + '.json'
    with open('./sentiment/code' + query_location) as fp:
        myfp = File(fp)
        for line in myfp:
            tweet = json.loads(line)
            # print(tweet["text"])
            try:
                #with open(tweet_file, "a") as f:
                with codecs.open(tweet_file, 'a', encoding='utf8') as f:
                    myf = File(f)
                    #print(tweet["text"], file=f)
                    myf.write(tweet["text"])
            except KeyError:
                continue
    with open(tweet_file) as tweetfile:
        # line=tweetfile.readline()
        for line in tweetfile:
            try:
                # while(line!=''and line!='\n'):
                scores = 0
                tup = line.split(" ")
                if (len(tup) >= 1):
                    for x in (tup):
                        if x in dic:
                            scores = scores + dic[x]
                            # print (scores)
                            count = count + 1
                            if scores > 1:
                                pos = pos + 1
                            elif scores < 1:
                                neg = neg + 1
                            else:
                                neu += 1
            except KeyError:
                continue
        #myf.closed
        #f.closed
    return tweet_sentiment(count, pos, neg, neu)


def tweet_sentiment(c, p, n, ne):
    count = c
    positive = float(p) / float(c) * 100
    negative = float(n) / float(c) * 100
    neutral = float(ne) / float(c) * 100
    tweet_sentiment_plot(count, positive, negative, neutral)
    print("Total tweets", c)
    result = '%s %d \n%s %.1f%s \n%s %.1f%s \n%s %.1f%s' % ("Total number of tweets:", c, "Positive:", positive, "%", "Negative:", negative, "%", "Neutral:", neutral, "%");
    print(result)
    # print ("Positive ",float(p/c)*100,"%")
    # print ("Negative ",float(n/c)*100,"%")
    # print ("Neutral ",float(ne/c)*100,"%")


# def tweet_cleaning():


def main():
    dic = {}
    #open(tweet_file, "w")
    with codecs.open(tweet_file, 'w'):
        print_lines()
        tweet()
        print("Tweet Sentiment pie chart generated at:", sentiment_location)
        tweet_wordcloud()
        print("Tweet Word Cloud generated at:", wc_location)



#if __name__ == '__main__':
#main()
