from django.urls import path, include
from api.views.account_view import AccountView
from rest_framework.routers import DefaultRouter
from api.views.auth_view import RegisterView, LoginView, LogoutView
# Router cho ViewSet
router = DefaultRouter()
router.register(r'accounts', AccountView, basename='accounts')
urlpatterns = [
    # Authentication API
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # CRUD Account API
    path('', include(router.urls)),  # /api/accounts/ sẽ tự động ánh xạ vào ViewSet
]