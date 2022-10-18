from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import *


def index(request):
    return render(request, 'news/index.html', {
        'page_title': _('PageTitle'),
        'all_posts': Post.objects.all()

    })

