from django.urls import path
from .views import UploadView, ChatView

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload'),
    path('chat/<int:source_id>/', ChatView.as_view(), name='chat'),
]