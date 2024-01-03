from django.urls import path
from . import views

urlpatterns = [
  path('details/<int:pk>',views.BookDetailsView.as_view(), name='details' ),
  path('borrow',views.BorrowingHistoryView.as_view(), name='borrow' ),
  path('return/<int:borrow_id>',views.return_book, name='return' ),
]
