from django.contrib import admin
from .models import News, Tag, Review, Magazine, MagazineSubscriber

# ✅ Custom admin for News to auto-fill slug from title
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Auto-generates slug
    list_display = ['title', 'slug', 'published_date']  # Optional: display more info

admin.site.register(Tag)
admin.site.register(Review)

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']

@admin.register(MagazineSubscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
