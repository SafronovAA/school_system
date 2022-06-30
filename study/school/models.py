from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
class Hometask(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    id_t=models.ForeignKey('Teacher',on_delete=models.PROTECT,null=True)
    id_sub=models.ForeignKey('Subject',on_delete=models.PROTECT,null=True)
    id_class=models.ForeignKey('Classes',on_delete=models.PROTECT,null=True)
    id_type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)
    file = models.FileField(upload_to='upload/% Y/% m/% d/', null=True)
    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('view', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name='Домашние задания'
        verbose_name_plural = 'Домашние задания'

class Teacher(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    surname=models.CharField(max_length=100,db_index=True)
    lastname=models.CharField(max_length=100,db_index=True)
    id_sub=models.ForeignKey('Subject',on_delete=models.PROTECT,null=True)
    phone = models.CharField(max_length=100, db_index=True)
    mail = models.CharField(max_length=100, db_index=True)
    viber=models.CharField(max_length=100,db_index=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name+' '+self.surname+' '+self.lastname

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'

class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'

class Check(models.Model):
    id_task = models.ForeignKey('Hometask', on_delete=models.PROTECT, null=True)
    id_student=models.ForeignKey('Student', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    file=models.FileField(upload_to ='uploads/% Y/% m/% d/', null=True)
    mark = models.IntegerField(null=True)
    comment=models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('ck',kwargs={'post_id':self.pk})

    class Meta:
        verbose_name = 'Выполненные задания'
        verbose_name_plural = 'Выполненные задания'

class Student(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    surname = models.CharField(max_length=100, db_index=True)
    lastname = models.CharField(max_length=100, db_index=True)
    id_class = models.ForeignKey('Classes', on_delete=models.PROTECT, null=True)
    phone = models.CharField(max_length=100, db_index=True)
    mail = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.lastname+' '+ self.id_class.name

    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'

class Subject(models.Model):
    name=models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subjects', kwargs={'sub_id': self.pk})

    class Meta:
        verbose_name = 'Предметы'
        verbose_name_plural = 'Предметы'

class Classes(models.Model):
    name=models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks', kwargs={'class_id': self.pk})

    class Meta:
        verbose_name = 'Классы'
        verbose_name_plural = 'Классы'