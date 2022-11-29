from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from django.views.generic import View
from users.models import RoleChoices


# NOTE: https://httpd.apache.org/docs/2.2/ko/howto/auth.html


class IsAdminUser(BasePermission):

    def has_permission(self, request: Request, view: View) -> bool:
        return bool(
            request.user
            and request.user.role == RoleChoices.ADMIN
        )

