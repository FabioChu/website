from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scienceDMZ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', 'usersManagement.views.main', name='main'),
	url(r'^register/', 'usersManagement.views.register', name='register'),
)
