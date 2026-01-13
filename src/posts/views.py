from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost
from django.urls import reverse_lazy


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blog_home.html"   
    
    def get_queryset(self): # méthode appeler par ListView our récuperer les datas. On l'a surchage pour filtrer l'affichage en fonction de l'utilisateur
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published = True)
    
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blog_create.html"
    fields = ["title", "content"]
    
class BlogPostEdit(UpdateView):
    model = BlogPost
    template_name = "posts/blog_edit.html"
    fields = ['title','content','published',]
    
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blog_details.html"
    
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts:home')
    template_name = "posts/blog_confirm_delete.html"
    context_object_name = "article"