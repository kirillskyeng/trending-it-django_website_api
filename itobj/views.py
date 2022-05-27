from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Post', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = ItObject.objects.all()
    context = {
        'title': 'TrendingIT - trending, loved and interesting things in IT world.',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_category(request, cat_id):
    posts = ItObject.objects.filter(cat=cat_id)
    context = {
        'title': Category.objects.get(pk=cat_id),
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(ItObject, pk=post_id)
    cats = Category.objects.all()

    context = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cats': cats,
        'cat_selected': post.cat_id,
        'menu_active_url': post.cat,
    }

    return render(request, 'itobj/post.html', context=context)


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
