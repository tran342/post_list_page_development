from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),  # This is url for `post` app
    path('api/', include('apis.urls', namespace='apis')),  # This is url for all APIs app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
