from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    form_class = StudentForm
    template_name = 'curd_app/student_form.html'


@method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student
    template_name = 'curd_app/student_form.html'
    success_url = reverse_lazy('retrieve_url')


@method_decorator(login_required, name='dispatch')
class StudentRetrieve(ListView):
    model = Student


@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('retrieve_url')


@method_decorator(login_required, name='dispatch')
class StudentDelete(DeleteView):
    model = Student
    template_name = 'curd_app/student_confirm.html'
    success_url = reverse_lazy('retrieve_url')


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'curd_app/signup.html'
    success_url = reverse_lazy('login_url')


