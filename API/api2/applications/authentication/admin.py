from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Roles, Permissions, Users, Roles, PermissionsRoles

# class DemoRolesInline(admin.TabularInline):
#     pass

class PermissionsRolesInline(admin.TabularInline):
    model = PermissionsRoles
    extra: 1 # permision roles un campo mas

class RolesAdmin(admin.ModelAdmin):
    inlines = (PermissionsRolesInline,)
    list_display = ('pk', 'Name', 'Description')
    fieldsets = (
        ('Roles', {
            'fields': ('Name', 'Description', 'Active', 'Deleted')
        }),
    )
    
class UserAdmin(UserAdmin):
    model = Users
    fieldsets = UserAdmin.fieldsets
    
    
# -----------------------------------------------------------------------------    
#  hacer columan de inline
admin.site.register(Permissions)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Users)