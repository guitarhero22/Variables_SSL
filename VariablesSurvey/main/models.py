from django.db import models
from django.contrib.auth.models import auth, User

class Form(models.Model):
    form_code = models.CharField(max_length=50)
    form_name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete='CASCADE')


    