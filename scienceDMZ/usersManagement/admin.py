from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Get UserProfile to be displayed on admin
class UserProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile

admin.site.register(UserProfile,UserProfileAdmin)
