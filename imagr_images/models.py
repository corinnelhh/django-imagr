from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    date_uploaded = models.DateTimeField('date uploaded')
    date_modified = models.DateTimeField('date modified')
    date_published = models.DateTimeField('date published')
    access_level = models.IntegerField(choices=(('private', 0), ('public', 1)))


class Album(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField('date created')
    date_modified = models.DateTimeField('date modified')
    date_published = models.DateTimeField('date published')
    access_level = models.IntegerField(choices=(('private', 0), ('public', 1)))
    photos = models.ManyToManyField(Photo)
    cover_photo = models.ImageField(upload_to='photos/%Y/%m/%d')


class Site_User(models.Model):
    user = models.OneToOneField(User)
    following = models.ManyToManyField('self', related_name="follows", symmetrical=False)
    date_joined = models.DateTimeField('date joined')
    status = models.IntegerField(choices=(('active', 0), ('inactive', 1)))
