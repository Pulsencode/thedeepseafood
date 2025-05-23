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
    path("product/enquiry/", views.product_enquiry, name="product_enquiry"),
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
    path("load-more-news/", views.load_more_news, name="load_more_news"),
    path("get_promotions/", views.LoadPromotions.as_view(), name="get_promotions"),
]
