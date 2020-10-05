from django.contrib import admin

from surveys.models import Survey


class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ('title', 'is_active', 'author',)
    list_filter = ('is_active', 'created_on',)
    search_fields = ('title',)
    readonly_fields = ('author',)


admin.site.register(Survey, SurveyAdmin)
