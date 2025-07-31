from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from slugify import slugify  

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True,allow_unicode=True)  # ✅ New field
    description = models.TextField()
    content = RichTextUploadingField()
    thumbnail = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)  # now keeps Tamil!
            slug = base_slug
            num = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("single-news", args=[self.slug])
class Review(models.Model):

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.TextField(null=True,blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.news.title
    

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    thumbnail = models.ImageField(null=True,blank=True)
    pdf_file = models.FileField(null=True,blank=True)
    published_date = models.DateField(auto_now_add=True)

class MagazineSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class ReviewMag(models.Model):

    Magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    name = models.TextField(null=True,blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.Magazine.title
