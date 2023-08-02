from django.urls import path, include

app_name = 'apis'

urlpatterns = [
    path('post/', include('apis.post.urls', namespace='post')),  # This is url for all APIs app
]
