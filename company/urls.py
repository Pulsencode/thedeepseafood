from django.urls import path
from company import views

urlpatterns = [
    # Company Testimonials
    path(
        "view/company-testimonial",
        views.CompanyTestimonialListView.as_view(),
        name="view_company_testimonial",
    ),
    path(
        "create/testimonial",
        views.CompanyTestimonialCreateView.as_view(),
        name="create_company_testimonial",
    ),
    path(
        "update/testimonial/<int:pk>",
        views.CompanyTestimonialUpdateView.as_view(),
        name="update_company_testimonial",
    ),
    # About us
    path(
        "view/about",
        views.AboutListView.as_view(),
        name="view_about_us",
    ),
    path(
        "create/about",
        views.AboutCreateView.as_view(),
        name="create_about_us",
    ),
    path(
        "update/about/<int:pk>",
        views.AboutUpdateView.as_view(),
        name="update_about_us",
    ),
    # Team Member
    path(
        "view/team/",
        views.TeamListView.as_view(),
        name="view_team",
    ),
    path(
        "create/management-team/",
        views.TeamCreateView.as_view(),
        name="create_team",
    ),
    path(
        "update/team/<int:pk>",
        views.TeamUpdateView.as_view(),
        name="update_team",
    ),

]
