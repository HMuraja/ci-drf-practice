from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        # this method is used to prevent duplicate views
        try:
            return super().create(validated_data)
        # Supre() needs to be called when using a method from the parent class
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
