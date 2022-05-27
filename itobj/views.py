from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Post', 'url_name': 'add_page'},
        {'title': 'Contact Us', 'url_name': 'contact'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = ItObject.objects.all()
    cats = Category.objects.all()
    context = {
        'title': 'Main Page',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_category(request, cat_id):
    posts = ItObject.objects.filter(cat=cat_id)
    cats = Category.objects.all()
    context = {
        'title': Category.objects.get(pk=cat_id),
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_post(request):
    return HttpResponse('show_post Page')


def about(request):
    return HttpResponse('About Page')


def addpage(request):
    return HttpResponse('Add Page Page')


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login Page')


def register(request):
    return HttpResponse('Register Page')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Category</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, the page is not found.</h1><p>Create page for this url.</p>")
