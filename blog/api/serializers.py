from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    class Meta:
        fields = ('title', 'text', 'pub_date', 'author', 'is_published')
        model = Post

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.is_published = validated_data.get('is_published',
                                                   instance.is_published)
        instance.save()
        return instance
