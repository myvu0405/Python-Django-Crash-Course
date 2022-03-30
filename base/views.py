# from django.http import HttpResponse
# from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

# from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

from .models import Task

# Create your views here.

# def taskList(request):

#     return HttpResponse('TO DO LIST')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(isCompleted=False).count()

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            # context['tasks']=context['tasks'].filter(title__icontains=search_input)
            context['tasks']=context['tasks'].filter(title__startswith=search_input)

        context['search_input']=search_input

        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name= 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    # fields= '__all__'
    fields=['title','description','isCompleted']
    success_url= reverse_lazy('tasks')

    def form_valid(self, form):

        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    # fields= '__all__'
    fields=['title','description','isCompleted']
    success_url= reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')
