from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, DeletePostView, CategoryView, CategoryListView, LikeView, UpdatePostView, AboutMaintainerBlog, AddCommentView, Search, SocialMediaLinks
urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('aboutme/', AboutMaintainerBlog, name='about_me'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('search/', views.Search, name='search'),
    path('social_media_links/', views.SocialMediaLinks, name='social_media_links'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)