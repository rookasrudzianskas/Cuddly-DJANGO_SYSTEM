from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'base.html', {})


def new_searches(request):
    return render(request, 'my_app/new_searches.html', {})
