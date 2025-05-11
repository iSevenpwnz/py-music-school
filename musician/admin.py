from django.contrib import admin

from musician.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "instrument",
        "age",
        "is_adult",
        "date_of_applying",
    )
    list_filter = ("instrument", "age")
    search_fields = ("first_name", "last_name", "instrument")
    readonly_fields = ("date_of_applying",)
