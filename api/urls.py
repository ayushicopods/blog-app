from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view()),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view()),
    path('blogposts/<int:pk>/likes/', views.BlogLikedByUserListCreate.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
