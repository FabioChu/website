from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scienceDMZ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','usersManagement.views.user_login',name='home'),
    url(r'^scp/','measureTools.views.scp_tool', name='scp'),
    url(r'^gridftp/','measureTools.views.gridftp_tool', name='gridftp'),
    url(r'^wget/','measureTools.views.wget_tool', name='wget'),
    url(r'^logout/', 'usersManagement.views.user_logout', name='logout'),
	url(r'^register/', 'usersManagement.views.register', name='register'),
    url(r'^data_scp/', 'measureTools.views.data_scp', name='data_scp'),
)
