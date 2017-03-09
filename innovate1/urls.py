"""innovate1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import (login_view, register_view, logout_view)
from health.views import (HealthFacilityData, MotherData, health_search, health_centre_detail,
                          group_list, donation_view, group_detail)
from .views import Index

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^register/', register_view, name='register'),
	url(r'^login/', login_view, name='login'),
	url(r'^logout/', logout_view, name='logout'),
	url(r'^$', Index.as_view(), name='index'),
	url(r'^dashboard/', include('health.urls')),
	url(r'^api/', include([
		url(r'healthfacilitiesdata/(?P<pk>\d+)', HealthFacilityData.as_view({'get': 'retrieve'}),
		    name='all-health-facilities'),
		url(r'^motherdata/', MotherData.as_view({'get': 'list'}), name='motherdata'),
	])),
	url(r'^healthfacilities/', include([
		url(r'^$', health_search, name='health-search'),
		url(r'^(?P<id>\d+)', health_centre_detail, name='centre_detail'),
		url(r'^groups/', include([
			url(r'^(?P<id>\d+)', group_list, name='group_list'),
			url(r'^detail/(?P<groupid>\d+)', group_detail, name='group_detail'),
		])
		    ),
		url(r'^donate', donation_view, name='donation_view'),
	])),

]
