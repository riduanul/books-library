from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import  FormView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import UserRegistrationForm, DepositForm
from users.models import Transaction
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
# Create your views here.

def send_transaction_email(user, subject, amount, template ):
        message = render_to_string(template, {
            'user':user,
            'amount': amount
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()

class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) 


class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')

class DepositMoneyView(LoginRequiredMixin, CreateView):
    
    model = Transaction
    form_class = DepositForm
    template_name = 'deposit.html'
    success_url = 'deposit'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['account'] = self.request.user.user
        return kwargs
        
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.user
        account.balance += amount
        account.save(update_fields = ['balance'])
        send_transaction_email(self.request.user,"Deposit Message", amount, 'deposit_email.html' )
        return super().form_valid(form)
    



    
    
    
    
    