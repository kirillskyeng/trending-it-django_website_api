from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Page")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Category</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, the page is not found.</h1><p>Create page for this url.</p>")
