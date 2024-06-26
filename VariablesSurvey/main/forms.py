from django.forms import ModelForm
from django import forms
from .models import question, option, response

class single(ModelForm):
    class Meta:
         model = response
         fields = ('single',)

class para(ModelForm):
    class Meta:
        model = response
        fields = ('para',)

class options(ModelForm):
    def __init__(self, choice, *args, **kwargs):
        super(waypointForm, self).__init__(*args, **kwargs)
        self.choices = choice

    class Meta:
        model = response
        fields = ('options',)
        choices = []
        widgets = { 'options' : forms.Select(choices = choices, attrs={'class':'form-control'})}

class single_int(ModelForm):
    class Meta:
        model = response
        fields = ('single',)

class multi_option(ModelForm):
    class Meta:
        model = response
        fields = ('multi_option',)
