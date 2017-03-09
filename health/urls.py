from django.conf.urls import url

from .views import DashboardView, PrenatalView, analysis_view

urlpatterns = [
	url(r'^$', DashboardView, name='dashboard'),
	url(r'^prenatal', PrenatalView, name='prenatal'),
	url(r'^analysis', analysis_view, name='analysis'),

]
