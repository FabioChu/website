from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scienceDMZ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','measureTools.views.scp_tool', name='scp'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', 'usersManagement.views.user_login', name='main'),
    url(r'^logout/', 'usersManagement.views.user_logout', name='logout'),
	url(r'^register/', 'usersManagement.views.register', name='register'),
)
