from django.db import models
from django.conf import settings

class Document(models.Model):
    file = models.FileField(upload_to='../media/downloads')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # model is not returning title of doc in view
    def __unicode__(self):
         return self.name

class Json_Model(models.Model):
    files = models.FilePathField(path=settings.MEDIA_ROOT + '/downloads/', match=".*\.csv$")
    comments = models.PositiveIntegerField()
    topics = models.PositiveIntegerField()
    iterations = models.PositiveIntegerField()
