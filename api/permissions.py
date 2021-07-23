from rest_framework.permissions import BasePermission, SAFE_METHODS
from blog.models import Post
from users.models import Profile


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        if isinstance(obj, Post):  # check if obj is instance of Post class in order to access owner attr correctly
            return obj.author == request.user
        elif isinstance(obj,
                        Profile):  # check if obj is instance of Profile class in order to access owner attr correctly
            return obj.user == request.user

        return obj == request.user
