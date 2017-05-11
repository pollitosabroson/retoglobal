from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializer import UserSerializer
from .utils import filters_user


# Create your views here.


class UserViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        GenericViewSet
):

    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        """
        All platform users are listed
        """
        distinc_sex = request.GET.get('diferent_sex', None)
        # Get viariables for filter
        kwargs = filters_user(request.GET)
        queryset = User.objects.filter(**kwargs)
        # Validation in case of opposite sex filtering
        if distinc_sex:
            queryset = queryset.exclude(genre__name=distinc_sex)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        A specific user is displayed.
        """
        user = get_object_or_404(User, pk=kwargs['pk'])

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @detail_route(
        methods=['get'],
        url_path='match-users'
    )
    def get_points_results(self, request, pk=None):
        """
        It creates a filtering of users that has the similarities.
        """
        user = get_object_or_404(User, pk=pk)
        user_list = user.hobbies.all().values_list(
            'name', flat=True
        )
        user_list = list(user_list)

        queryset = User.objects.filter(
            age__gte=user.age - 3,
            age__lte=user.age + 3,
            hobbies__name__in=user_list,
        ).exclude(
            genre=user.genre,
        )
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        A new user is created on the platform.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
