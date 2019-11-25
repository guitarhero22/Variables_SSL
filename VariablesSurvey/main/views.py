from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Form, question, option
from django.db import models
from django.http import HttpResponse
from .forms import *
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
				return redirect('answer')

	else:
		return render(request, 'respond.html')




def answer(request, form_name):
    if not request.user.is_authenticated:
        return redirect('login')

    form = Form.objects.get(form_name=form_name)
    form_list = []
    question_set = question.objects.filter(form_id=form).order_by('order')
    num = question.objects.filter(form_id=form).count()
    option_set = []
    for q in question_set:
        opt = option.objects.filter(q_id=q)
        option_set += [(q, opt)]

    return render(request, 'answer.html',  {'tuple' : option_set})

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

        if q_type == 'paragraph':
            content = request.POST['content']
            max_length = request.POST['max_length']

            if content == "" or max_length == "":
                messages.info(request, 'please fill all the fields')
                return redirect('/add_q/'+form_name+'/'+q_type)

            order = 1 + question.objects.filter(form_id = form.id).count()
            quest = question(form_id = form, q_type = q_type, d_type = "text", visible = True, content=content, max_length=int(max_length), order = order)
            quest.save()

        if q_type == 'radio' or q_type == 'check' or q_type == 'dropdwn':
            content = request.POST['content']

            if content == "":
                messages.info(request, 'please fill all the fields')
                return redirect('/add_q/' + form_name + '/' + q_type)

            order = 1 + question.objects.filter(form_id = form.id).count()
            quest = question(form_id = form, q_type = q_type, d_type = "text", visible = True, content=content, max_length=0, order = order)
            quest.save()
            caller = question.objects.get(order=order,form_id=form)
            qid = str(caller.id)

            return redirect('/add_opt/' + qid + '/' + q_type + '/')

        return redirect('/build/' + form_name)

def add_opt(request, q_id, opt_type):
    if not request.user.is_authenticated:
        return redirect('login')

    questio = question.objects.get(id=q_id)
    if not questio.form_id.creator == request.user:
        return HttpResponse('Cannot edit this form sorry')
    opts = option.objects.filter(q_id=questio)

    if request.method == 'GET':
        return render(request, 'add_opt.html', {'q_id': q_id, 'opt_type': opt_type , 'form_name': questio.form_id.form_name, 'options' : opts})
    else:
        opt_content = request.POST['content']
        q_id = int(q_id)
        order = 1+ option.objects.filter(q_id=questio).count()
        optio = option(q_id=questio, opt_content=opt_content, opt_type=opt_type, opt_order=order)
        optio.save()
        return redirect('/add_opt/'+str(q_id)+'/'+opt_type+'/')
