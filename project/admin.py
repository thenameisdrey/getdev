from django.contrib import admin
from . models import Post

# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import Custom_User

# Register your models here. 

admin.site.register(Post)
# admin.site.register(Comment)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = Custom_User
#     list_display = ['username', 'email', 'password']

# admin.site.register(Custom_User, CustomUserAdmin)

