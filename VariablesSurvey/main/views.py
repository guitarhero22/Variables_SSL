from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Form

# Create your views here.


def create(request):
	if request.method == 'POST':
		creator = request.user
		form_name = request.POST['form_name']
		form_code = request.POST['form_code']
		if form_name == "" or form_code == "":
			messages.info(request, 'make sure you enter all fields')
			return render(request, 'create.html')
		else:
			try:
				form = Form(form_code=form_code, form_name=form_name, creator=creator)
				form.save()
				return render(request, 'index.html')
			except IntegrityError as e:
				messages.info(request, 'try another unique name')
				return render(request, 'create.html')

	else:
		return render(request, 'create.html')
			


def deactivate(request):
	if request.method == 'POST':
		form_name = request.POST['form_name']
		form_code = request.POST['form_code']
		creator = request.user


def home(request):
    return render(request, 'index.html')


def respond(request):
    pass


def answer(request):
    pass
