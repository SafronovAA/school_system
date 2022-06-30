from urllib import request

from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    id_type = forms.ModelChoiceField(queryset=Type.objects.filter(id=1))
    class Meta:

        model = Hometask
        labels={
            "title":"Заголовок",
            "content":"Описание",
            "id_t":"Учитель",
            "id_sub":"Предмет",
            "id_type": "Тип",
            "id_class":"Класс",
            "file": "Файл"

        }
        fields = ['title', 'content', 'id_t', 'id_sub', 'id_class', 'id_type', 'file']
        widgets={
            'title':forms.Textarea(attrs={'rows':2})
        }
        #id_type = forms.ModelChoiceField(queryset=Type.objects.get(id_type=2))

class AddOnline(forms.ModelForm):
    id_type = forms.ModelChoiceField(queryset=Type.objects.filter(id=2))
    class Meta:
        model = Hometask
        labels = {
            "title": "Заголовок",
            "content": "Описание",
            "id_t": "Учитель",
            "id_sub": "Предмет",
            "id_type": "Тип",
            "id_class": "Класс",
            "file": "Файл"


        }
        fields = ['title', 'content', 'id_t', 'id_sub', 'id_class','id_type','file']
        widgets = {
            'title': forms.Textarea(attrs={'rows': 2})
        }


            #title = forms.CharField(max_length=255)
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    #id_t = forms.ModelChoiceField(queryset=Teacher.objects.filter(id=1))
    #id_sub = forms.ModelChoiceField(queryset=Subject.objects.all())
    #id_class = forms.ModelChoiceField(queryset=Classes.objects.all())