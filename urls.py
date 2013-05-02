from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include('admin_honeypot.urls')),
    url(r'^secret/', include('admin_honeypot.urls')),
    url(r'^funkstank/', include(admin.site.urls)),
    
    url(r'^accounts/', include('userena.urls')),
    #url(r'^messages/', include('userena.contrib.umessages.urls')),

    #url(r'^activity/', include('actstream.urls')),
    
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL +'ico/favicon.ico')), #favicon fix

	url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
	url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),

	url(r'', include('social_auth.urls')),
	#url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
	#url(r'^associate/$', TemplateView.as_view(template_name='associate.html'), name='associate'),

    url(r'^features/responsivedesign/$', TemplateView.as_view(template_name='features/responsivedesign.html'), name='feature_responsive_design'),

    url(r'^directory/', include('directory.urls')),

    url(r'^jewelry/', include('jewelry.urls')),
)
