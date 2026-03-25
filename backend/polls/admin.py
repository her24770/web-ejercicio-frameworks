from django.contrib import admin
from .models import Poll, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["question", "total_votes", "created_at"]
    inlines = [OptionInline]

    def total_votes(self, obj):
        return obj.total_votes


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ["text", "poll", "votes"]
