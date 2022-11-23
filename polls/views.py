from django.http import HttpResponse


def index(request):
    return HttpResponse("<>Главная страница")


def products(request, name):
    return HttpResponse(f"Список товаров {name}")

