from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'base.html', {})


def new_searches(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/new_searches.html', stuff_for_frontend)
