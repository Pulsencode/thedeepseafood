from django.contrib import admin
from company.models import (
    Certification,
    Event,
    BlogImage,
    Blog,
    News,
    NewsImage,
    EventImage,
    ManagementTeam,
    History,
    HistoryImage,
    CompanyTestimonial,
    Brand,
)

admin.site.register(Certification)
admin.site.register(CompanyTestimonial)
admin.site.register(Event)
admin.site.register(BlogImage)
admin.site.register(Blog)
admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(EventImage)
admin.site.register(ManagementTeam)
admin.site.register(History)
admin.site.register(HistoryImage)
admin.site.register(Brand)
