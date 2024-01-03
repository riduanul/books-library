from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from books.models import Book, Borrow
from users.models import UserAccount
from books.forms import ReviewForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 

def send_transaction_email(user, subject, amount, template ):
        message = render_to_string(template, {
            'user':user,
            'amount': amount
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()
        
class BookDetailsView(DetailView):
    model = Book
    template_name ='details.html'
    context_object_name = 'book'
    
    def post(self, request, *args, **kwargs):
         
        review_form = ReviewForm(data=self.request.POST)
        book = self.get_object()

        existing_borrow = Borrow.objects.filter(user=request.user, book=book, is_borrow=True).first()

        if existing_borrow:
            messages.warning(self.request, "You have already borrowed this book.")
        elif 'borrow_post' in request.POST:
            if book.quantity > 0:
                account = request.user.user
                Borrow.objects.create(user=request.user, book=book, quantity=1, is_borrow= True)
                book.quantity -= 1
                account.balance -= book.price
                book.save()
                account.save()
                messages.success(self.request, "Book Borrowed Successfully")
                send_transaction_email(self.request.user,"Deposit Message", book.price, 'borrow_email.html' )
            else:
                messages.success(self.request, "Sorry, the book is out of stock.")
        elif 'review_post' in request.POST:
            if existing_borrow:
                if review_form.is_valid():
                    new_review = review_form.save(commit=False)
                    new_review.book = book
                    new_review.save()
                    return redirect('details', pk=book.pk)
            else:
                messages.warning(self.request, "You can only submit a review after borrowing the book.")

        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        book = self.get_object()
        reviews = book.reviews.all
        review_form = ReviewForm()
        
        context['reviews'] = reviews
        context['review_form'] = review_form
        
        return context


class BorrowingHistoryView(ListView):
    model = Borrow
    template_name= 'profile.html'
    context_object_name = 'borrows'
   
    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    
    if request.user == borrow.user:
        borrow.is_borrow = False
        borrow.save()
        
        user_account = UserAccount.objects.get(user=request.user)
        user_account.balance += borrow.book.price
        user_account.save()
        return redirect('borrow')
    

