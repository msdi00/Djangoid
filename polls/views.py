from django.shortcuts import render


def index(request):
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    return render(request, "index.html", context={"langs": langs})