from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Form
from django.db import models
from django.http import HttpResponse
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
				return render(request, 'build.html', {'form_name': form_name})
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
		form = Form.objects.filter(form_name=form_name, form_code=form_code, creator=creator, active=True)
		if not form.exists():
			messages.info(request, 'that is not possible with these credentials')
			return render(request, 'deactivate.html')
		else:
			for f in form:
				f.active = False
				f.save()
			return render(request, 'index.html')

	else:
		return render(request, 'deactivate.html')


def home(request):
    return render(request, 'index.html')


def respond(request):
	if request.method == 'POST':
		form_name = request.POST['form_name']
		form_code = request.POST['form_code']
		form = Form.objects.filter(form_name=form_name, form_code=form_code, active=True)
		if not form.exists():
			messages.info(request, 'Form is not accessible')
			return render(request, 'respond.html')
		else:
			for f in form:
				message = 'You are viewing '+f.form_name+' created by '+str(f.creator)
				messages.info(request, message)
				return render(request, 'answer.html')

	else:
		return render(request, 'respond.html')




def answer(request):
    pass

def build(request, form_name):
    return render(request, 'build.html', {'form_name':form_name})

def add_q(request, form_name, q_type):
    if request.method == 'GET':
        return render(request, 'add_q.html', {'form_name':form_name, 'q_type':q_type})
    else:
        return redirect(request, 'build/form_name')
