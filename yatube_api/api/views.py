from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Group, Post, User, Comment, Follow
from .serializers import GroupSerializer, PostSerializer, CommentSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyToComments, OwnerOrReadOnly
from rest_framework.exceptions import MethodNotAllowed
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets. ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user, post=get_object_or_404(Post, pk=post_id))


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # http_method_names = ['get', 'post', 'head']

    def list(self, request):
        queryset = Follow.objects.filter(user=request.user)
        serializer = FollowSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
