from django.shortcuts import render

from .forms import FindForm
from .models import Declaration


def home_view(request):
    #print(request.GET)
    form = FindForm
    city = request.GET.get('city')
    metro = request.GET.get('metro')
    qs = []
    if city or metro:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if metro:
            _filter['metro__slug'] = metro

        qs = Declaration.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs,
                                                  'form': form})

