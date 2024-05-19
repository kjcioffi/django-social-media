import datetime
from django.db import DataError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, render

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from content_sharing.forms import PostForm
from content_sharing.models import Post, Profile

from django.contrib.auth.models import User


@login_required
def index(request):
    """
    Newsfeed / Home Page for the platform. 

    This view contains social media posts from the past day and enables 
    users to create new posts.
    """
    past_day = timezone.now() - datetime.timedelta(days=1)
    posts_in_past_day = Post.objects.filter(created__range=(past_day, timezone.now()))
    form = PostForm()

    return render(request, 'content_sharing/index.html', {'form': form, 'posts': posts_in_past_day})

def profile(request, username: str):
    """
    A page that represents a user and their social engagement.
    """
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'content_sharing/profile.html', {'profile': profile})

@require_http_methods(["POST"])
def create_post(request):
    """
    An API integration to handle the creation of social media posts
    in real time.
    """
    try:
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.create(profile=profile, content=request.POST.get('content'))
        return JsonResponse({'creator': post.profile.__str__(), 'content': post.content, 'created': post.created}, status=201)
    
    except DataError as e:
        return JsonResponse({'failure': e.__str__()}, status=400)
    except Exception as e:
        return JsonResponse({'failure': e.__str__()}, status=500)