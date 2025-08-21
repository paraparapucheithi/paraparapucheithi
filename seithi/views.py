from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import News,Review, ReviewMag,Tag,Magazine,MagazineSubscriber
from collections import defaultdict


def news(request):
    news = News.objects.all()
    tags = Tag.objects.all()
    bnews = News.objects.filter(tags__name="பரபரப்பு செய்தி").order_by('-published_date')[:8]
    tags_with_news = []
    for tag in tags:
        related_news = News.objects.filter(tags=tag).order_by('-published_date')
        tags_with_news.append((tag, related_news))
    context = {'news': news,'tags':tags, 'istop':bnews,'tags_with_news': tags_with_news,}
    return render(request, 'seithi/news.html', context)

def new(request, slug):
    projectobj = get_object_or_404(News, slug=slug)
    tagsa = Tag.objects.all()
    tags = projectobj.tags.all()
    latest_news = News.objects.exclude(slug=slug).order_by('-published_date')[:3]
    matched_news = News.objects.filter(tags__in=tags).exclude(slug=slug).distinct().order_by('-published_date')[:30]

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            Review.objects.create(news=projectobj, name=name, body=body)
            return redirect('single-news', slug=slug)

    comments = projectobj.review_set.all().order_by('-created')

    context = {
        'new': projectobj,
        'tagsa' : tagsa,
        'tags': tags,
        'latest_news': latest_news,
        'matched_news': matched_news,
        'comments': comments,
    }

    return render(request, 'seithi/single-news.html', context)

def new_news(request):
    news = News.objects.all().order_by('-published_date')
    tags = Tag.objects.all()
    context = {
        'news': news,
        'tags': tags,
    }
    return render(request, 'seithi/new_news.html', context)


def news_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    news = News.objects.filter(tags=tag).order_by('-published_date')  # No slicing here!
    tags = Tag.objects.all()  # For the dropdown
    return render(request, 'seithi/tag_news.html', {'news': news, 'tags': tags, 'tag_name': tag_name,})

def magazine_page(request):
    magazines = Magazine.objects.order_by('-published_date')
    tags = Tag.objects.all()

    return render(request, 'seithi/magazine_page.html', {
        'magazines': magazines,
        'tags':tags,
    })
def single_magazine(request,slug):
    magazine = Magazine.objects.get(slug = slug)
    show_pdf = True
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            ReviewMag.objects.create(Magazine=magazine, name=name, body=body)
            return redirect('single-mag', slug=slug)

    comments = ReviewMag.objects.filter(Magazine=magazine).order_by('-created')
    return render(request, 'seithi/single-mag.html',{'magazine' : magazine,'show_pdf':show_pdf,'comments':comments})

def Contactus(request):
    return render(request, 'seithi/contactus.html')


def terms(request):
    return render(request, 'seithi/terms.html')

def privacy(request):
    return render(request, 'seithi/privacy.html')

def robots_txt(request):
    return render(request, "seithi/robots.txt", content_type="text/plain")
