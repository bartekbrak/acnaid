from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import *


def news(request, year=None, month=None, slug=None):
    news = get_object_or_404(News, published=True, date__year=year, date__month=month, translations__slug=slug)
    return render_to_response('news/news.html', {
        'news': news,
    }, context_instance=RequestContext(request))


def index(request):
    news = News.objects.filter(published=True).order_by('-date')
    news_paginator = Paginator(news, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        news_page = news_paginator.page(page)
    except (EmptyPage, InvalidPage):
        news_page = news_paginator.page(news_paginator.num_pages)
    return render_to_response('news/index.html', {
        'news_paginator': news_paginator,
        'news_page': news_page,
    }, context_instance=RequestContext(request))
