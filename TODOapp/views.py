from django.shortcuts import render, redirect
from .models import TODO

def add(request):
    if request.method == 'POST':
        task_description = request.POST.get('task')
        if task_description:
            # Save the task to the database
            TODO.objects.create(TODO=task_description)
            return redirect('home')  # Redirect to the home page after saving the task

    # Fetch all tasks from the database
    tasks = TODO.objects.all()
    return render(request, 'home.html', {'tasks': tasks})