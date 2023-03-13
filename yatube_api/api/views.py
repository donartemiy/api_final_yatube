from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Group, Post, User, Comment
from .serializers import GroupSerializer, PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import MethodNotAllowed
from django.shortcuts import get_object_or_404


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

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments
