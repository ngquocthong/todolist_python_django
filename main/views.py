from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewLists

# Create your views here.
#{"save": ["save"], "c1":["clicked"]}
def index(response, id):    
    ls = ToDoList.objects.get(id=id)
    if response.method=="POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) =="clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
            
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if(len(txt)>2):
                ls.item_set.create(text=txt, complete=False)
            else: 
                print("invalid value")
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
        return HttpResponseRedirect("/%a" %t.id)
    else:
        form = CreateNewLists()
    return render(response, "main/create.html", {"form": form})    