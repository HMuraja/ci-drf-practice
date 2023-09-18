from django.db import IntegrityError
from rest_framework import serializers
from followers.models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'created_at', 'followed_name', ]

    def create(self, validated_data):
        # this method is used to prevent duplicate views
        try:
            return super().create(validated_data)
        # Supre() needs to be called when using a method from the parent class
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })