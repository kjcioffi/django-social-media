import datetime
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from content_sharing.forms import PostForm
from content_sharing.models import Post, Profile

@login_required
def index(request):
    """
    Newsfeed / Home Page for the platform. 

    This view contains social media posts from the past day and enables 
    users to create new posts.
    """
    past_day = timezone.now() - datetime.timedelta(days=1)
    posts_in_past_day = Post.objects.filter(created__range=(past_day, timezone.now()))

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            breakpoint()
            post = form.save(commit=False)
            post.profile = Profile.objects.get(user=request.user)
            post.save()
    else:
        form = PostForm()

    return render(request, 'content_sharing/index.html', {'form': form, 'posts': posts_in_past_day})
    
