from django.http import Http404
from django.shortcuts import render

from myapp.models import Program
from myapp.models import Session

def index(request):
    latest_program_list = Program.objects.order_by('-create_date')[:5]
    context = {'latest_program_list':latest_program_list}
    return render(request, 'myapp/index.html', context)    

def program(request, program_id):
    try:
        program = Program.objects.get(pk=program_id)
        program_sessions_list = Session.objects.filter(program__id=program_id).order_by('start_date')
        context = {'program_sessions_list':program_sessions_list,'program':program}
        #context = {'program':program}
    except Program.DoesNotExist:
        raise Http404("Program does not exist")
    return render(request, 'myapp/program.html', context)

def session(request, session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        raise Http404("Session does not exist")
    return render(request, 'myapp/session.html', {'session':session})
