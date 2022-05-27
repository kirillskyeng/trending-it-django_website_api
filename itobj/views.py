from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *

menu = [{'title': 'Add Post', 'url_name': 'add_post'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'},
        ]


class ItHome(ListView):
    model = ItObject
    template_name = 'itobj/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'TrendingIT - trending, loved and interesting things in IT world.'
        return context

    def get_queryset(self):
        return ItObject.objects.filter(is_published=True)


class ItCategory(ListView):
    model = Category
    template_name = 'itobj/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'TrendingIT - ' + str(context['posts'][0].cat)
        return context

    def get_queryset(self):
        return ItObject.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DetailView):
    model = ItObject
    template_name = 'itobj/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'itobj/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add new post'
        return context


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login Page')


def register(request):
    return HttpResponse('Register Page')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, the page is not found.</h1><p>Create page for this url.</p>")
