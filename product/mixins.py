from rest_framework import permissions

from .permission import IsStaffEditorPermissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermissions]

class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self,*args,**kwargs):
        lookup_field = {}
        lookup_field[self.user_field] = self.request.user
        qs = super().get_queryset(*args,**kwargs)
        return qs.filter(**lookup_field)