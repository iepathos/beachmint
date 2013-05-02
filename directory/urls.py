from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from .views import DirectoryView, FileDetailView, FileUpdateView, FolderDetailView, FolderUpdateView

urlpatterns = patterns('',
	url(r'^(?P<username>[\.\w-]+)/$', DirectoryView.as_view(), name='directory_list'),

	# File and Folder urls broken down to
	# username/object_id
	url(r'^(?P<username>[\.\w-]+)/(?P<pk>\d+)/$', 
			FileDetailView.as_view(), 
			name='file_detail'),
	
	url(r'^(?P<username>[\.\w-]+)/update/(?P<pk>\d+)/$', 
			FileUpdateView.as_view(), 
			name='file_update'),

	url(r'^(?P<username>[\.\w-]+)/(?P<pk>\d+)/$', 
			FolderDetailView.as_view(), 
			name='folder_detail'),

	url(r'^(?P<username>[\.\w-]+)/update/(?P<pk>\d+)/$', 
			FolderUpdateView.as_view(), 
			name='folder_update'),
)