from django.urls import include, path
from news import settings
from . import views
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from seithi.sitemaps import NewsSitemap
from django.views.generic import TemplateView


sitemaps = {
    'news': NewsSitemap,
}

urlpatterns = [
    path('', views.news, name="home"),

    # Single news using slug
    path('tamil-news/<str:slug>/', views.new, name="single-news"),

    # Admin post view
    path('tamil-news/', views.new_news, name='new-news'),

    # Tag/category-based news
    path('tamil-seithigal/<str:tag_name>/', views.news_by_tag, name='news-by-tag'),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    # Magazine main page
    path('tamil-magazine/', views.magazine_page, name='magazine_page'),

    # Single magazine (you can later also use slug here if needed)
    path('tamil-magazine/<str:slug>/', views.single_magazine, name="single-mag"),
    path('Contact-Us',views.Contactus, name="contact"),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
