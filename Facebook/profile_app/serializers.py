from rest_framework.serializers import ModelSerializer
from .models import *
from post_app.models import Post

class ProfileRegisterSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
        
class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'