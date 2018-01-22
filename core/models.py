from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class TweetMetadata(models.Model):
    """Contains all the metadata about the tweets extracted from the twitter streaming API"""
    tweet_id = models.BigIntegerField(unique=True)
    tweet_id_str = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    text = models.TextField()
    user_id = models.BigIntegerField(null=True, blank=True)
    user_id_str = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    screen_name = models.CharField(max_length=120, null=True, blank=True)
    location= models.CharField(max_length=120, null=True, blank=True)
    retweet_count = models.IntegerField(null=True, blank=True)
    favourite_count = models.IntegerField(null=True, blank=True)
    follower_count = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    coordinates = JSONField(null=True, blank=True)
    user_mentions = JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.tweet_id) + ' - ' + str(self.created_at) + ' - ' + str(self.user_name)

    class Meta:
        verbose_name = 'Tweet Metadata'
        verbose_name_plural = 'Tweets Metadata'
        db_table = 'tweet_metadata'

