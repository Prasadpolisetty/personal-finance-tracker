from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="finance/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("transactions/", views.transaction_list, name="transactions"),
    path("transactions/add/", views.transaction_create, name="transaction_create"),
    path("transactions/<int:pk>/edit/", views.transaction_edit, name="transaction_edit"),
    path("transactions/<int:pk>/delete/", views.transaction_delete, name="transaction_delete"),
    path("transactions/upload/", views.upload_statement, name="upload"),
    path("transactions/export/", views.export_transactions, name="export"),
    path("savings/", views.savings_list, name="savings"),
    path("savings/add/", views.savings_create, name="savings_create"),
    path("savings/<int:pk>/edit/", views.savings_edit, name="savings_edit"),
    path("savings/<int:pk>/delete/", views.savings_delete, name="savings_delete"),
    path("tax/", views.tax_calculator, name="tax"),
]
