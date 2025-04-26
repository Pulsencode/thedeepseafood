from django.contrib import admin


from career.models import ApplicationDetails, JobCategory, VaccancyDetails

admin.site.register(ApplicationDetails)
admin.site.register(JobCategory)
admin.site.register(VaccancyDetails)
