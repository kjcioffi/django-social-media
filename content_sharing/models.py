from django.db import models
from user_accounts.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=600, blank=True)
    photo = models.ImageField(upload_to=user_directory_path,
                              default='default.jpg')
    
    def __str__(self):
        return f"{self.user}"
    
    
class Post(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=30000)

    def __str__(self):
        return f"Post #{self.id} created by {self.user_profile}"


class PostLike(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user} liked {self.post.user_profile}'s post"
    

class Reply(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    response = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.user_profile} replied to {self.post}"