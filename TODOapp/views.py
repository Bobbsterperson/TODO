# TODOapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TODO
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TaskList(ListView):
    model = TODO
    context_object_name = 'todos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomplete_tasks'] = TODO.objects.filter(completed=False)
        context['completed_tasks'] = TODO.objects.filter(completed=True)
        return context

   

class TaskDetail(DetailView):
    model = TODO
    context_object_name = 'TODO'
    template_name = 'TODOapp/task_detail.html'


class TaskCreate(CreateView):
    model = TODO
    fields = '__all__'
    template_name = 'TODOapp/task_form.html'
    success_url = reverse_lazy('TODOs')


class TaskUpdate(UpdateView):
    model = TODO
    fields = '__all__'
    template_name = 'TODOapp/task_form.html'
    success_url = reverse_lazy('TODOs')


class DeleteView(DeleteView):
    model = TODO
    context_object_name = 'title'
    template_name = 'TODOapp/task_confirm_delete.html'
    success_url = reverse_lazy('TODOs')


def mark_complete(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    task.completed = True
    task.save()
    return redirect('TODOs')

def mark_incomplete(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    task.completed = False
    task.save()
    return redirect('TODOs')
