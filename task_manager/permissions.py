from rest_framework import permissions


class IsTaskAssignee(permissions.BasePermission):
    """
    Custom permission to check if the authenticated user is the task assignee.

    This permission allows access only if the authenticated user is the assignee of the task.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the task assignee.

        Args:
            request (HttpRequest): The incoming HTTP request.
            view (APIView): The view handling the request.
            obj (Task): The task object being accessed.

        Returns:
            bool: True if the user is the task assignee, False otherwise.
        """
        return obj.assignee == request.user