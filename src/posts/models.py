from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse


User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.CharField(max_length=255, unique=True, blank=True)
    Author = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank = True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True,null=True, upload_to='blog/')
    
    class Meta:
        ordering = ['-last_updated']
        verbose_name = 'Article'
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)       
        super().save(*args, **kwargs)
    
    @property
    def author_or_self_default(self):
        return self.Author.username if self.Author else "l'Auteur inconnue"
    
    def get_absolute_url(self):
        return reverse("posts:home")
    