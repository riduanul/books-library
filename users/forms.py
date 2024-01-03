from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import UserAccount, Transaction


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserAccount.objects.create(user=user)
        return user

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields=['amount']
        
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account', None)
        super().__init__(*args, **kwargs)
        
    
    def clean_amount(self):
        min_transaction = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_transaction:
            raise forms.ValidationError(f'You have to deposit at least ${min_transaction}')
        return amount 
    
    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


