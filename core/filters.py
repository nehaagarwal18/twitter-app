import django_filters
from .models import TweetMetadata


class TweetMetadataFilter(django_filters.FilterSet):
    retweet_count = django_filters.NumberFilter()
    retweet_count__gt = django_filters.NumberFilter(name='retweet_count', lookup_expr='gt')
    retweet_count__lt = django_filters.NumberFilter(name='retweet_count', lookup_expr='lt')

    favourite_count = django_filters.NumberFilter()
    favourite_count__gt = django_filters.NumberFilter(name='favourite_count', lookup_expr='gt')
    favourite_count__lt = django_filters.NumberFilter(name='favourite_count', lookup_expr='lt')

    follower_count = django_filters.NumberFilter()
    follower_count__gt = django_filters.NumberFilter(name='follower_count', lookup_expr='gt')
    follower_count__gt = django_filters.NumberFilter(name='follower_count', lookup_expr='lt')

    user_name = django_filters.CharFilter(lookup_expr='icontains')
    user_name = django_filters.CharFilter(lookup_expr='iexact')

    screen_name = django_filters.CharFilter(lookup_expr='icontains')
    screen_name = django_filters.CharFilter(lookup_expr='iexact')

    location = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='iexact')

    created_at = django_filters.DateRangeFilter(name='created_at',lookup_expr='lt')
    created_at = django_filters.DateRangeFilter(name='created_at', lookup_expr='gt')


    class Meta:
        model = TweetMetadata
        fields = ['created_at', 'retweet_count', 'favourite_count', 'follower_count', 'user_name', 'screen_name', 'location']