from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete= models.CASCADE)
    balance = models.IntegerField(default=0)
         
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount,related_name='transactions', on_delete= models.CASCADE )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['timestamp']
        