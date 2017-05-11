from rest_framework.routers import DefaultRouter

from users import views


router = DefaultRouter(trailing_slash=False)

router.register(r'users', views.UserViewSet, base_name="users")


urlpatterns = [

    # Translation libraries
]

urlpatterns += router.urls
