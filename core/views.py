import tweepy
import csv
import logging
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.shortcuts import render
from .filters import TweetMetadataFilter
from .services import save_twitter_data, twitter_authentication
from .twitter_streaming import tweet_streaming
from .models import TweetMetadata

logger = logging.getLogger(__name__)


@api_view(['GET', ])
def get_streaming_data(request, stream_term):
    try:
        stream_term = list(stream_term)
        tweet_streaming(stream_term)
        return HttpResponse(status=200)
    except Exception as e:
        logger.error(e)
        return HttpResponse(status=400)


@api_view(['GET', ])
def get_search_data(request, query, max_tweets):
    try:
        auth = twitter_authentication()
        api = tweepy.API(auth)
        search_results = api.search(q=query, count=max_tweets)
        for result in search_results:
            data = result._json
            save_twitter_data(data)
        return HttpResponse(status=200)
    except Exception as e:
        logger.error(e)
        return HttpResponse(status=400)


@api_view(['GET', ])
def search_sort_data(request, attribute_searched, search_term, text_sort, date_sort):
    try:
        if attribute_searched == 'text':
            tweet_metadata_objects = TweetMetadata.objects.filter(text__contains=search_term)
        if attribute_searched == 'user':
            tweet_metadata_objects = TweetMetadata.objects.filter(user_name__contains=search_term)
        if text_sort == 'asc' and date_sort == 'asc':
            results = tweet_metadata_objects.order_by('text').order_by('created_at')
        if text_sort == 'desc' and date_sort == 'desc':
            results = tweet_metadata_objects.order_by('-text').order_by('-created_at')
        if text_sort == 'asc' and date_sort == 'desc':
            results = tweet_metadata_objects.order_by('text').order_by('-created_at')
        if text_sort == 'desc' and date_sort == 'asc':
            results = tweet_metadata_objects.order_by('-text').order_by('created_at')
        return HttpResponse(results)
    except Exception as e:
        logger.error(e)
        return HttpResponse(status=400)


@api_view(['GET', ])
def tweet_metadata_list(request):
    try:
        f = TweetMetadataFilter(request.GET, queryset=TweetMetadata.objects.all())
        if 'exportcsv' in request.GET:
            output = []
            response = HttpResponse(content_type='text/csv')
            writer = csv.writer(response)
            writer.writerow(['Created At', 'Screen Name', 'User Name', 'Text', 'Retweet Count', 'Followers Count', 'Favourite Count'])
            for item in f.qs:
                output.append([item.created_at, item.screen_name, item.user_name, item.text,
                               item.retweet_count, item.follower_count, item.favourite_count])
            writer.writerows(output)
            return response
        return render(request, 'filters.html', {'filter': f})
    except Exception as e:
        logger.error(e)
        return HttpResponse(status=400)





