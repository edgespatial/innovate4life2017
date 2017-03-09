from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import Context
from django.template.loader import render_to_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from health.forms import HealthSearchForm
from health.models import HealthFacility, Mother, SupportGroup
from health.serializers import HealthFacilitySerializer, MotherSerializer


# Create your views here.


# class DashboardView(LoginRequiredMixin, TemplateView):
# 	login_url = '/login/'
# 	redirect_field_name = 'next'
# 	template_name = 'dashboard.html'
#
# 	def get_context_data(self, **kwargs):
# 		context = super(DashboardView, self).get_context_data(**kwargs)
# 		context['hospital_name'] = HealthFacility.objects
# 		return context

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='Hospital Admins').count() == 1, login_url='/login/')
def DashboardView(request):
	user = request.user
	context = {
		'health_centre_name': user.healthfacility.name,
	}
	return render(request, 'dashboard.html', context)


class HealthFacilityData(viewsets.ModelViewSet, ):
	queryset = HealthFacility.objects.all()
	serializer_class = HealthFacilitySerializer


class MotherData(viewsets.ModelViewSet):
	queryset = Mother.objects.all()
	serializer_class = MotherSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('home_health_facility', 'group', 'first_visit', 'second_visit', 'third_visit', 'fourth_visit',)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='Hospital Admins').count() == 1, login_url='/login/')
def PrenatalView(request):
	user = request.user
	under_prenatal = Mother.objects.filter(home_health_facility__id=user.healthfacility.id,
	                                       first_visit__complete=True)
	complete_first_visit = Mother.objects.filter(home_health_facility__id=user.healthfacility.id,
	                                             first_visit__complete=True)
	complete_second_visit = Mother.objects.filter(home_health_facility__id=user.healthfacility.id,
	                                              second_visit__complete=True)
	complete_third_visit = Mother.objects.filter(home_health_facility__id=user.healthfacility.id,
	                                             third_visit__complete=True)
	complete_fourth_visit = Mother.objects.filter(home_health_facility__id=user.healthfacility.id,
	                                              fourth_visit__complete=True)
	print under_prenatal
	context = {
		'health_centre_name': user.healthfacility.name,
		'under_prenatal': under_prenatal,
		'first_complete': complete_first_visit,
		'second_complete': complete_second_visit,
		'third_complete': complete_third_visit,
		'fourth_complete': complete_fourth_visit,
	}
	return render(request, 'prenatal.html', context)


@api_view(['GET', 'POST'])
def health_search(request):
	if request.method == 'POST':
		data = {'county': request.data.get('county'), 'level': request.data.get('level')}
		results = HealthFacility.objects.filter(level=data['level'])
		serializer = HealthFacilitySerializer(results, many=True)
		context = Context({'centres': results})
		return_str = render_to_string('partials/_health_search.html', context)
		return Response(return_str)
	else:
		form = HealthSearchForm
	return render(request, 'healthfacility.html', {'form': form})


def health_centre_detail(request, id):
	centre = get_object_or_404(HealthFacility, id=id)
	return render(request, 'centre_detail.html', {'centre': centre})


def group_list(request, id):
	groups = SupportGroup.objects.filter(health_facility__id=id)
	return render(request, 'groups.html', {'groups': groups})


def group_detail(request, groupid):
	group = SupportGroup.objects.get(id=groupid)
	return render(request, 'group_detail.html', {'group': group})


def donation_view(request):
	return render(request, 'donate.html')


def analysis_view(request):
	return render(request, 'analysis.html')
