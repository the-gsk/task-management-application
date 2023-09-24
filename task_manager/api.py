from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets,generics
from .serializers import TaskSerializer,UserRegistrationSerializer
from .permissions import IsTaskAssignee
from .models import Task



class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing tasks.

    Provides CRUD operations for tasks, with permissions applied.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskAssignee]

    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of tasks assigned to the authenticated user.
        """
        user = self.request.user
        queryset = Task.objects.filter(assignee=user).order_by('due_date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        """
        Create a new task, assigning it to the authenticated user.
        """
        serializer.save(assignee=self.request.user)

class UserLoginView(ObtainAuthToken):
    """
    API endpoint for user authentication.

    Allows users to log in and obtain an authentication token.
    """
    permission_classes = []

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration.

    Allows new users to create accounts with the provided information.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]






