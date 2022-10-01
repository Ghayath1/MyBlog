from django.shortcuts import render,redirect
from comments.models import Comment

from .models import Post

from .forms import PostForm
from comments.forms import CommentForm

# Create your views here.
def post_list(request):
    blog= Post.objects.all()
    return render(request,'post_list.html',{'all_posts':blog})

def post_detail(request,id):
    post =Post.objects.get(id=id)
    post_comments=Comment.objects.filter(post=post)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           myform = form.save(commit=False)
           myform.author=request.user
           myform.post=post
           myform.save()
    
    else:
        form=CommentForm()

    return render(request,'post_detail.html',{'single':post,'coments':post_comments,'form':form})

def new_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
           myform = form.save(commit=False)
           myform.author =request.user
           myform.save()
           return redirect('/blog')
    else:
     
        form =PostForm()
    return render(request,'new_post.html',{'form':form})

def edit_post(request,id):
    post=Post.objects.get(id=id)

    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
           
    else:
     
         form =PostForm(instance=post)
    return render(request,'edit_post.html',{'form':form})

def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/blog')