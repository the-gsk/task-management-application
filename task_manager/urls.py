from django.urls import path,include
from .api import UserLoginView, UserRegistrationView, TaskViewSet
from rest_framework.routers import DefaultRouter
from . import views

# for apis
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task_manger')

urlpatterns = [
    path('api/login/', UserLoginView.as_view(), name='user_login'),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/', include(router.urls)),
]


# for views
urlpatterns += [
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),

]