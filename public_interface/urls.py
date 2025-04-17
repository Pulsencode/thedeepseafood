from django.urls import path

from public_interface import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("career/", views.career, name="career"),
    path("career/apply-job", views.apply_job, name="apply_job"),
    path("product/", views.product, name="product"),
    path("product/detail/<slug:slug>", views.product_details, name="product_details"),
    path("brand/oceano/", views.brand, name="brand"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/details/<slug:slug>", views.blogs, name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("news-room/", views.news_room, name="news_room"),
    path("news-details/<slug:slug>", views.news_detail, name="news_detail"),
    path("distribution-channel/", views.distribution_channel, name="distribution"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path(
        "terms-and-conditions/", views.terms_and_condition, name="terms_and_conditions"
    ),
]
