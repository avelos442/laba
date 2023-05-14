from django.shortcuts import render
from .models import Declaration


def home_view(request):
    qs = Declaration.objects.all()
    return render(request, 'scraping/home.html', {'object_list': qs})

