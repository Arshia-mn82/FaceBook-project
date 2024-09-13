from .models import Profile
from .views import *
from .serializers import *
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def perform_create(self, serializer):
        serializer.save()


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        profile__user = self.request.user

        following_profiles = ProfileHistory.objects.filter(
            follower=profile__user
        ).values_list("following", flat=True)

        return Post.objects.filter(profile__in=following_profiles).order_by(
            "-created_at"
        )


class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            profile_to_follow = Profile.objects.get(pk=kwargs["profile_id"])
            user_profile = request.user.profile

            # Check if already following
            if ProfileHistory.objects.filter(
                follower=user_profile, following=profile_to_follow
            ).exists():
                return Response(
                    {"detail": "You are already following this profile."}, status=400
                )

            # Create follow relationship
            ProfileHistory.objects.create(
                follower=user_profile, following=profile_to_follow
            )
            return Response({"detail": "Profile followed successfully."}, status=200)

        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=404)


class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            profile_to_unfollow = Profile.objects.get(pk=kwargs['profile_id'])
            user_profile = request.user.profile

            # Check if the follow relationship exists
            follow_relationship = ProfileHistory.objects.filter(follower=user_profile, following=profile_to_unfollow)
            if not follow_relationship.exists():
                return Response({"detail": "You are not following this profile."}, status=400)

            # Remove the follow relationship
            follow_relationship.delete()
            return Response({"detail": "Profile unfollowed successfully."}, status=200)

        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=404)