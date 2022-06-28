from django.db import models

# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='pictures')
    descp = models.TextField()

    def __str__(self):
        return self.name