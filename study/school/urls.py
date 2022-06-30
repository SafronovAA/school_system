from django.urls import path
from .views import *
from django.urls import path, include
urlpatterns = [
    path('', LoginUser.as_view(),name='login'),
    path('hometask/',hometasks,name='hometask'),
    path('subject/',subjects),
    path('class/', classes),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/', LoginUser.as_view(),name='logout'),
    path('teacher/', teacher,name='teacher'),
    path('online/', hometasks,name='online'),
    path('addpost/', addpost,name='addpost'),
    path('addonline/', addonline,name='addonline'),
    path('check/', checktask,name='check'),
    path('checks/<int:post_id>/',makemark,name='ck'),
    path('subject/<int:sub_id>/',classes,name='subjects'),
    path('tasks/<int:class_id>/',schometask,name='tasks'),
    path('viewtask/<int:task_id>/',viewtask,name='view'),
    path('onlinetask/', onlinetask,name='onlinetask'),
    path('view/', viewtask2,name='viewtask')
]