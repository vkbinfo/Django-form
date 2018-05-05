from django.shortcuts import render, redirect
from .models import Comment
from .form import CommentForm


def index(request):
    comment_objects = Comment.objects.all()
    return render(request,'guestBook/index.html', {"comment": comment_objects})


def sign(request):
    if request.method == "GET":
        form = CommentForm()
        context = {'form': form}
        return render(request, 'guestBook/sign.html', context)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_obj = Comment(name = request.POST['name_input'], comment = request.POST['comment_input'])
            comment_obj.save()
        return redirect('index')
