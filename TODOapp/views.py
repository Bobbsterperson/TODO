# TODOapp/views.py
from django.shortcuts import render, redirect
from .models import TODO
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TaskList(ListView):
    model = TODO
    context_object_name = 'todos'
   

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
    context_object_name = 'TODO'
    template_name = 'TODOapp/task_confirm_delete.html'
    success_url = reverse_lazy('TODOs')

# def add(request):
#     if request.method == 'POST':
#         if 'task' in request.POST:
#             task_text = request.POST.get('task')
#             TODO.objects.create(TODO=task_text)
#         elif 'mark_done' in request.POST:
#             completed_ids = request.POST.getlist('completed_tasks')
#             TODO.objects.filter(id__in=completed_ids).update(completed=True)
#         return redirect('home')

#     tasks = TODO.objects.filter(completed=False)
#     completed_tasks = TODO.objects.filter(completed=True)
#     return render(request, 'home.html', {'tasks': tasks, 'completed_tasks': completed_tasks})
