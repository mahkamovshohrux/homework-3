from django.db import models

# Create your models here.
class Nmodel(models.Model):
    title = models.CharField(max_length=40, default="")
    body = models.CharField(max_length=50,default='')
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
