from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout


def user_logout(request):
    """
    Log out the current user and redirect to the login page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponseRedirect: Redirects to the login page.
    """
    logout(request)
    return redirect('login')

class UserRegistrationView(CreateView):
    """
    View for user registration.

    Allows new users to create accounts with the provided information.
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class TaskListView(LoginRequiredMixin, ListView):
    """
    View for listing tasks assigned to the authenticated user.

    Displays a list of tasks assigned to the logged-in user.
    """
    model = Task
    template_name = 'task_manager/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        """
        Retrieve tasks assigned to the current user.

        Returns:
            QuerySet: Tasks assigned to the current user.
        """
        return Task.objects.filter(assignee=self.request.user)

class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying the details of a task.

    Displays detailed information about a specific task.
    """
    model = Task
    template_name = 'task_manager/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new task.

    Allows users to create new tasks and assigns them to the current user.
    """
    model = Task
    template_name = 'task_manager/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        """
        Save the newly created task, assigning it to the current user.

        Args:
            form (TaskForm): The form containing task data.

        Returns:
            HttpResponseRedirect: Redirects to the task list page.
        """
        form.instance.assignee = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing task.

    Allows users to edit and update the details of an existing task.
    """
    model = Task
    template_name = 'task_manager/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, View):
    """
    View for deleting a task.

    Allows users to delete a task if they are the assignee.
    """
    def get(self, request, pk):
        """
        Delete the task if the current user is the assignee.

        Args:
            request (HttpRequest): The incoming HTTP request.
            pk (int): The primary key of the task to delete.

        Returns:
            HttpResponseRedirect: Redirects to the task list page.
        """
        task = get_object_or_404(Task, pk=pk)
        if task.assignee == request.user:
            task.delete()
        return redirect('task_list')

            

