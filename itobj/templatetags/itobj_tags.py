from django import template
from itobj.models import *

register = template.Library()


@register.inclusion_tag('itobj/show_sidebar.html')
def show_sidebar():
    cats = Category.objects.all()
    return {'cats': cats}


@register.inclusion_tag('itobj/show_title_stats.html')
def show_title_stats(post=None, liked=False):
    return {'p': post, 'liked': liked}
