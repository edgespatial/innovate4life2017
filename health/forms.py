from django import forms


class HealthSearchForm(forms.Form):
	COUNTY_CHOICES = (
		('KISII', 'KISII'),
		('NAIROBI', 'NAIROBI'),
		('LAMU', 'LAMU'),
		('BOMET', 'BOMET'),
	)
	LEVEL_CHOICES = (
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)
	county = forms.CharField(widget=forms.Select(
		choices=COUNTY_CHOICES
	))
	level = forms.CharField(widget=forms.Select(
		choices=LEVEL_CHOICES
	))
