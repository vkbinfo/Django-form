from django.shortcuts import render
from .models import Comment


def index(request):
    comment_objects = Comment.objects.all()
    return render(request,'guestBook/index.html', {"comment": comment_objects})


def sign(request):
    return render(request, 'guestBook/sign.html')