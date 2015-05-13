import os

from django.http import Http404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from myapp.forms import RegisterForm
from myapp.models import Program
from myapp.models import Session
from myapp.models import Customer
from myapp.models import Registration

def index(request):
    latest_program_list = Program.objects.order_by('-create_date')[:5]
    path="myapp/static"
    img_list = os.listdir(path)
    context = {'latest_program_list':latest_program_list, 'images':img_list}
    return render(request, 'myapp/index.html', context)

def program(request, program_id):
    try:
        program = Program.objects.get(pk=program_id)
        program_sessions_list = Session.objects.filter(program__id=program_id).order_by('start_date')
        context = {'program_sessions_list':program_sessions_list,'program':program}
    except Program.DoesNotExist:
        raise Http404("Program does not exist")
    return render(request, 'myapp/program.html', context)

def session(request, session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        raise Http404("Session does not exist")
    return render(request, 'myapp/session.html', {'session':session})

def selectProgram(request):
    available_programs_list = Program.objects.order_by('title')
    context = {'available_programs_list':available_programs_list}
    return render(request, 'myapp/selectProgram.html', context)

def register_session(request, session_id):
    try:
        session = Session.objects.get(pk=session_id)
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                customer = form.save()
                registration = Registration.objects.create(customer=customer, session=session)
                #return HttpResponseRedirect('/player/%s', customer.id)
                body='%s %s has been registered in %s' % (customer.firstname, customer.lastname, session.title)
                to=customer.email
                send_mail('Confirmation for RT Hockey Registration', body, settings.EMAIL_HOST_USER, [to], fail_silently=False)
                return render(request, 'myapp/player.html', {'customer' : customer})
        else:
            form = RegisterForm()
    except Session.DoesNotExist:
        raise Http404("Session does not exist")
    return render(request, 'myapp/register_session.html', {'session':session, 'form':form})

def register_program(request, program_id):
    try:
        program = Program.objects.get(pk=program_id)
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                customer = form.save()
                registration = Registration.objects.create(customer=customer, program=program)
                #return HttpResponseRedirect('/player/%s', customer.id)
                body='%s %s has been registered in %s' % (customer.firstname, customer.lastname, program.title)
                to=customer.email
                send_mail('Confirmation for RT Hockey Registration', body, settings.EMAIL_HOST_USER, [to], fail_silently=False)
                return render(request, 'myapp/player.html', {'customer' : customer})
        else:
            form = RegisterForm()
    except Program.DoesNotExist:
        raise Http404("Program does not exist")
    return render(request, 'myapp/register_program.html', {'program':program, 'form':form})

def gallery(request):
    return render(request, 'myapp/gallery.html')

def contact(request):
    return render(request, 'myapp/contact.html')

#def about(request):
#    return render(request, 'myapp/about.html')

def player(request):
    if request.method == 'POST':
        customer = request.session.get('customer', None)
        return render(request, 'myapp/player.html', {'customer' : customer})
