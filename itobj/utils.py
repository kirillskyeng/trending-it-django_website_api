from itobj.models import Category

menu = [{'title': 'Add Post', 'url_name': 'add_post'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        context['menu'] = user_menu

        context['cats'] = cats
        return context
