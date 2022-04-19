from django.contrib import admin

# Register your models here.

from .models import Game

admin.site.register(Game)


class ExampleAdmin(admin.ModelAdmin):
    ordering = ['display', ]

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'display':
            kwargs['strip'] = False
        return super().formfield_for_dbfield(db_field, request, **kwargs)
