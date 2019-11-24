from django.db import models
from django.contrib.auth.models import auth, User

class Form(models.Model):
    form_code = models.CharField(max_length=50)
    form_name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete='CASCADE')

class question(models.Model):
    form_id = models.ForeignKey(Form, on_delete='CASCADE')
    q_type = models.CharField(max_length = 50)
    d_type = models.CharField(max_length = 50)
    # options = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    content = models.TextField(null=False)
    order = models.IntegerField()
    max_length = models.IntegerField()

class option(models.Model):
    q_id = models.ForeignKey(question, on_delete='CASCADE')
    opt_content = models.CharField(max_length = 100)
    opt_type = models.CharField(max_length = 50)
    opt_order = models.IntegerField()

#
# class single(question):
#     pass
#
# class paragraph(question):
#     pass
#
# class radio(question):
#     pass
#
# class check(question):
#     pass
#
# class dropdwn(question):
#     pass
#
# class toggle(question):
#     pass
#
# class scale(question):
#     pass
