from django.db import models
from profile_app.models import Profile
from post_app.models import Post


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
