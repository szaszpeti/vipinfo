from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    topic = models.CharField(max_length=250)
    topic_info = models.CharField(max_length=500)
    topic_logo = models.FileField()

    def __str__(self):
        return self.topic


class Document(models.Model):
    topic = models.ForeignKey(Category, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=250, default='')
    document_url = models.CharField(max_length=1000, default='')
    document_logo = models.FileField(null=True, blank=True)
    like = models.IntegerField(null=True, blank=True, default=0)
    dislike = models.IntegerField(null=True, blank=True, default=0)




    def __str__(self):
        return self.document_title