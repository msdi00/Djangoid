from django.http import HttpResponse


def index(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")




def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)


def contact(request):
    return HttpResponse("Контакты")
