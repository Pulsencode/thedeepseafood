from django.urls import path
from . import views


urlpatterns = [
    path(
        "job-category-view",
        views.JobCategoryListView.as_view(),
        name="job_category_view",
    ),
    path(
        "job-category-add",
        views.JobCategoryCreateView.as_view(),
        name="job_category_add",
    ),
    path(
        "job-category-update/<int:id>/",
        views.JobCategoryUpdateView.as_view(),
        name="job_category_update",
    ),
    path("career-view", views.CareerListView.as_view(), name="career_view"),
    path("career-add", views.CareerCreateView.as_view(), name="career_add"),
    path(
        "career-update/<int:pk>/",
        views.CareerUpdateView.as_view(),
        name="career_update",
    ),
    path(
        "application-view", views.ApplicationListView.as_view(), name="application_view"
    ),
]
