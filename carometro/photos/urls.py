from django.urls import path, include
from . import views

urlpatterns = [
    path('clear/', views.clear_database, name='clear_database'),
    path('list-photos/', views.list_photos, name='list_photos'),
    path('progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
]
