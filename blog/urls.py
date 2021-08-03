from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('new_post/', new_post, name='new_post'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]
