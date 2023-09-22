from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CusUser5(AbstractUser):
    CHOICE_ROLES = (
        (3, 'admin5'),
        (2,'staff5'),
        (1,'user5')
    )
    roles = models.PositiveIntegerField(choices=CHOICE_ROLES,default=1)

    def __str__(self) -> str:
        return self.username