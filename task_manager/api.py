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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskAssignee]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        queryset = Task.objects.filter(assignee=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)


class UserLoginView(ObtainAuthToken):
    permission_classes = []

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
