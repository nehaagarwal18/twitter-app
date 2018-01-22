import time

from django.conf import settings
from tweepy import OAuthHandler

from .models import TweetMetadata


def twitter_authentication():
    auth = OAuthHandler(settings.API_KEY, settings.API_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    return auth


def save_twitter_data(data):
    screen_name = data['user']['screen_name']
    user_name = data['user']['name']
    user_id = data['user']['id']
    user_id_str = data['user']['id_str']
    TweetMetadata.objects.get_or_create(retweet_count=data.get('retweet_count'),
                                        favourite_count=data.get('favorite_count'),
                                        tweet_id_str=data.get('id_str'),
                                        language=data.get('lang'),
                                        text=data.get('text'),
                                        tweet_id=data.get('id'),
                                        created_at=time.strftime('%Y-%m-%d %H:%M:%S',
                                                                  time.strptime(data.get('created_at'),
                                                                                '%a %b %d %H:%M:%S +0000 %Y')),
                                        screen_name=screen_name,
                                        user_name=user_name,
                                        user_id=user_id,
                                        user_id_str=user_id_str)