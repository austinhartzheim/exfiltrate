from django.db import models

# Create your models here.
class Group(models.Model):
    title = models.CharField(max_length=50)

class UploadedFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='/tmp/', blank=True, null=True)
    
    # Privacy settings
    group = models.ForeignKey('Group', default=None, null=True)
    private = models.BooleanField(default=False)
