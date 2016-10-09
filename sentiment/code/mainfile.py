import os
from ..models import Query

def change():
    query = Query.objects.all()[len(Query.objects.all())-1].tag
    return query

def change_loc():
    query_location = '/dataset/' + change() + '.json'
    return query_location

#query = change()

location = os.getcwd()
print(location)

#query_location=location + '/sentiment/code/dataset/' + query +'.json'



dictionary='/home/julia/code/DjangoTM/twitTMP/sentiment/code/dataset/' +'AFINN-111.txt'
tweet_file='/home/julia/code/DjangoTM/twitTMP/sentiment/code/dataset/' +'tweet_out.txt'
sentiment_location='/home/julia/code/DjangoTM/twitTMP/sentiment/static/img/' +'sentiment.png'
wc_location='/home/julia/code/DjangoTM/twitTMP/sentiment/static/img/' +'wc.png'
url_sentiment=location+ '/sentiment/code/dataset/' +'url_sentiment.txt'
hashtag_file=location+ '/sentiment/code/dataset/' +'hashtag.txt'
hashtag_graph=location+ '/sentiment/static/img/' +'hashtag.png'

#print(query_location)
#print(dictionary)
print(tweet_file)
#print(sentiment_location)
#print(wc_location)
#print(url_sentiment)
#print(hashtag_file)
#print(hashtag_graph)
