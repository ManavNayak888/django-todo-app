from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View

from django.contrib import messages

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('created')


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task created successfully.")
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully.")
        return super().form_valid(form)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect('task-list')


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {'form': form}) 

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created and logged in!")
            return redirect('task-list')
        return render(request, 'registration/signup.html', {'form': form})


def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    if task.complete:
        messages.success(request, "Task marked as complete.")
    else:
        messages.info(request, "Task marked as incomplete.")
    return redirect('task-list')



