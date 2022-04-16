from django.shortcuts import render
from .models import *
from .forms import *

now = timezone.now()
def pet_list(request):
    if request.user.is_anonymous:
        object_list = Pet.objects.all().order_by('-publish')
    else:
        object_list = Pet.objects.filter(owner=request.user).all().order_by('-publish')
    return render(request,'pet/pet_list.html',
            {'pets': object_list})

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        user_form = CreateUserAccountForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("pet:pet_list")
    else:
        user_form = CreateUserAccountForm()
    return render(request, 'pet/signup.html', {'user_form': user_form})

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


#to view details of the post from the application
@login_required
def pet_detail(request):
    posts = Pet.objects.all()
    return render(request, 'pet/pet_detail.html',
                  {'posts': posts})


#to add new post from the application
@login_required
def pet_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('pet:pet_list')
    else:
        form = PostForm()
    return render(request, 'pet/pet_new.html', {'form': form})


#to edit the post from the application
#@login_required
def pet_edit(request, pk):
    post = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        # update
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_date = timezone.now()
            post.save()
            if request.user.is_superuser:
                return redirect('pet:pet_detail')
            else:
                newrequest = HttpRequest()
                newrequest.method = 'GET'
                newrequest.user = request.user
                return pet_post(newrequest, post.pk)
    else:
        # edit
        form = PostForm(instance=post)
    return render(request, 'pet/pet_edit.html', {'form': form})


#to delete the post from the application
@login_required
def pet_delete(request, pk):
    post = get_object_or_404(Pet, pk=pk)
    post.delete()
    if request.user.is_superuser:
        return redirect('pet:pet_detail')
    else:
        return redirect('pet:pet_list')

def pet_post(request, post_id):
    post = get_object_or_404(Pet, id=post_id)
    # List of active comments for this post
    #comments = post.comments.filter()
    #new_comment = None
    #if request.method == 'POST':
        # A comment was posted
    #    comment_form = CommentForm(data=request.POST)
    #    if comment_form.is_valid():
    #        # Create Comment object but don't save to database yet
    #        new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
    #        new_comment.post = post
    #        new_comment.name = request.user.first_name
    #        new_comment.email = request.user.email
            # Save the comment to the database
    #        new_comment.save()
    #        comment_form = CommentForm()
    #else:
    #    comment_form = CommentForm()
    return render(request, 'pet/pet_post.html',{'post': post})



#comment list view from the application
#@login_required
#def comment_list(request):
#    comments = Comment.objects.all()
#    return render(request, 'journey/comment_list.html',
#              {'comments': comments})


#to edit the comment from the application
#@login_required
#def comment_edit(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    if request.method == "POST":
#        # update
#        form = CommentForm(request.POST, instance=comment)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.updated_date = timezone.now()
#            comment.save()
#            return redirect('journey:comment_list')
#    else:
#        # edit
#        form = CommentForm(instance=comment)
#    return render(request, 'journey/comment_edit.html', {'form': form})



#to delete the comment from the application
#@login_required
#def comment_delete(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    comment.delete()
#    return redirect('journey:comment_list')
