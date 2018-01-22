"""twitter_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path
from .views import get_streaming_data, get_search_data, search_sort_data, \
    tweet_metadata_list

urlpatterns = [
    path('tweet-stream/<stream_term>', get_streaming_data),
    path('tweet-search/<query>/<int:max_tweets>', get_search_data),
    path('tweet-search-sort/<attribute_searched>/<search_term>/<text_sort>/<date_sort>',
         search_sort_data),
    path('list-tweets', tweet_metadata_list),
]
