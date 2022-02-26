from django.contrib import admin
from .models import Accounts, Team, Group
# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('accounts_fullname', 'accounts_key', 'key_vendor')

admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Team)
admin.site.register(Group)