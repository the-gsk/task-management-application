from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

login_url = '/accounts/login/'

def user_logout(request):
    logout(request)
    return redirect('login')

class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_manager/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'task_manager/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'task_manager/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.assignee = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_manager/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.assignee == request.user:
            task.delete()
        return redirect('task_list')
            

