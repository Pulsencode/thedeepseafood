from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path(
        "distribution-channels",
        views.distribution_channel,
        name="distribution",
    ),
    path("blog", views.blog, name="blog"),
    path("blogs/<slug:slug>/", views.blog_details, name="blog_details"),
    path("career", views.career, name="career"),
    path("job_application/", views.job_application, name="job_email"),
    path("product", views.product, name="product"),
    path(
        "product-details/<slug:slug>/",
        views.product_details,
        name="product_details",
    ),
    path("contact", views.contact, name="contact"),
    path("enquiry/", views.enquiry, name="enquiry"),
    path("news-room", views.news_room, name="newsroom"),
    path("news-details/<slug:slug>/", views.news_detail, name="news_details"),
    path("brands/oceano", views.brand, name="brands"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("meeting/", views.meeting, name="meeting"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path(
        "terms-and-conditions/", views.terms_and_condition, name="terms_and_conditions"
    ),
    path(
        "get_product_content/",
        views.ProductContentView.as_view(),
        name="get_product_content",
    ),
    path(
        "promotion-view/<int:id>/",
        views.PromotionView.as_view(),
        name="promotion_details",
    ),
    path("enquiry_email/", views.ProductEnquiryView.as_view(), name="enquiry_email"),
    # oceano related url
    path(
        "get_product_details/",
        views.OceanoProductDetailsView.as_view(),
        name="get_product_details",
    ),
    path(
        "get_modal_product_details/",
        views.OceanoModalProductDetailsView.as_view(),
        name="get_modal_product_details",
    ),
    # load pages
    path("load_more_product/", views.load_more_product, name="load_more_product"),
    path("get_news/", views.LoadNews.as_view(), name="get_news"),
    path("get_global_news/", views.LoadGlobalNews.as_view(), name="get_global_news"),
    # path("load_more_news/", views.load_more_news, name="load_more_news"),
    path("load_more_events/", views.load_more_events, name="load_more_events"),
    path("get_events/", views.LoadEvents.as_view(), name="get_events"),
    path("get_promotions/", views.LoadPromotions.as_view(), name="get_promotions"),
    path("load_more_news/", views.load_more_news, name="load_more_news"),
    path("enquiry_email/", views.ProductEnquiryView.as_view(), name="enquiry_email"),
]
