from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.models import Articles, Com


# from web.models import Comment


def index(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        arts = Articles.objects.all()[::-1]
        paginator = Paginator(arts, 5)
        page = paginator.page(page)
        com = Com.objects.all()[::-1]
        a = Articles.objects.all()
        return render(request, 'web/index.html', {'page': page, 'comm': com, 'a': a})


def view(request):
    if request.method == 'GET':
        return render(request, 'web/view.html')


def article(request, id):
    if request.method == 'GET':
        arts = Articles.objects.filter(pk=id).first()
        com = Com.objects.all()[::-1]
        a = Articles.objects.all()
        art = True
        return render(request, 'web/index.html', {'art': art, 'arts': arts, 'comm': com, 'a': a})


def comment(request):
    if request.method == 'GET':
        flag = True
        return render(request, 'web/index.html', {'flag': flag})
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Com.objects.create(com=comment)
        return HttpResponseRedirect(reverse('web:index'))

# def new(request):
#     if request.method == 'GET':
#         page = int(request.GET.get('page', 1))
#         arts = Articles.objects.all()
#         paginator = Paginator(arts, 8)
#         page = paginator.page(page)
#         return render(request, 'web/new.html', {'page': page})
#
#
# def newlist(request):
#     if request.method == 'GET':
#         page = int(request.GET.get('page', 1))
#         arts = Articles.objects.all()
#         paginator = Paginator(arts, 6)
#         page = paginator.page(page)
#         return render(request, 'web/newlist.html', {'page':page})
#
#
# def about(request):
#     if request.method == 'GET':
#         return render(request, 'web/about.html')


# def infopic(request):
#     if request.method == 'GET':
#         return render(request, 'web/infopic.html')
