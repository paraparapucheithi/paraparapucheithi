from django.contrib import admin
from .models import News, Tag, Review, Magazine, MagazineSubscriber,Repoter
from unfold.admin import ModelAdmin

# ✅ Custom admin for News to auto-fill slug from title
@admin.register(News)
class NewsAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'get_reporters','slug', 'published_date']  # Add custom method

    # Custom method to display ManyToMany field
    def get_reporters(self, obj):
        return ", ".join([repoter.name for repoter in obj.repoter.all()])
    get_reporters.short_description = "Reporters"

admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Repoter)

@admin.register(Magazine)
class MagazineAdmin(ModelAdmin):
    list_display = ['title', 'published_date']

@admin.register(MagazineSubscriber)
class SubscriberAdmin(ModelAdmin):
    list_display = ['email', 'subscribed_at']
