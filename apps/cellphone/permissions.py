from rest_framework.permissions import BasePermission

from apps.cellphone.models import CellphoneAccessToken


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        is_authenticating = "/brands/authenticate/" in request.path

        if is_authenticating:
            return True

        auth_token = request.headers.get("Authorization")
        if not auth_token:
            return False

        token = CellphoneAccessToken.objects.filter(token=auth_token).first()
        if not token:
            return False

        if token.is_expired:
            return False

        return True
