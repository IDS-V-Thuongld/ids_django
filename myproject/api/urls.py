from django.urls import path, include
from api.views.account_view import AccountView
from rest_framework.routers import DefaultRouter
from api.views.auth_view import LoginView
from api.views.company_view import CompanyView
from api.views.department_view import DepartmentView
from api.views.group_view import GroupView
from api.views.task_assignment_view import TaskAssignmentViewSet
from api.views.task_view import TaskViewSet
# Router cho ViewSet
router = DefaultRouter()
router.register(r'accounts', AccountView, basename='accounts')
router.register(r'company', CompanyView, basename = 'company')
router.register(r'department', DepartmentView, basename = 'department')
router.register(r'group', GroupView, basename='group')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'task-assignments', TaskAssignmentViewSet, basename='task-assignments')
urlpatterns = [
    # Authentication API
    path('auth/login/', LoginView.as_view(), name='login'),

    # CRUD Account API
    path('', include(router.urls)),  # /api/accounts/ sẽ tự động ánh xạ vào ViewSet
]