from .serializers import *
from .views import *
from .models import *
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(profile__user = self.request.user)
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.all(profile__user = self.request.user)
    
@csrf_exempt
def add_like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.get(id=data['post_id'])
        post.likes += 1
        post.save()
        return HttpResponse('liked')
@csrf_exempt 
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = Post.objects.get(id=data['post_id'])
        comment = data['comment']
        post = Post.objects.get(post_id=post_id)
        post.comment = comment
        post.save()
        return HttpResponse('commented')