from django.contrib.gis.utils import LayerMapping

from .models import HealthFacility

health_facility_mapping = {
	'name': 'F_NAME',
	'geom': 'POINT',
	'district': 'DIST',
	'location': 'LOCATION',
	'sub_location': 'SUB_LOCATI',
	'agency': 'AGENCY',
	'level': 'LEVEL',
}

health_facility_shp = '/home/oty/Desktop/Axis/Axis Innovate4Life/kisii_health/kisii_health.shp'


def load_health_facilities(verbose=True):
	lm = LayerMapping(
		HealthFacility, health_facility_shp, health_facility_mapping,
		transform=False, encoding='iso-8859-1',
	)
	lm.save(strict=True, verbose=verbose)
