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
        choices = []
        widgets = { 'option' : forms.Select(choices = choices, attrs={'class':'form-control'})}

class single_int(ModelForm):
    class Meta:
        model = response
        fields = ['single']

class multi_option(ModelForm):
    class Meta:
        model = response
        fields = ['multi_option']
