from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts})

def list_tags(request):
    tags = Tag.objects.all()
    return render(request, 'list_tags.html', {'tags': tags})

def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})

def list_user_profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'list_user_profiles.html', {'user_profiles': user_profiles})

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'create_post.html', {'form': form})

def update_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('list_tags')
    else:
        form = TagForm(instance=tag)
    return render(request, 'create_tag.html', {'form': form})

def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'create_user.html', {'form': form})

def update_user_profile(request, user_profile_id):
    user_profile = UserProfile.objects.get(id=user_profile_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('list_user_profiles')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'create_user_profile.html', {'form': form})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('list_posts')

def delete_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect('list_tags')

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('list_users')

def delete_user_profile(request, user_profile_id):
    user_profile = UserProfile.objects.get(id=user_profile_id)
    user_profile.delete()
    return redirect('list_user_profiles')








