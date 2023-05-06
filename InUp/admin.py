from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fields = ('age', 'gender', 'country', 'full_name', 'phone_number')

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name','user_age', 'user_country', 'user_gender','is_staff')

    def user_age(self, instance):
        return instance.userprofile.age
    user_age.short_description = 'Age'
    
    def user_country(self, instance):
        return instance.userprofile.country
    user_country.short_description = 'Country'

    def user_gender(self, instance):
        return instance.userprofile.get_gender_display()
    user_gender.short_description = 'Gender'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

