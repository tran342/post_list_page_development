from django.urls import path

from pages.post import views

app_name = 'post'

urlpatterns = [
    path('detail', views.PostDetailView.as_view(), name='detail-view'),
]
