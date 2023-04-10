from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sailor, TaskType, Task


@admin.register(Sailor)
class SailorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class SailorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("priority",)


admin.site.register(TaskType)
