from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, ImageList, ImageDetail, ImageAdd, ImageDelete, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ImageList.as_view(), name='images'),
    path('image/<int:pk>/', ImageDetail.as_view(), name='image'),
    path('add-image/', ImageAdd.as_view(), name='add-image'),
    path('delete-image/<int:pk>/', ImageDelete.as_view(), name='delete-image'),
]
