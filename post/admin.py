from django.contrib import admin
from post.models import Post
# Register your models here.

class  PostAdmin(admin.ModelAdmin):
    
    list_display = ["title","publishing_date"]
    list_display_links=["publishing_date"]
    
    class Meta:
        model =Post


admin.site.register(Post,PostAdmin)








