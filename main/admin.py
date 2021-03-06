from django.contrib import admin

from main.models import Account,Post,Tags,Search_history
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username')
    read_only=('date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

class SearchAdmin(UserAdmin):
    model=Search_history
    list_display=('search','user')
    search_fields=('user',)
    read_only=('search','user')
    filter_horizontal=()
    list_filter=()
    ordering = ('user',)
    fieldsets=()

admin.site.register(Account,AccountAdmin)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Search_history,SearchAdmin)