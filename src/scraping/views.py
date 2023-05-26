from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import FindForm
from .models import Declaration


def home_view(request):
    form = FindForm
    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    form = FindForm
    city = request.GET.get('city')
    metro = request.GET.get('metro')
    context = {'city': city, 'metro': metro, 'form': form}
    if city or metro:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if metro:
            _filter['metro__slug'] = metro

        qs = Declaration.objects.filter(**_filter)
        paginator = Paginator(qs, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)
