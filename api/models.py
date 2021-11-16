from django.db import models


# Create your models here.

class UserSaver(models.Model):

    user_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default="")
    previous_search = models.CharField(max_length=255)


class Anime(models.Model):

    title = models.CharField(max_length=250)
    anime_id = models.CharField(max_length=20)
    image = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    weight = models.CharField(max_length=2, default="")

    """
    def search_anime(anime_title):
        #anime.animes(anime_title); #myanimelist api call
        return 0

    
    def recommendation_algorithm():
        return 0"""
