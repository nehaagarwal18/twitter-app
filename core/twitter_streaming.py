import json

from tweepy import Stream
from tweepy.streaming import StreamListener
from django.http.response import HttpResponse

from .services import save_twitter_data, twitter_authentication


class TwitterListner(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        save_twitter_data(data)
        return HttpResponse(status=200)

    def on_error(self, status):
        return status


def tweet_streaming(stream_term):
    l = TwitterListner()
    auth = twitter_authentication()
    stream = Stream(auth, l)
    stream.filter(track=stream_term)