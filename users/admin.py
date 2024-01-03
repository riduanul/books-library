from django.contrib import admin
from users.models import UserAccount, Transaction
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Transaction)