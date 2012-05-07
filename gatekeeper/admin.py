from django.contrib import admin

from gatekeeper.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'twitter_name', 'location')
    search_fields = ('user__username', 'user__first_name', 'location', 'twitter_name', 
                    'focus', 'profession', 'blog_url')

admin.site.register(UserProfile, UserProfileAdmin)
