from django.contrib import admin
from .models import AkunSosmed


@admin.register(AkunSosmed)
class AkunSosmedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nama_depan',
        'nama_belakang',
        'username',
        'platform',
    )

    list_filter = (
        'platform',
    )

    search_fields = (
        'nama_depan',
        'nama_belakang',
        'username',
    )
