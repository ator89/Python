from django import forms
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []#if user doesn't have a list of tasks, provide empty list
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":#check request method is POST
        form = NewTaskForm(request.POST)#store all submitted data
        if form.is_valid(): #check if data is valid
            task = form.cleaned_data["task"]#if it's valid, add the task to tasks
            #tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()#if new access, just provide empty form
    })