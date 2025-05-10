from django.urls import path
from django.conf.urls.static import static

from config import settings
from . import views

app_name = 'blogs'

urlpatterns = [
    path('home_data/', views.PostsListView.as_view(), name='home_data'),
    path('post/<int:pk>/', views.PostDetailsView.as_view(), name='post_details'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)