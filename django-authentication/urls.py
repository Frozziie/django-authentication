from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include

from .apps.core import views

# -------------------------------------------- #
# //////////////////////////////////////////// #
# -------------------------------------------- #

urlpatterns = [
    path('', views.home, name='home'),

    path('accounts/signup/', views.signup, name='signup'),

    path('accounts/login/', LoginView.as_view(template_name='core/registration/login.html', redirect_authenticated_user=True), name='login'),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='core/registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(template_name='core/registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='core/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='core/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='core/registration/password_change_form.html'), name='password_change'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('secret/', views.secret_page, name="secret"),
    path('secret_class/', views.SecretPage.as_view(), name="secret_class"),

    path('admin/', admin.site.urls),
]
