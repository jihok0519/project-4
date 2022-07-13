from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birthdays/', views.birthdays_index, name='index'),
    path('birthdays/<int:birthday_id>/', views.birthdays_detail, name='detail'),
    path('birthdays/create', views.BirthdayCreate.as_view(), name='birthdays_create'),
    path('birthdays/<int:pk>/update/', views.BirthdayUpdate.as_view(), name='birthdays_update'),
    path('birthdays/<int:pk>/delete/', views.BirthdayDelete.as_view(), name="birthdays_delete"),
    path('gifts/<int:birthday_id>/assoc_gift/<int:gift_id>/', views.assoc_gift, name='assoc_gift'),
    path('gifts/<int:birthday_id>/assoc_gift/<int:gift_id>/delete/', views.assoc_gift_delete, name='assoc_gift_delete'),
    path('gifts/', views.GiftList.as_view(), name='gifts_index'),
    path('gifts/<int:pk>/', views.GiftDetail.as_view(), name='gifts_detail'),
    path('gifts/create/', views.GiftCreate.as_view(), name='gifts_create'),
    path('gifts/<int:pk>/update/', views.GiftUpdate.as_view(), name='gifts_update'),
    path('gifts/<int:pk>/delete/', views.GiftDelete.as_view(), name='gifts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]