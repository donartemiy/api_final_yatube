from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Group, Post, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    text = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta():
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):

    class Meta():
        fields = '__all__'
        model = Follow
        read_only_fields = ('user',)
