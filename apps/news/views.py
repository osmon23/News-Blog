from django.shortcuts import render

from .models import News


def get(request):
    if request.method == 'GET':
        news = News.objects.all()
        context = {
            'news': news,
        }
        return render(request, 'news/index.html', context)


def detail(request, pk):
    if request.method == 'GET':
        news = News.objects.get(pk=pk)
        context = {
            'news': news,
        }
        return render(request, 'news/detail.html', context)
