from django.db import models
from profile_app.models import Profile
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    profile = models.ForeignKey(Profile  , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)