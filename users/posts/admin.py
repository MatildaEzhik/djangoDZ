from django.contrib import admin

from posts.models import Article

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)



admin.site.register(Article, PostAdmin)