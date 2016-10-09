import json
import re
from mainfile import dictionary, tweet_file, sentiment_location, wc_location, dictionary, hashtag_file, hashtag_graph
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import codecs
from django.core.files import File

from mainfile import change_loc, change
from ..models import Query

def hashtag_plot(c):
    xaxis = range(len(c))
    keys_freq = []
    values_freq = []
    for key, value in c.most_common()[::-1]:
        keys_freq.append(key)
        values_freq.append(value)
    fig = plt.figure()
    plt.subplot(211)
    plt.bar(xaxis, values_freq, align='center')
    plt.xticks(xaxis, keys_freq)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    fig.tight_layout()
    plt.savefig(hashtag_graph)



def clean_text(text):
    text = re.sub(r'\'+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'(https?://[^\s]+)', ' ', text, flags=re.MULTILINE)
    text = re.sub('[$,?!\n]', ' ', text)
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
    text = re.sub('[^A-Za-z0-9 ]+', ' ', text)
    return text


def hash_main():
    query = Query.objects.all()[len(Query.objects.all()) - 1].tag
    query_location = '/dataset/' + query + '.json'
    print("calculating Hashtag Count.........")
    open(hashtag_file, "w")
    cnt = Counter();
    id_list = list()
    with open('./sentiment/code' + query_location) as f:
        myf = File(f)
        for line in myf:
            try:
                tweet = json.loads(line)
                if 'text' in tweet:
                    idt = str(tweet['id'])
                    #print (idt,"id")
                    id_list.append(idt)
                    text = str(tweet['text'].encode(encoding='utf8'))
                    text = clean_text(text)
                    hash_tags = []
                    for hashtag in tweet['entities']['hashtags']:
                        ht = hashtag['text']
                        with codecs.open(hashtag_file, 'a', encoding='utf8') as f:
                            myh = File(f)
                            myh.write(ht + '\n')

            except KeyError:
                continue

    for line in codecs.open(hashtag_file, 'r', encoding='utf8'):
        for word in line.split ():
            cnt [word] += 1
    hashtag_plot(cnt)
    print("Hashtag_graph was created")

hash_main()