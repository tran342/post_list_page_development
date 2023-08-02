from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import resource

app_name = 'post'

router = DefaultRouter(trailing_slash=False)
router.register('posts', resource.PublicPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
