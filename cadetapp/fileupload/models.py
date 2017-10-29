from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='../media/downloads')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # model is not returning title of doc in view
    def __unicode__(self):
         return self.name
