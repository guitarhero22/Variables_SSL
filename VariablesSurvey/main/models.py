from django.db import models
from django.contrib.auth.models import auth, User

class Form(models.Model):
    form_code = models.CharField(max_length=50)
    form_name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete='CASCADE')

class question(models.Model):
    # form_id = models.ForeignKey(Form, on_delete='CASCADE')
    q_type = models.CharField(max_length = 50)
    d_type = models.CharField(max_length = 50)
    options = models.BooleanField()
    visible = models.BooleanField()
    content = models.TextField()
    choices = models.TextField()
