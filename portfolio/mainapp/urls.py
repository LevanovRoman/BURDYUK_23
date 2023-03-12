from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django_email_verification import urls as mail_urls

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('portfolio/', PortfolioPage.as_view(), name='portfolio'),
    path('price/', PricePage.as_view(), name='price'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('portfolio_post/<slug:portf_slug>/', PortfolioPost.as_view(), name='portfolio_post'),
    path('login/', LoginUser.as_view(), name='login_page'),
    path('register/', RegisterUser.as_view(), name='register_page'),
    path('logout/', LogoutUser.as_view(), name='logout_page'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="mainapp/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="mainapp/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="mainapp/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="mainapp/password_reset_done.html"),
         name="password_reset_complete"),

    path('email/', include(mail_urls)),
    re_path('^send_email/$', sendEmail),

]