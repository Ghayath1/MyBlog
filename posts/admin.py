from django.contrib import admin

# Register your models here.
from .models import Post, Category
class PostAdmin(admin.ModelAdmin):
    list_display=['title','active','publish_date','author','category']
    list_filter=['active','author','category']
    search_fields=['title','content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
