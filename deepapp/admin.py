from django.contrib import admin
from deepapp.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','username','is_admin']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display =['id','name','logo','status','created','updated']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['id','brand','name','image','status','created','updated']

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display =['id','name','status','created','updated']

@admin.register(EventGallery)
class EventGalleryAdmin(admin.ModelAdmin):
    list_display =['id','title','name','description','location','date','status','created','updated']

@admin.register(EventGalleryImage)
class EventGalleryImageAdmin(admin.ModelAdmin):
    list_display =['id','event','image','created','updated']

@admin.register(NewsDetails)
class NewsDetailsAdmin(admin.ModelAdmin):
    list_display =['id','title','name','description','location','date','status','created','updated']

@admin.register(NewsGalleryImage)
class NewsGalleryImageAdmin(admin.ModelAdmin):
    list_display =['id','news','image','created','updated']

@admin.register(PromotionDetails)
class PromotionDetailsAdmin(admin.ModelAdmin):
    list_display =['id','title','name','description','location','date','status','created','updated']

@admin.register(PromotionImage)
class PromotionImageAdmin(admin.ModelAdmin):
    list_display =['id','promotion','image','created','updated']

@admin.register(BlogDetails)
class BlogDetailsAdmin(admin.ModelAdmin):
    list_display =['id','title','slug','name','description','location','date','status','created','updated']

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display =['id','blog','image','created','updated']

@admin.register(ManagementTeam)
class ManagementTeamAdmin(admin.ModelAdmin):
    list_display =['id','designation','name','image','status','created','updated']

@admin.register(CompanyTestimonial)
class CompanyTestimonialAdmin(admin.ModelAdmin):
    list_display =['id','name','message','image','status','created','updated']

@admin.register(VaccancyDetails)
class VaccancyDetailsAdmin(admin.ModelAdmin):
    list_display =['id','category','title','location','description','status','created','updated']

@admin.register(HistoryDetails)
class HistoryDetailsAdmin(admin.ModelAdmin):
    list_display =['id','year','title','description','status','created','updated']

@admin.register(HistoryImage)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display =['id','history','image','created','updated']

@admin.register(ContactUsDetails)
class ContactUsDetailsAdmin(admin.ModelAdmin):
    list_display =['id','name','location','email','mobile_no','message','created','updated']

@admin.register(EnquiryDetails)
class EnquiryDetailsAdmin(admin.ModelAdmin):
    list_display =['id','product','name','location','email','mobile_no','message','created','updated']

@admin.register(Supermarkets)
class SupermarketsAdmin(admin.ModelAdmin):
    list_display =['id','image','status','created','updated']

@admin.register(RecipeDetails)
class RecipeDetailsAdmin(admin.ModelAdmin):
    list_display =['id','brand','title','description','status','created','updated']

@admin.register(RecipeIngredients)
class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display =['id','recipe','title','amount','created','updated']

@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    list_display =['id','recipe','image','created','updated']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name','brand','title_tag','metatag','keyword','canonical','slug_product','type','homepage','status','image','created','updated']

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display =['id','product','category','sub_categories','price','product_code','net_weight','description','ingredients','instructions','storage_instructions','causion','grade','origin','packing','status']


admin.site.register(ApplicationDetails)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display =['id','image', 'status', 'created', 'updated']
    

# @admin.register(Aboutus)
# class AboutusAdmin(admin.ModelAdmin):
    # list_display =['id','image','title', 'status', 'created', 'updated']