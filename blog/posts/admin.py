from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'text',
                    'pub_date',
                    'author',
                    'is_published')
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
