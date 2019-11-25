from django.forms import ModelForm
from models import question, option, response

class single(ModelForm):
    class Meta:
         model = response
         fields = ['single']

class para(ModelForm):
    class Meta:
        model = response
        fields = ['para']

class option(ModelForm):
    class Meta:
        model = response
        fields = ['option']

class single_int(ModelForm):
    class Meta:
        model = response
        fields = ['single']
