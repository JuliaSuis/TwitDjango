from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import sys
import os
import codecs
#from importlib import reload
import mainfile


#consumer key, consumer secret, access token, access secret.
ckey="----enter yours one-------"
csecret="----enter yours one-------"
atoken="----enter yours one-------"
asecret="----enter yours one-------"

#reload(mainfile)
from mainfile import change_loc, change
from ..models import Query

#query = change()
#query_location = change_loc()

class listener(StreamListener):
    def __init__(self, count):
        self.counter = 0
        self.limit = 200

    def on_data(self, data):
        query = Query.objects.all()[len(Query.objects.all()) - 1].tag
        query_location = '/dataset/' + query + '.json'
        try:
            with open('./sentiment/code' + query_location, 'a') as f:
                f.write(data)
                self.counter += 1
            if self.counter == self.limit:
                print ("Limit reached. Exiting...")
                return False
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print (status)

def author():

    query = Query.objects.all()[len(Query.objects.all()) - 1].tag
    query_location = '/dataset/' + query + '.json'

    open('./sentiment/code' + query_location, 'w').close()
    try:
        #print("AUTHOR QUERY & QUERY LOC" + query + "__" + query_location)
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterstream = Stream(auth, listener(count=200))
        print("Writing Tweets")
        twitterstream.filter(track=[query])#, languages=['en'])
    except KeyboardInterrupt:
        return False
            #print ("Exiting....")

