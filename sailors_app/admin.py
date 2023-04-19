from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sailor, TaskType, Task, Position


@admin.register(Sailor)
class SailorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "board_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", "board_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                    "board_number",
                )
            },
        ),
    )
    list_filter = ("position",)


@admin.register(Task)
class SailorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("priority",)


@admin.register(Position)
class SailorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(TaskType)
class SailorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
