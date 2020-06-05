from django.db import models


class Campaign(models.Model):
    slug = models.CharField(max_length=32)

    def __str__(self):
        return self.slug


class Link(models.Model):
    campaign = models.ForeignKey(
        Campaign, null=True, blank=True, on_delete=models.SET_NULL
    )
    short_suffix = models.CharField(max_length=16)
    target_url = models.URLField()

    utm_source = models.CharField(max_length=16, null=True, blank=True)
    utm_medium = models.CharField(max_length=16, null=True, blank=True)
    utm_campaign = models.CharField(max_length=16, null=True, blank=True)
    utm_term = models.CharField(max_length=16, null=True, blank=True)
    utm_content = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return "%s /%s #%d" % (self.target_url[:50], self.short_suffix, self.id)


class Visit(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    visited_dt = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    referer = models.URLField()

    def __str__(self):
        return "#%d link#%d" % (self.id, self.link.id)
