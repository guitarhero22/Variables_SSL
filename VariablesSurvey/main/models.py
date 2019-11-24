from django.db import models
from django.contrib.auth.models import auth, User

class Form(models.Model):
    form_code = models.IntegerField(unique=True)
    form_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete='CASCADE')


    