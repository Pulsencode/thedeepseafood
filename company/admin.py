from django.contrib import admin

from company.models import (
    Supermarkets,
    Certification,
    CompanyTestimonial,
    ManagementTeam,
    AboutUs,
    SEO,
    BlogDetails,
    BlogImage,
    NewsDetails,
    NewsGalleryImage,
    PromotionDetails,
    PromotionImage,
    HistoryDetails,
    HistoryImage,
    EventGallery,
    EventGalleryImage,
    Brand
)

admin.site.register(SEO)
admin.site.register(Supermarkets)
admin.site.register(Certification)
admin.site.register(CompanyTestimonial)
admin.site.register(ManagementTeam)
admin.site.register(AboutUs)
admin.site.register(BlogDetails)
admin.site.register(BlogImage)
admin.site.register(NewsGalleryImage)
admin.site.register(NewsDetails)
admin.site.register(PromotionImage)
admin.site.register(PromotionDetails)
admin.site.register(HistoryDetails)
admin.site.register(HistoryImage)
admin.site.register(EventGalleryImage)
admin.site.register(EventGallery)
admin.site.register(Brand)
