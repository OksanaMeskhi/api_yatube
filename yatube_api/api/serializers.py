from rest_framework import serializers

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'group')


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
