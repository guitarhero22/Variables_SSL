from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Form, question
from django.db import models
from django.http import HttpResponse
# Create your views here.


def create(request):
	if not request.user.is_authenticated:
		return redirect('home')

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
	if not request.user.is_authenticated:
		return redirect('home')

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
	if not request.user.is_authenticated:
		return redirect('home')

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
    if not request.user.is_authenticated:
        return redirect('login')

    form = Form.objects.get(form_name=form_name)
    if not form.creator == request.user:
        return HttpResponse('Cannot Edit This Form, Sorry ;-(')

    quest = question.objects.filter(form_id=form.id).order_by('order')
    return render(request, 'build.html', {'form_name':form_name, 'questions' : quest})

def add_q(request, form_name, q_type):
    if not request.user.is_authenticated:
        return redirect('login')

    form = Form.objects.get(form_name=form_name)
    if not form.creator == request.user:
        return HttpResponse('Cannot Edit This Form, Sorry ;-(')

    if request.method == 'GET':
        return render(request, 'add_q.html', {'form_name':form_name, 'q_type':q_type})
    else:
        form = Form.objects.get(form_name = form_name)
        
        if q_type == 'single':
            content = request.POST['content']
            max_length = request.POST['max_length']
            d_type = request.POST['d_type']

            if content == "" or max_length == "":
                messages.info(request, 'please fill all the fields')
                return redirect('/add_q/' + form_name + '/' + q_type)

            order = 1 + question.objects.filter(form_id = form.id).count()
            quest = question(form_id = form, q_type = q_type, d_type = d_type, visible = True, content=content, max_length=int(max_length), order = order)
            quest.save()

        return redirect('/build/' + form_name)

        if q_type == 'paragraph':
            content = request.POST['content']
            max_length = request.POST['max_length']

			if content == "" or max_length == "":
				messages.info(request, 'please fill all the fields')
				return redirect('add_q/'+form_name+'/'+q_type)	
				

            order = 1 + question.objects.filter(form_id = form.id).count()
            quest = question(form_id = form, q_type = q_type, d_type = "text", visible = True, content=content, max_length=int(max_length), order = order)
            quest.save()

        if q_type == radio:
            content = request.POST['content']
			
			if content == "":
                messages.info(request, 'please fill all the fields')
                return redirect('/add_q/' + form_name + '/' + q_type)

            order = 1 + question.objects.filter(form_id = form.id).count()
            quest = question(form_id = form, q_type = q_type, d_type = "text", visible = True, content=content, max_length=int(max_length), order = order)
            quest.save()


def add_opt(request, q_id, opt_name):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        return render(request, 'add_opt.html', {'q_id': q_id, 'opt_type': opt_type})
    else:
        pass
