from django import forms

from scraping.models import City, Metro


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Город'
    )
    metro = forms.ModelChoiceField(
        queryset=Metro.objects.all(), to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Станция метро'
    )
