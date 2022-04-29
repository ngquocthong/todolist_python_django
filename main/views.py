from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewLists

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html",{"list": ls})

def base(response):
    return render(response, "main/base.html", {"name": "test"})

def home(response):
    return render(response, "main/home.html", {"name": "test"})

def create(response):
    if response.method == "POST":
        form = CreateNewLists(response.POST) # return as dictionary
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            print(n)
            t = ToDoList(name=n)
            t.save()
    else:
        form = CreateNewLists()
    return render(response, "main/create.html", {"form": form})    