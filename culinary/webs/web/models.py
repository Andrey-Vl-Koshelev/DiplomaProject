from django.db import models

class Web(models.Model):
    image = models.ImageField(upload_to='web/images/',null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name