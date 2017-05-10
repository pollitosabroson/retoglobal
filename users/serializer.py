from rest_framework import serializers

from hobbies.models import Hobbie

from .models import User


class HobbieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobbie
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

    genre = serializers.CharField(
        source='genre.name'
    )
    hobbies = HobbieSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'age',
            'genre',
            'hobbies',
            'last_name',
            'name',
        )
