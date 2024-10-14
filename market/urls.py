from django.urls import path
from .import views

urlpatterns = [
    path('', views.get_user, name='get'),
    path('create/', views.create_user, name='create'),
    path('detail/<int:pk>', views.user_detail, name='detail'),
]
