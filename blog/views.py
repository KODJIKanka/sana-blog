from django.shortcuts import render, redirect, HttpResponseRedirect
from . import models
from . import forms
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def list_group(request):
    groups = models.Category.objects.all()

    return render(request, 'blog/list_group.html', context={'groups': groups})

def detail_article(request, id):   
    article = models.Post.objects.get(id=id)
    articles = models.Post.objects.all()
    context = {
        'article': article,
        'articles': articles
    }
    return render(request, 'blog/detail_article.html', context)

@login_required
def kofi(request):
    return render(request, 'blog/kofi.html')




