from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_view_url'),
    path('<int:blog_id>/comment/', views.Blog_New_Comment, name='new_comment_url'),
    path('<int:blog_id>/', views.BlogDetails, name='blog-details'),
    path('wireless-services', views.Package_View, name="wireless-services-url"),
]
