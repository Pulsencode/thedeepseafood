from django.urls import path
from . import views


urlpatterns = [
    path("brand-view", views.BrandListView.as_view(), name="brand_view"),
    path("brand-add", views.BrandCreateView.as_view(), name="brand_add"),
    path(
        "brand-update/<int:id>/", views.BrandUpdateView.as_view(), name="brand_update"
    ),
    path("gallery-view", views.GalleryListView.as_view(), name="gallery_view"),
    path("gallery-add", views.GalleryCreateView.as_view(), name="gallery_add"),
    path(
        "gallery-update/<int:id>/",
        views.GalleryUpdateView.as_view(),
        name="gallery_update",
    ),
    path("delete-slider/<int:image_id>/", views.delete_slider, name="delete_slider"),
    path("news-view", views.NewsListView.as_view(), name="news_view"),
    path("news-add", views.NewsCreateView.as_view(), name="news_add"),
    path("news-update/<int:id>/", views.NewsUpdateView.as_view(), name="news_update"),
    path(
        "delete-newsslider/<int:image_id>/",
        views.delete_newsslider,
        name="delete_newsslider",
    ),
    path("promotion-view", views.PromotionListView.as_view(), name="promotion_view"),
    path("promotion-add", views.PromotionCreateView.as_view(), name="promotion_add"),
    path(
        "promotion-update/<int:id>/",
        views.PromotionUpdateView.as_view(),
        name="promotion_update",
    ),
    path(
        "delete-promotionslider/<int:image_id>/",
        views.delete_promotionslider,
        name="delete_promotionslider",
    ),
    path("blog-view", views.BlogListView.as_view(), name="blog_view"),
    path("blog-add", views.BlogCreateView.as_view(), name="blog_add"),
    path("blog-update/<int:id>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path(
        "delete-blogslider/<int:image_id>/",
        views.delete_blogslider,
        name="delete_blogslider",
    ),
    path("team-view", views.TeamListView.as_view(), name="team_view"),
    path("team-add", views.TeamCreateView.as_view(), name="team_add"),
    path("team-update/<int:id>/", views.TeamUpdateView.as_view(), name="team_update"),
    path(
        "testimonial-view", views.TestimonialListView.as_view(), name="testimonial_view"
    ),
    path(
        "testimonial-add", views.TestimonialCreateView.as_view(), name="testimonial_add"
    ),
    path(
        "testimonial-update/<int:id>/",
        views.TestimonialUpdateView.as_view(),
        name="testimonial_update",
    ),
    path("history-view", views.HistoryListView.as_view(), name="history_view"),
    path("history-add", views.HistoryCreateView.as_view(), name="history_add"),
    path(
        "history-update/<int:id>/",
        views.HistoryUpdateView.as_view(),
        name="history_update",
    ),
    path(
        "delete-historyslider/<int:image_id>/",
        views.delete_historyslider,
        name="delete_historyslider",
    ),
    path("contact-view", views.ContactListView.as_view(), name="contact_view"),
    path("enquiry-view", views.EnquiryListView.as_view(), name="enquiry_view"),
    path("export_excel/", views.ExportExcel.as_view(), name="export_excel"),
    path(
        "supermarket-view", views.SupermarketListView.as_view(), name="supermarket_view"
    ),
    path(
        "supermarket-update/<int:id>/",
        views.SupermarketUpdateView.as_view(),
        name="supermarket_update",
    ),
    path(
        "supermarket-add", views.SupermarketCreateView.as_view(), name="supermarket_add"
    ),
    path(
        "certification-view",
        views.CertificationListView.as_view(),
        name="certification_view",
    ),
    path(
        "certification-update/<int:id>/",
        views.CertificationUpdateView.as_view(),
        name="certification_update",
    ),
    path(
        "certification-add",
        views.CertificationCreateView.as_view(),
        name="certification_add",
    ),
    # path("about-view", views.AboutusListView.as_view(), name="about_view"),
    # path(
    #     "about-update/<int:id>/", views.AboutusUpdateView.as_view(), name="about_update"
    # ),
    # path("about-add", views.AboutusCreateView.as_view(), name="about_add"),
    path("seo-view", views.SeoListView.as_view(), name="seo_view"),
    path("seo-update/<int:id>/", views.SeoUpdateView.as_view(), name="seo_update"),
    path("seo-add", views.SeoCreateView.as_view(), name="seo_add"),
]
