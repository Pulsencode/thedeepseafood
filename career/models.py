from django.db import models

# Create your models here.


class JobPosting(models.Model):
    category = models.TextField(null=True)  # IT ,marketing
    status = models.BooleanField(null=False, blank=True, default=True)
    title = models.TextField(null=True)
    location = models.TextField(null=True)
    description = models.TextField(null=True)
    job_type = models.TextField(null=True)  # hybride,full time
    salary = models.TextField(null=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ApplicationDetails(models.Model):
    NoTICE_PERIOD = (
        ("immediate join", "Immediate join"),
        ("2 week", "2 Week"),
        ("1 month", "1 Month"),
    )

    start_date = models.DateField(null=True, blank=True)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, null=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    notice_period = models.CharField(max_length=100, choices=NoTICE_PERIOD, null=True)
    linkedin_url = models.TextField(null=True)
    portfolio_url = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)

    message = models.TextField(null=True, blank=True)
    upload_cv = models.FileField(upload_to="careerfiles", null=True)
    cover_letter = models.FileField(upload_to="careerfiles", null=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # old one


# class JobCategory(models.Model):
#     name = models.TextField(null=True)
#     status = models.BooleanField(null=False, blank=True, default=True)#finilize
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

# class VaccancyDetails(models.Model):
#     category = models.ForeignKey(JobCategory,null=True,blank=True,related_name="job_category",on_delete=models.CASCADE)#iT
#     title = models.TextField(null=True)#Djngo
#     location = models.TextField(null=True)#knr
#     description = models.TextField(null=True)#good comunicztion
#     type = models.TextField(null=True)#hybrid
#     salary = models.TextField(null=True)#34453

#     status = models.BooleanField(null=False, blank=True, default=True)#avilable
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

# class ApplicationDetails(models.Model):
#     vaccancy = models.ForeignKey(VaccancyDetails,null=True,blank=True,on_delete=models.CASCADE)
#     start_date = models.DateField(null=True, blank=True)
#     job = models.TextField(null=True)
#     first_name = models.TextField(null=True)
#     last_name = models.TextField(null=True)
#     email = models.TextField(null=True)
#     mobile_no = models.TextField(null=True)
#     notice = models.TextField(null=True)
#     linkedin = models.TextField(null=True)
#     portfolio = models.TextField(null=True)
#     date = models.DateField(null=True)

#     message = models.TextField(null=True, blank=True)
#     attachment = models.FileField(null=True,blank=True)
#     cover = models.FileField(upload_to='careerfiles',null=True)

#     status = models.BooleanField( default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
