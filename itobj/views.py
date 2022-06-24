from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from hitcount.views import HitCountDetailView

from .forms import *
from .models import *
from .permissions import *
from .serializers import ItObjectSerializer
from .utils import *


class ItHome(DataMixin, ListView):
    model = ItObject
    template_name = 'itobj/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='TrendingIT - trending, loved and interesting things in IT world.')
        context.update(c_def)
        return context

    def get_queryset(self):
        return ItObject.objects.filter(is_published=True).select_related('cat')


class ItCategory(DataMixin, ListView):
    model = Category
    template_name = 'itobj/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='TrendingIT - ' + str(c.name))
        context.update(c_def)
        return context

    def get_queryset(self):
        return ItObject.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class ShowPost(DataMixin, HitCountDetailView):
    model = ItObject
    template_name = 'itobj/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    count_hit = True

    # def get_object(self, queryset=None):
    #     item = super().get_object(queryset)
    #     item.increase_views()
    #     return item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # liked used to set heart-icon to red or grey color
        liked = False
        if self.object.likes.filter(id=self.request.user.id).exists():
            liked = True
        c_def = self.get_user_context(title=context['post'], liked=liked)
        context.update(c_def)
        return context


def like_view(request, post_slug):
    post = get_object_or_404(ItObject, slug=post_slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=[post_slug]))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'itobj/addpost.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add new post')
        context.update(c_def)
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'itobj/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        context.update(c_def)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'itobj/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, the page is not found.</h1><p>Create page for this url.</p>")


# API VIEWS
class ItObjectAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ItObjectAPIList(generics.ListCreateAPIView):
    queryset = ItObject.objects.all()
    serializer_class = ItObjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ItObjectAPIListPagination


class ItObjectAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ItObject.objects.all()
    serializer_class = ItObjectSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ItObjectAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ItObject.objects.all()
    serializer_class = ItObjectSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)
