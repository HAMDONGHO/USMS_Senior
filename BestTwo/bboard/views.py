from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'bbs/home.html', {'posts' : posts})


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    commentForm = CommentForm()
    return render(request, 'bbs/detail.html', {'post' : post_detail, 'commentForm':commentForm})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'bbs/post_new.html', {'form':form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bbs/post_edit.html', {'form':form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('home')


def comment_new(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=post_id)
            comment.author = request.user
            comment.save()
            return redirect('detail', post_id=post_id)
    else:
        return redirect('home')


def comment_delete(request, post_id):
    comment = get_object_or_404(Comment, pk = post_id)
    comment.delete()
    return redirect('home')
