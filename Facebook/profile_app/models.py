from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class ProfileHistory(models.Model):
    following = models.ForeignKey(Profile, related_name="follower_set", on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, related_name="following_set", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"

