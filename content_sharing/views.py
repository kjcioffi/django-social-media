from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from content_sharing.forms import PostForm

@login_required
def homepage(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = request.user.userprofile
            post.save()
    else:
        form = PostForm()
    
    return render(request, 'content_sharing/homepage.html', {'form': form})
