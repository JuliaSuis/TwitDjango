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

dictionary=location + '/sentiment/code/dataset/' +'AFINN-111.txt'
tweet_file=location + '/sentiment/code/dataset/' +'tweet_out.txt'
sentiment_location= location + '/sentiment/static/img/' +'sentiment.png'
wc_location= location + '/sentiment/static/img/' +'wc.png'

url_sentiment=location+ '/sentiment/code/dataset/' +'url_sentiment.txt'
hashtag_file=location+ '/sentiment/code/dataset/' +'hashtag.txt'
hashtag_graph=location+ '/sentiment/static/img/' +'hashtag.png'

#dictionary='/home/julia/code/DjangoTM/twitTMP/sentiment/code/dataset/' +'AFINN-111.txt'
#tweet_file='/home/julia/code/DjangoTM/twitTMP/sentiment/code/dataset/' +'tweet_out.txt'
#sentiment_location='/home/julia/code/DjangoTM/twitTMP/sentiment/static/img/' +'sentiment.png'
#wc_location='/home/julia/code/DjangoTM/twitTMP/sentiment/static/img/' +'wc.png'