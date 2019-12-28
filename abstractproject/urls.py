"""abstractproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static



# added for redux
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import (password_reset, password_reset_done,
                               password_reset_confirm, password_reset_complete,
                               password_change, password_change_done,)
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



# added for redux to create a class that redirects user to index page
# if successful at logging.
class MyRegistrationView(RegistrationView):
    def get_success_url (self, user):
       return  '/journal/register_profile/'





urlpatterns = [
    path('admin/', admin.site.urls),
    path('journal/', include('journal.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
     # added for redux, to redirect page to index after registraton.
    path('accounts/register/', MyRegistrationView.as_view(), name = 'registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),

    # added for redux password reset and change
    path(r'password/reset/',
         auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('auth_password_reset_done'),
            html_email_template_name='registration/password_reset_email.html'),
            name='auth_password_reset'),
    path(r'accounts/password/reset/', password_reset,{'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    path(r'accounts/password/reset/done/', password_reset_done,{'template_name':'registration/password_reset_done.html'},
        name="password_reset_done"),
    re_path(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name':'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    path(r'accounts/password/done/', password_reset_complete, {'template_name':
        'registration/password_reset_complete.html'}, name="password_reset_complete"),
    path(r'accounts/password/change/', password_change, {'template_name': 'registration/password_change_form.html'}, 
        name='password_change'),
    path(r'accounts/password/change/done/', password_change_done, {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
