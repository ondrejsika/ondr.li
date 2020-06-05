from django.contrib import admin
from .models import Campaign, Link, Visit


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0


class CampaignAdmin(admin.ModelAdmin):
    inlines = (LinkInline,)


class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "short_suffix",
        "campaign",
        "target_url",
    )
    inlines = (VisitInline,)


class VisitAdmin(admin.ModelAdmin):
    list_display = ("link", "visited_dt", "ip")


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Visit, VisitAdmin)
