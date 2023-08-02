from django.urls import path, include

from pages.post import views

app_name = 'pages'

urlpatterns = [
    # This is post index page, I do this way to remove the trailing slash of post page
    # So all the pages list here will be without trailing slash, like /author, /category, /tag etc
    path('posts', views.PostView.as_view(), name='post-view'),
    # This is url for pages inside the post
    path('posts/', include('pages.post.urls', namespace='post')),
]
