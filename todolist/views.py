from audioop import reverse
import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Task
from django.urls import reverse_lazy


# Create your views here.

class CustomLoginView(LoginView):
    template_name='todolist/login.html'
    field='__all__'
    redirect_authenticated_user: True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
   model=Task
   context_object_name='tasks'

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name="task"

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields="__all__"
    template_name = 'todolist/task_form.html'
    success_url=reverse_lazy("tasks")

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields="__all__"
    success_url=reverse_lazy("tasks")

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="task"
    success_url=reverse_lazy("tasks")
