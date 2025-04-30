from django.contrib import admin


from career.models import ApplicationDetails, JobCategory, VacancyDetails

admin.site.register(ApplicationDetails)
admin.site.register(JobCategory)
admin.site.register(VacancyDetails)
