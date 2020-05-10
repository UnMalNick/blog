from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


from .models import Post
from .forms import CommentForm
from comment.models import Comment

# Create your views here.


class PostView(View):
    template_name = "post/detail.html"
    def get(self, request, category_slug, post_slug):
        post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        form = CommentForm
        context = {
            'post': post,
            'form': form,
            'comments': comments
        }
        return render(request, self.template_name, context)
    
    def post(self, request, category_slug, post_slug):
        user = request.user
        post = get_object_or_404(Post, slug=post_slug, category__slug=category_slug)
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.post = post
            comment.save()
        return redirect('post-detail', category_slug=category_slug, post_slug=post_slug)