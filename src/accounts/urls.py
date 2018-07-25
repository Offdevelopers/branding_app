from django.conf.urls import url
from django.contrib.auth.views import(
    login,logout,logout_then_login,
    password_change,password_change_done,
    password_reset,password_reset_done,
    password_reset,password_reset_confirm,
    password_reset_complete
)
from . import views


urlpatterns = [
   url(r'^login/$', login, {'template_name':'accounts/login.html'}, name='sign_in'),
   url(r'^logout/$', logout, {'template_name':'accounts/login.html'}, name='logout'),
   url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

   # change password urls
   url(r'^password-change/$', password_change, {'template_name':'accounts/login.html'}, name='password_change'),
   url(r'^password-change/done/$', password_change_done, {'template_name':'accounts/login.html'},  name='password_change_done'),

   # restore password urls
   url(r'^password-reset/$',password_reset, {'template_name':'accounts/login.html'}, name='password_reset'),
   url(r'^password-reset/done/$',password_reset_done, {'template_name':'accounts/login.html'}, name='password_reset_done'),
   url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,{'template_name':'accounts/login.html'},  name='password_reset_confirm'),
   url(r'^password-reset/complete/$',password_reset_complete, {'template_name':'accounts/login.html'}, name='password_reset_complete'),

   url(r'^brand-signup/$', views.register,  name='register'),
   url(r'^influncer-signup/$', views.register, {'template_name':'accounts/influencer_register.html'}, name=''),
   url(r'^edit/$', views.edit, name='edit'),

]