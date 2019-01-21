from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from backweb.models import Articles


def index(request):
    if request.method == 'GET':
        arts = Articles.objects.all()
        return render(request, 'web/index.html', {'arts':arts})


def share(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        arts = Articles.objects.all()
        paginator = Paginator(arts, 8)
        page = paginator.page(page)
        return render(request, 'web/share.html', {'page': page})


def list(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        arts = Articles.objects.all()
        paginator = Paginator(arts, 6)
        page = paginator.page(page)
        return render(request, 'web/list.html', {'page':page})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def infopic(request):
    if request.method == 'GET':
        return render(request, 'web/infopic.html')