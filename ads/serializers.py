from rest_framework import serializers
from ads.models import Ad, Comment


class AdSerializers(serializers.ModelSerializer):
    """Сериализатор для просмотра объявлений"""

    class Meta:
        model = Ad
        fields = ['title', 'price', 'descriptions', 'image']


class AdDetailSerializers(serializers.ModelSerializer):
    """Сериалайзер для просмотра одного объявления"""

    class Meta:
        model = Ad
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    """Сериализатор для просмотра отзывов"""
    class Meta:
        model = Comment
        fields = '__all__'