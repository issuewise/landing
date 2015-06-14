from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from landing.views import email

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        regex = r'^$',
        view =  TemplateView.as_view(template_name='landing.html'),
        name = 'landing',
        ),
    url(
        r'^admin/', 
        include(admin.site.urls)
        ),
    url(
        regex = r'^emails',
        view = email,
        name = 'email',
        ),
)