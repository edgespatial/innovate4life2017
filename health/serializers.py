from rest_framework_gis.serializers import GeoFeatureModelSerializer

from health.models import HealthFacility, Mother


class HealthFacilitySerializer(GeoFeatureModelSerializer):
	class Meta:
		model = HealthFacility
		geo_field = 'geom'
		fields = ('name', 'district', 'location', 'sub_location', 'agency')


class MotherSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Mother
		geo_field = 'home_location'
		exclude = ()