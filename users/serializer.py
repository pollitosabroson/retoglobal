from rest_framework import serializers

from genres.models import Genre
from hobbies.models import Hobbie

from .models import User


class HobbieSerializer(serializers.ModelSerializer):
    """
    Serializer for Hobbies
    """

    class Meta:
        model = Hobbie
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Users.
    """

    # It's used custom field for genre
    genre = serializers.CharField(
        source='genre.name'
    )
    # It's used seriralizer HobbieSerializer
    hobbies = HobbieSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'age',
            'genre',
            'hobbies',
            'last_name',
            'name',
        )

    # Create custom User
    def create(self, validated_data):
        hobbies = validated_data.pop('hobbies')
        genre_name = validated_data.pop('genre')
        # Here you get the gender, in case of no exister is created
        genre, status = Genre.objects.get_or_create(**genre_name)
        user = User(
            genre=genre,
            **validated_data
        )
        user.save()

        # Creation Hobbires for users
        for hobbie in hobbies:
            object_hobbie, status = Hobbie.objects.get_or_create(**hobbie)
            user.hobbies.add(object_hobbie)
        return user
