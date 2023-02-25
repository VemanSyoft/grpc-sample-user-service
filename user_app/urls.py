from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user_app.views import UserListApi, UserDetailApi


urlpatterns = [
    path('user/', UserListApi.as_view()),
    path('user/<str:pk>/', UserDetailApi.as_view()),
]
 

urlpatterns = format_suffix_patterns(urlpatterns)
