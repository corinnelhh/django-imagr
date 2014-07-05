from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ImagrUser(User):

    follows = models.ManyToManyField('self')
   # followed

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.username


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(ImagrUser)
    date_uploaded = models.DateTimeField('date uploaded', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
    date_published = models.DateTimeField(
        'date published', blank=True, auto_now=True
    )
    access_level = models.IntegerField(choices=(('private', 0), ('public', 1)))

    def __unicode__(self):
        return self.title


class Album(models.Model):
    owner = models.ForeignKey(ImagrUser)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
    date_published = models.DateTimeField(
        'date published', blank=True, auto_now=True
    )
    access_level = models.IntegerField(choices=(('private', 0), ('public', 1)))
    photos = models.ManyToManyField(Photo)
    cover_photo = models.ForeignKey(
        Photo, limit_choices_to=(Photo.objects.filter(access_level=1))
    )

    # def get_photos(self):

    #     return self.photos

    def __unicode__(self):
        return self.title
