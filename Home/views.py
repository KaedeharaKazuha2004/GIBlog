from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category, User, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def Home(request):
 #   return render(request, 'Home.html', {})
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
class HomeView(ListView):
    model = Post
    template_name = "Home.html"
    ordering = ['post_date']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('Home')
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts': category_posts})
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
def AboutMaintainerBlog(request):
    return render(request, 'about_maintainer_blog.html')
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('Home')
def Search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        post = Post.objects.filter(title__contains = searched) | Post.objects.filter(title_tag__contains = searched) 
        return render(request, 'search_post.html', {'searched': searched, 'post': post})
    else:
        return render(request, 'search_post.html', {})
def SocialMediaLinks(request):
    return render(request, 'social_media_links.html')