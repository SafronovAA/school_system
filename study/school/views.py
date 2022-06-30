from datetime import datetime

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy

from .forms import AddPostForm, AddOnline
from .models import *
from .utils import DataMixin
sub=1
clasii=2
task=1
menu = ["Моя страница","Выйти",]
def home(request):


    #teachers = Teachers.objects.all()
    return render(request,'school/base.html')
def hometasks(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
        'menu': menu,

    }
    #teachers = Teachers.objects.all()
    return render(request,'school/index.html',{'subject':subject,'menu':menu})
def classes(request,sub_id):
    global sub
    sub=sub_id
    clases = Classes.objects.all()
    context = {
        'clases': clases,
        'menu': menu,
        'sub':sub

    }

    return render(request,'school/clases.html',{'clases':clases,'menu':menu,'sub_id':sub_id,'sub':sub})
def schometask(request,class_id):
    global clasii
    clasii=class_id

    tasks = Hometask.objects.filter(id_class=class_id,id_sub=sub,id_type=1)

    context = {
        'tasks': tasks,
        'menu': menu

    }

    return render(request,'school/hometask.html',{'tasks':tasks,'menu':menu,'sub':sub,'clasii':clasii})

def login(request):

    user = Teacher.objects.all()

    context = {
        'user': user,
        'menu': menu

    }

    return render(request,'school/checklogin.html',{'user':user,'menu':menu})

def onlinetask(request,class_id):
    global clasii
    clasii=class_id

    tasks = Hometask.objects.filter(id_class=class_id,id_sub=sub,id_type=2)

    context = {
        'tasks': tasks,
        'menu': menu

    }

    return render(request,'school/hometask.html',{'tasks':tasks,'menu':menu,'sub':sub,'clasii':clasii})

def viewtask(request,task_id):
    global task
    task=task_id
    tasks = Hometask.objects.filter(id=task_id)

    context = {
        'tasks': tasks,
        'menu': menu

    }

    return render(request,'school/viewtask.html',{'tasks':tasks,'menu':menu,'task':task})



def online(request):
    posts = Hometask.objects.all()

    #teachers = Teachers.objects.all()
    return render(request,'school/online.html',{'posts':posts,'menu':menu})

def subjects(request):
    return HttpResponse("<h1>Страница предметов</h1>")



def teacher(request):


    #teachers = Teachers.objects.all()
    return render(request,'school/teacher.html')

def checktask(request):
    current_user = request.user


    z=Check.objects.all()


    return render(request, 'school/checktask.html', {'tasks': z})

def viewtask2(request):
    current_user = request.user
    stud=Student.objects.get(author=current_user)

    z=Check.objects.filter(id_student=stud)
    return render(request, 'school/madetask.html', {'viewtask': z})



def makemark(request,post_id):
    check = Check.objects.get(id=post_id)
    if request.method == "POST":
        check.mark = request.POST.get("mark")
        check.comment = request.POST.get("comment")

        check.save()
    return render(request, 'school/edit.html', {'check': check})





def addpost(request):
    if request.method=='POST':

        form = AddPostForm(request.POST)

        if form.is_valid():
            try:


                form.save()
                form.add_error(None, 'Успешно добавлено')
            except:
                form.add_error(None,'Не удалось добавить, проверьте корректность данных')

    else:
        form = AddPostForm()

    return render(request, 'school/addpost.html',{'form':form})

def addonline(request):
    if request.method=='POST':

        form = AddOnline(request.POST)
        if form.is_valid():
            try:


                form.save()
                form.add_error(None, 'Успешно добавлено')
            except:
                form.add_error(None,'Не удалось добавить, проверьте корректность данных')

    else:
        form = AddOnline()

    return render(request, 'school/addonline.html',{'form':form})

class LoginUser(DataMixin,LoginView):
    form_class = AuthenticationForm
    template_name = 'school/login.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))
