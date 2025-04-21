from django.contrib import admin
from company.models import (
    Certification,
    EventGalleryImage,
    BlogImage,
    BlogDetails,
    NewsDetails,
)

admin.site.register(Certification)
admin.site.register(EventGalleryImage)
admin.site.register(BlogImage)
admin.site.register(BlogDetails)
admin.site.register(NewsDetails)
