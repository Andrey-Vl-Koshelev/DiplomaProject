from django.db import models

class Web(models.Model):
    image = models.ImageField(upload_to='web/images/')
