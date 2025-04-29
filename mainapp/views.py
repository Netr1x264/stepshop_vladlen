from django.shortcuts import render

def index(request):
    title = 'Главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
