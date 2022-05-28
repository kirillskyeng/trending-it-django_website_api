from rest_framework import serializers

from .models import ItObject


class ItObjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ItObject
        fields = ('title', 'slug', 'content', 'is_published', 'cat', 'user')
