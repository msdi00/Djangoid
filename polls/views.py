from django.shortcuts import render, HttpResponse
from .forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, "index.html", {"form": userform})

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")