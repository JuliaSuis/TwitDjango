from django.shortcuts import render
from django.http import HttpResponse
from .models import Query
import codecs
import os
from sentiment.code.mainfile import dictionary, tweet_file, sentiment_location, wc_location, hashtag_graph, url_sentiment
from sentiment.code.sentiment import print_lines, tweet, tweet_wordcloud
from sentiment.code.auth import author
from sentiment.code.hashtag import hash_main

def main():
    dic = {}
    #open(tweet_file, "w")
    from sentiment.code.mainfile import change_loc, change
    query = change()
    query_location = change_loc()
    #print("query and query_loc in views.py" + query + ", " + query_location)
    from sentiment.code.sentiment import print_lines, tweet, tweet_wordcloud
    from sentiment.code.auth import author
    author()
    with codecs.open(tweet_file, 'w'):
        print_lines()
        tweet()
        #print("Tweet Sentiment pie chart generated at:", sentiment_location)
        tweet_wordcloud()
        #print("Tweet Word Cloud generated at:", wc_location)
    from sentiment.code.hashtag import hash_main
    hash_main()
    from sentiment.code.url_sentiment import urlssentiment
    urlssentiment()


def index(request):
    #main()

    return render(request, 'sentiment/main.html')

def loadImagePage(request):
    return render(request, 'sentiment/image.html')

def search_query(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')

        Query.objects.create(
            tag = query
        )

        previousQuery = Query.objects.all()[len(Query.objects.all()) - 2].tag
        Qlocation = os.getcwd() + '/sentiment/code/dataset/' + previousQuery + '.json'
        print("Qlocation: ", Qlocation)
        try:
            os.remove(Qlocation)
        except:
            pass

        try:
            os.remove(tweet_file)
        except:
            pass

        try:
            os.remove(url_sentiment)
        except:
            pass

        try:
            os.remove(sentiment_location)
        except:
            pass
        try:
            os.remove(wc_location)
        except:
            pass
        try:
            os.remove(hashtag_graph)
        except:
            pass


        print("Removed")
        main()

        return render(request, 'sentiment/image.html')

