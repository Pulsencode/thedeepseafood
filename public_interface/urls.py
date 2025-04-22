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
    path("product", views.product, name="product"),
    path(
        "product-details/<slug:slug>/",
        views.product_details,
        name="product_details",
    ),
    path("contact", views.contact, name="contact"),
    path("news-room", views.news_room, name="newsroom"),
    path("news-details/<int:pk>/", views.news_detail, name="news_details"),
    path("brands/oceano", views.brand, name="brands"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("meeting/", views.meeting, name="meeting"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path(
        "terms-and-conditions/", views.terms_and_condition, name="terms_and_conditions"
    ),  # path("", views.IndexView.as_view(), name="index"),
    # path("career", views.CareerView.as_view(), name="careers"),
    # path("blogs/<slug:slug>/", views.BlogDetailsView.as_view(), name="blog_details"),
    # path("product", views.ProductView.as_view(), name="product"),
    # path(
    #     "product-details/<slug:slug_product>/",
    #     views.ProductDetailsView.as_view(),
    #     name="product_details",
    # ),
    # path("news-room", views.NewsRoomView.as_view(), name="newsroom"),
    # path(
    #     "news-details/<int:id>/", views.NewsDetailsView.as_view(), name="news_details"
    # ),
    # path("brands/oceano", views.BrandView.as_view(), name="brands"),
    path(
        "get_product_index/", views.IndexProductView.as_view(), name="get_product_index"
    ),
    path(
        "get_product_lists/",
        views.ProductListingView.as_view(),
        name="get_product_lists",
    ),
    path("search_product/", views.SearchProductView.as_view(), name="search_product"),
    path(
        "product_details_switch/",
        views.GeneralProductDetailsView.as_view(),
        name="product_details_switch",
    ),
    path("brands-list", views.BrandsListView.as_view(), name="brands_list"),
    path(
        "get_product_content/",
        views.ProductContentView.as_view(),
        name="get_product_content",
    ),
    path("load_more_product/", views.load_more_product, name="load_more_product"),
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
    path("get_news/", views.LoadNews.as_view(), name="get_news"),
    path("get_global_news/", views.LoadGlobalNews.as_view(), name="get_global_news"),
    path("load_more_news/", views.load_more_news, name="load_more_news"),
    path("load_more_events/", views.load_more_events, name="load_more_events"),
    path("get_events/", views.LoadEvents.as_view(), name="get_events"),
    path("get_promotions/", views.LoadPromotions.as_view(), name="get_promotions"),
    path("news-lists", views.NewsListsView.as_view(), name="news_lists"),
    path(
        "promotion-view/<int:id>/",
        views.PromotionView.as_view(),
        name="promotion_details",
    ),
    path("send_email/", views.SendEmailView.as_view(), name="send_email"),
    path("job_email/", views.CareerEmailView.as_view(), name="job_email"),
    path("enquiry_email/", views.ProductEnquiryView.as_view(), name="enquiry_email"),
]
