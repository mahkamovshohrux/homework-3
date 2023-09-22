from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CusUser2(AbstractUser):
    ChOICE_ROLSE = (
        (3, 'admin2'),
        (2,'staff2'),
        (1,'user')
    )
    rolse = models.PositiveIntegerField(choices=ChOICE_ROLSE,default=1)

    def __str__(self) -> str:
        return self.username