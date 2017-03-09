from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import (HealthFacility, MidWife, SupportGroup, Mother, FirstVisit, SecondVisit, ThirdVisit, FourthVisit)

admin.site.site_header = 'Axis Mother & Child Admin'


class HealthFacilityAdmin(LeafletGeoAdmin):
	settings_overrides = {
		'DEFAULT_CENTER': (-1.30323720, 36.77813964),
	}


class MotherAdmin(LeafletGeoAdmin):
	settings_overrides = {
		'DEFAULT_CENTER': (-1.30323720, 36.77813964),
	}


class SupportGroupAdmin(LeafletGeoAdmin):
	settings_overrides = {
		'DEFAULT_CENTER': (-0.800545, 34.724808),
	}


class MidwifeAdmin(LeafletGeoAdmin):
	settings_overrides = {
		'DEFAULT_CENTER': (-0.800545, 34.724808),
	}


admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(MidWife, MidwifeAdmin)
admin.site.register(SupportGroup, SupportGroupAdmin)
admin.site.register(Mother, MotherAdmin)
admin.site.register(FirstVisit)
admin.site.register(SecondVisit)
admin.site.register(ThirdVisit)
admin.site.register(FourthVisit)
