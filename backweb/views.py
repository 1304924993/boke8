from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from backweb.form import AddArtForm, EddArtForm
from backweb.models import User, Articles, Column
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        password2 = request.POST.get('userpwd2')
        user = User.objects.filter(username=username).exists()
        if user:
            error = '该用户已注册过'
            return render(request, 'backweb/register.html', {'error': error})
        if password != password2:
            error = '密码不一致'
            return render(request, 'backweb/register.html', {'error': error})
        password = make_password(password)
        User.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('backweb:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(username=username).first()
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('backweb:index'))
        else:
            error = '账号或密码错误'
            return render(request, 'backweb/login.html', {'error': error})


def index(request):
    if request.method == 'GET':
        user = request.session['user_id']
        user = User.objects.filter(id=user)
        art = Articles.objects.all()
        return render(request, 'backweb/index.html',{'art':art, 'user':user})


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Articles.objects.all()[::-1]
        paginator = Paginator(articles, 3)
        page = paginator.page(page)
        return render(request, 'backweb/article.html', {'page':page})


def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Articles.objects.create(title=title, desc=desc, content=content, icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            form = form.errors
            return render(request, 'backweb/add_article.html', {'form':form})


def update_article(request, id):
    if request.method == 'GET':
        art = Articles.objects.filter(pk=id).first()
        return render(request, 'backweb/update_article.html', {'art':art})
    if request.method == 'POST':
        form = EddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Articles.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            form = form.errors
            return render(request, 'backweb/update_article.html', {'form':form})


def del_article(request, id):
    if request.method == 'GET':
        Articles.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def category(request):
    if request.method == 'GET':
        # column = Column.objects.all()
        return render(request, 'backweb/category.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        Column.objects.create(c_name=name)
        return render(request, 'backweb/category.html')









