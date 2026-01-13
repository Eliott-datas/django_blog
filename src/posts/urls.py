from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete
from django.contrib.auth.decorators import login_required

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name = "home"),
    path('create/', login_required(BlogPostCreate.as_view()), name = "create"),  
    path('detail/<str:slug>/', BlogPostDetail.as_view(), name = "detail"),
    path('edit/<str:slug>/', login_required(BlogPostEdit.as_view()), name = "edit"),               
    path('delete/<str:slug>/', login_required(BlogPostDelete.as_view()), name = "delete"),       
]
